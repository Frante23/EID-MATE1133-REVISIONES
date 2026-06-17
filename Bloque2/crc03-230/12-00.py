
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

canvas_grafico = None
figura = None
def validar_entrada(funcion_texto, valor_texto):

    if funcion_texto.strip() == "" or valor_texto.strip() == "":
        return False, "Debes completar todos los campos."
    return True, ""
def es_indeterminado(valor):

    if valor is None:
        return True
    if valor in (sp.nan, sp.zoo):
        return True


    if valor.is_finite is not True:
        return True
    return False
def calcular_limite(funcion_texto, valor_texto):

    x = sp.Symbol('x')
    try:

        valor_h     = sp.sympify(valor_texto)
        funcion_sym = sp.sympify(funcion_texto)




        if valor_h not in (sp.oo, -sp.oo):
            sustitucion = funcion_sym.subs(x, valor_h)
            resultado   = sp.simplify(sustitucion)
            if not es_indeterminado(resultado):
                return True, resultado, funcion_sym, valor_h




        funcion_cancelada   = sp.cancel(funcion_sym)
        funcion_factorizada = sp.factor(funcion_cancelada)
        if valor_h not in (sp.oo, -sp.oo):
            sustitucion2 = funcion_factorizada.subs(x, valor_h)
            resultado2   = sp.simplify(sustitucion2)
            if not es_indeterminado(resultado2):
                return True, resultado2, funcion_sym, valor_h



        if valor_h in (sp.oo, -sp.oo):


            signo  = 1 if valor_h == sp.oo else -1
            puntos = [signo * 10**k for k in range(4, 10)]
            valores_convergencia = []
            for p in puntos:

                try:
                    val = float(funcion_sym.subs(x, p))
                    valores_convergencia.append(val)
                except Exception:

                    continue
            if len(valores_convergencia) < 2:
                return False, "No se pudo evaluar la funcion en el infinito", None, None


            convergio = True
            for i in range(len(valores_convergencia) - 1):
                difference = abs(valores_convergencia[i + 1] - valores_convergencia[i])
                if difference > 1e-2:
                    convergio = False
                    break
            if not convergio:
                return False, "El limite no converge posiblemente no existe", None, None
            resultado_num = valores_convergencia[-1]
        else:


            centro = float(valor_h)

            pasos_h      = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7]
            val_izq_prev = None
            val_der_prev = None
            for h in pasos_h:
                try:
                    val_izq = float(funcion_sym.subs(x, centro - h))
                    val_der = float(funcion_sym.subs(x, centro + h))
                except Exception:
                    continue

                val_izq_prev = val_izq
                val_der_prev = val_der


            if val_izq_prev is None or val_der_prev is None:
                return False, "No se pudo evaluar numericamente la funcion", None, None



            if abs(val_der_prev - val_izq_prev) > 1e-4:
                return False, "El limite no existe limites laterales distintos", None, None


            resultado_num = (val_izq_prev + val_der_prev) / 2



        resultado = sp.nsimplify(resultado_num, rational=True, tolerance=1e-5)
        return True, resultado, funcion_sym, valor_h

    except Exception as error:
        return False, str(error), None, None


def limpiar_grafico():
    global canvas_grafico, figura

    if canvas_grafico is not None:
        canvas_grafico.get_tk_widget().destroy()
        canvas_grafico = None

    if figura is not None:
        plt.close(figura)
        figura = None


def graficar_funcion(funcion_sym, valor_h, resultado_limite, frame_grafico):
    global canvas_grafico, figura
    limpiar_grafico()
    x = sp.Symbol('x')


    if valor_h in (sp.oo, -sp.oo):
        x_inicio, x_fin = (10, 200) if valor_h == sp.oo else (-200, -10)
    else:
        x_centro = float(valor_h)
        x_inicio = x_centro - 5
        x_fin    = x_centro + 5


    puntos_x_validos = []
    puntos_y = []
    px   = x_inicio
    paso = 0.5 if valor_h in (sp.oo, -sp.oo) else 0.05

    while px <= x_fin:

        cerca = valor_h not in (sp.oo, -sp.oo) and abs(px - float(valor_h)) <= 0.03
        if not cerca:
            try:
                valor_y = float(funcion_sym.subs(x, px))

                if abs(valor_y) <= 1000:
                    puntos_x_validos.append(px)
                    puntos_y.append(valor_y)
            except:
                pass
        px += paso


    figura = plt.Figure(figsize=(6, 4), dpi=100)
    figura.patch.set_facecolor('#2d1b2e')
    ax = figura.add_subplot(111)
    ax.set_facecolor('#3a1f3c')
    ax.plot(puntos_x_validos, puntos_y,
            color='#ed93b1', linewidth=2,
            label=f'f(x) = {funcion_sym}')

    try:
        limite_float = float(resultado_limite)

        if valor_h not in (sp.oo, -sp.oo):
            ax.plot(float(valor_h), limite_float, 'o',
                    color='#ff6eb4', markersize=10,
                    markerfacecolor='#2d1b2e',
                    markeredgecolor='#ff6eb4',
                    markeredgewidth=2,
                    label=f'Limite = {resultado_limite}', zorder=5)
            ax.axvline(x=float(valor_h), color='#f4c0d1',
                       linestyle='--', alpha=0.4, linewidth=1)
        ax.axhline(y=limite_float, color='#f4c0d1',
                   linestyle='--', alpha=0.4, linewidth=1,
                   label=f'Limite = {resultado_limite}')
    except:
        pass


    ax.set_title(f'f(x) = {funcion_sym}', color='#f4c0d1', fontsize=11, pad=10)
    ax.set_xlabel('x',    color='#c490c8')
    ax.set_ylabel('f(x)', color='#c490c8')
    ax.tick_params(colors='#c490c8')
    for spine in ax.spines.values():
        spine.set_color('#5c3060')
    ax.legend(facecolor='#4a1b4e', edgecolor='#993556',
              labelcolor='#f4c0d1', fontsize=9)
    ax.grid(True, alpha=0.2, color='#5c3060')
    figura.tight_layout()


    canvas_grafico = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)


def boton_calcular(entry_funcion, entry_valor, label_resultado, frame_grafico):
    texto_funcion = entry_funcion.get()
    texto_valor   = entry_valor.get()


    es_valido, mensaje_error = validar_entrada(texto_funcion, texto_valor)
    if not es_valido:
        messagebox.showerror("Error", mensaje_error)
        return


    exito, resultado, funcion_sym, valor_h = calcular_limite(texto_funcion, texto_valor)
    if not exito:
        messagebox.showerror("Error al calcular", f"No se pudo calcular el limite\n{resultado}")
        label_resultado.configure(text="Error al calcular", text_color="#ff6eb4")
        return


    label_resultado.configure(
        text=f"lim f(x) = {resultado}   (x -> {valor_h})",
        text_color="#ed93b1"
    )


    try:
        graficar_funcion(funcion_sym, valor_h, resultado, frame_grafico)
    except Exception as e:
        messagebox.showwarning("Advertencia", f"Limite calculado pero error al graficar\n{e}")


def boton_limpiar(entry_funcion, entry_valor, label_resultado):

    entry_funcion.delete(0, "end")
    entry_valor.delete(0, "end")
    label_resultado.configure(
        text="Ingresa una funcion y presiona Calcular Limite",
        text_color="#9b6b9e"
    )
    limpiar_grafico()


def crear_ventana():

    ventana = ctk.CTk()
    ventana.title("Calculadora de Limites")
    ventana.geometry("850x680")


    ctk.CTkLabel(ventana, text="Calculadora de Limites",
                 font=ctk.CTkFont(size=20, weight="bold"),
                 text_color="#f4c0d1").pack(pady=(20, 3))
    ctk.CTkLabel(ventana, text="Calculo I - Ingenieria Civil Informatica",
                 font=ctk.CTkFont(size=12),
                 text_color="#9b6b9e").pack(pady=(0, 15))


    frame_entradas = ctk.CTkFrame(ventana, corner_radius=10,
                                  fg_color="#3a1f3c",
                                  border_color="#5c3060",
                                  border_width=1)
    frame_entradas.pack(padx=20, pady=5, fill="x")

    ctk.CTkLabel(frame_entradas, text="f(x):",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1").grid(row=0, column=0, padx=15, pady=12)
    entry_funcion = ctk.CTkEntry(frame_entradas, width=280,
                                 placeholder_text="Ej: (x**2 - 1)/(x - 1)",
                                 font=ctk.CTkFont(size=12),
                                 fg_color="#4a1b4e",
                                 border_color="#993556",
                                 text_color="#f4c0d1")
    entry_funcion.grid(row=0, column=1, padx=10, pady=12)

    ctk.CTkLabel(frame_entradas, text="x tiende a:",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1").grid(row=0, column=2, padx=15)
    entry_valor = ctk.CTkEntry(frame_entradas, width=120,
                               placeholder_text="Ej: 1, 0, oo",
                               font=ctk.CTkFont(size=12),
                               fg_color="#4a1b4e",
                               border_color="#993556",
                               text_color="#f4c0d1")
    entry_valor.grid(row=0, column=3, padx=10)


    frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_botones.pack(pady=10)

    ctk.CTkButton(frame_botones, text="Calcular Limite",
                  font=ctk.CTkFont(size=14, weight="bold"), height=40, width=200,
                  fg_color="#993556",
                  hover_color="#72243e",
                  corner_radius=8,
                  command=lambda: boton_calcular(entry_funcion, entry_valor,
                                                 label_resultado, frame_grafico)
                  ).grid(row=0, column=0, padx=15)

    ctk.CTkButton(frame_botones, text="Limpiar",
                  font=ctk.CTkFont(size=14), height=40, width=130,
                  fg_color="#5c3060",
                  hover_color="#4a1b4e",
                  corner_radius=8,
                  command=lambda: boton_limpiar(entry_funcion, entry_valor, label_resultado)
                  ).grid(row=0, column=1, padx=15)


    frame_resultado = ctk.CTkFrame(ventana, corner_radius=10, height=55,
                                   fg_color="#3a1f3c",
                                   border_color="#5c3060",
                                   border_width=1)
    frame_resultado.pack(padx=20, pady=5, fill="x")
    frame_resultado.pack_propagate(False)

    label_resultado = ctk.CTkLabel(frame_resultado,
                                   text="Ingresa una funcion y presiona Calcular Limite",
                                   font=ctk.CTkFont(size=14),
                                   text_color="#9b6b9e")
    label_resultado.pack(expand=True)


    ctk.CTkLabel(ventana, text="Grafica",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1",
                 anchor="w").pack(padx=25, pady=(5, 0), anchor="w")

    frame_grafico = ctk.CTkFrame(ventana, corner_radius=10,
                                 fg_color="#3a1f3c",
                                 border_color="#5c3060",
                                 border_width=1)
    frame_grafico.pack(padx=20, pady=(5, 10), fill="both", expand=True)


    ctk.CTkLabel(ventana, text="Usa ** para potencias   Ej: x**2   o   (x**3 - 8)/(x - 2)",
                 font=ctk.CTkFont(size=10),
                 text_color="#6b3d70").pack(pady=(0, 8))


    ventana.mainloop()


if __name__ == "__main__":

    crear_ventana()