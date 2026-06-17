






import customtkinter as ctk
import matplotlib.pyplot as plt
import sympy as sp
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg





ctk.set_appearance_mode("Light")
ctk.set_default_color_theme("blue")


vp = ctk.CTk()
vp.title("Analizador y Visualizador de Límites")
vp.geometry("1200x700")


vp.grid_columnconfigure(0, weight=1)
vp.grid_rowconfigure(3, weight=1)


marco_superior = ctk.CTkFrame(vp)
marco_superior.grid(row=0, column=0, padx=20, pady=20, sticky="ew")


campo_funcion = ctk.CTkEntry(marco_superior, placeholder_text="Función f(x)=")
campo_funcion.pack(side="left", padx=10, fill="x", expand=True)


campo_limite = ctk.CTkEntry(marco_superior, placeholder_text="h tiende a")
campo_limite.pack(side="left", padx=10)

boton_calcular = ctk.CTkButton(marco_superior, text="Calcular límite")
boton_calcular.pack(side="left", padx=10)


etiqueta_resultado = ctk.CTkLabel(vp, text="Resultado:", font=("Arial", 18))
etiqueta_resultado.grid(row=1, column=0)


texto_ayuda =   "  SINTAXIS:  Multiplicar -> 3*x  |  Dividir -> x/2  " \
                "|  Potencia -> x**2  |  raiz(x)  |  Infinito -> oo          " \
                "TRIGONOMETRICO:  sin(x)  |  cos(x)  |  tan(x)"
panel_ayuda = ctk.CTkLabel(vp, text=texto_ayuda, font=("Consolas", 11),
                            text_color="#003399", fg_color="#dce8ff",
                            corner_radius=8, anchor="w", padx=14, pady=7)
panel_ayuda.grid(row=2, column=0, padx=20, pady=(0, 2), sticky="ew")


marco_grafico = ctk.CTkFrame(vp, fg_color="white")
marco_grafico.grid(row=3, column=0, padx=20, pady=20, sticky="nsew")






def crear_grafico(contenedor):
    figura, ejes = plt.subplots(figsize=(8, 5))
    figura.patch.set_facecolor("#FFFFFF")

    ejes.set_facecolor("#ffffff")
    ejes.tick_params(colors="black")

    for borde in ejes.spines.values():
        borde.set_edgecolor("#000000")


    ejes.set_xlim(0, 10)
    ejes.set_ylim(0, 10)

    ejes.axhline(0, color='black', linewidth=0.8)
    ejes.axvline(0, color='black', linewidth=0.8)
    ejes.grid(True, linestyle='--', alpha=0.5, color='gray')

    lienzo = FigureCanvasTkAgg(figura, master=contenedor)
    lienzo.get_tk_widget().pack(fill="both", expand=True)
    return figura, ejes, lienzo





def ejecutar_analsis():
    global ejes_grafico, lienzo_grafico

    texto_usuario = campo_funcion.get().strip()

    texto_funcion = texto_usuario.replace('raiz', 'sqrt').replace('^', '**')
    texto_limite = campo_limite.get().strip()


    if not texto_funcion or not texto_limite:
        return

    ejes_grafico.clear()
    ejes_grafico.set_facecolor("#ffffff")

    try:
        x = sp.Symbol("x")
        funcion_simbolo = sp.sympify(texto_funcion)


        aprox = 0.0001
        es_infinito = texto_limite.lower() in ["oo", "inf", "infinito"]

        if es_infinito:

            val_grande  = float(funcion_simbolo.subs(x, 1e6).evalf())
            val_grande2 = float(funcion_simbolo.subs(x, 1e7).evalf())


            if abs(val_grande2 - val_grande) < 0.01:
                resultado = (val_grande + val_grande2) / 2
            else:
                resultado = None

        else:
            centro = float(sp.sympify(texto_limite))


            valor_izquierdo = float(funcion_simbolo.subs(x, centro - aprox).evalf())
            valor_derecho = float(funcion_simbolo.subs(x, centro + aprox).evalf())


            if abs(valor_derecho - valor_izquierdo) < 0.1:
                resultado = (valor_derecho + valor_izquierdo) / 2
            else:
                resultado = None


        if resultado is not None:
            texto_final = f"Resultado: {resultado:.2f}"
            etiqueta_resultado.configure(text=texto_final, text_color="#000000")
        else:
            texto_final = "Resultado: No existe el límite. \n Indefinido."
            etiqueta_resultado.configure(text=texto_final, text_color="#000000")


        if es_infinito:
            inicio = 0.0
            ancho_total = 100.0
        else:
            ancho_total = 10.0
            inicio = centro - (ancho_total / 2)

        paso = ancho_total / 300


        lista_x = []
        for i in range(301):
            lista_x.append(inicio + (i * paso))


        lista_y = []
        for d in lista_x:
            try:
                valor = funcion_simbolo.subs(x, d).evalf()
                if valor.is_real:
                    lista_y.append(float(valor))
                else:
                    lista_y.append(None)
            except:
                lista_y.append(None)

        ejes_grafico.plot(lista_x, lista_y,
                          color="#0066FF", linewidth=2,
                          label="f(x)")


        if resultado is not None:
            if not es_infinito:
                ejes_grafico.plot(centro, resultado, "ro",
                                  markersize=10, label="Límite", zorder=5)
                ejes_grafico.set_xlim(centro - 4, centro + 4)
                ejes_grafico.set_ylim(resultado - 5, resultado + 5)


                if not isinstance(resultado, str):
                    ejes_grafico.set_ylim(resultado - 5, resultado + 5)
                else:

                    valores_reales = [y for y in lista_y if y is not None]
                    if valores_reales:
                            ejes_grafico.set_ylim(min(valores_reales[:150]),
                                                  max(valores_reales[:150]))


        ejes_grafico.axhline(0, color='black', linewidth=0.8)
        ejes_grafico.axvline(0, color='black', linewidth=0.8)
        ejes_grafico.grid(True, linestyle='--', alpha=0.5, color='gray')
        ejes_grafico.legend(facecolor="#FFFFFF", labelcolor='black')

        lienzo_grafico.draw()

    except Exception as e:

        etiqueta_resultado.configure(text="Error de sintaxis", text_color="red")
        lienzo_grafico.draw()

boton_calcular.configure(command=ejecutar_analsis)
figura_grafico, ejes_grafico, lienzo_grafico = crear_grafico(marco_grafico)


if __name__ == "__main__":
    vp.mainloop()
