import customtkinter as ctk
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

x = sp.Symbol('x')

app = ctk.CTk()
app.title("EID MATE1133 - Analizador y Visualizador de Límites")
app.geometry("1000x600")


def calcular_limite(f, h):

    pasos = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0001, 0.00001]

    izquierda = []
    derecha = []

    for paso in pasos:
        try:
            val_izq = float(f.subs(x, h - paso))
            izquierda.append(val_izq)
        except:
            izquierda.append(None)

        try:
            val_der = float(f.subs(x, h + paso))
            derecha.append(val_der)
        except:
            derecha.append(None)


    izq = next((v for v in reversed(izquierda) if v is not None), None)
    der = next((v for v in reversed(derecha) if v is not None), None)

    if izq is None or der is None:
        return None, False, izquierda, derecha

    diff = abs(izq - der)
    escala = max(abs(izq), abs(der), 1)

    if diff / escala < 0.0001:
        valor = round((izq + der) / 2, 6)
        return valor, True, izquierda, derecha


    return None, False, izquierda, derecha


def formato_resultado(lim_sp):

    if lim_sp == sp.oo:
        return "+∞"
    if lim_sp == -sp.oo:
        return "-∞"
    if lim_sp == sp.zoo:
        return "∞ (complejo)"
    if lim_sp is sp.nan or lim_sp == sp.nan:
        return "indeterminado"
    return str(lim_sp)


def boton_calcular():
    try:
        texto_f = entry_funcion.get().strip()
        texto_h = entry_h.get().strip()

        if not texto_f or not texto_h:
            label_resultado.configure(text="Error: ingresa una función y un valor h")
            return


        permitidos = {
            "x": x,
            "sin": sp.sin, "cos": sp.cos, "tan": sp.tan,
            "sqrt": sp.sqrt, "log": sp.log, "exp": sp.exp,
            "oo": sp.oo, "pi": sp.pi, "E": sp.E,
        }

        f = sp.sympify(texto_f, locals=permitidos)
        h = sp.sympify(texto_h, locals=permitidos)


        if f.free_symbols and x not in f.free_symbols:
            label_resultado.configure(text="Error: la función debe contener la variable x")
            return

        resultado_limite_sympy = None

        try:
            h_num = float(h)
        except (TypeError, ValueError):
            h_num = None


        if h_num is not None and abs(h_num) != float('inf'):


            if not f.free_symbols:
                valor_cte = float(f)
                label_resultado.configure(
                    text=f"Límite = {valor_cte}\n(función constante)"
                )
                resultado_limite_sympy = f

            else:

                valor, existe, aprox_izq, aprox_der = calcular_limite(f, h_num)

                izq_mostrar = next((v for v in reversed(aprox_izq) if v is not None), None)
                der_mostrar = next((v for v in reversed(aprox_der) if v is not None), None)


                try:
                    resultado_limite_sympy = sp.limit(f, x, h)
                    validacion = f"\nValidación SymPy: {formato_resultado(resultado_limite_sympy)}"
                except:
                    validacion = ""

                if existe:
                    texto = f"Límite ≈ {valor}"
                    if izq_mostrar is not None:
                        texto += f"\n\nIzquierda ≈ {round(izq_mostrar, 6)}"
                    if der_mostrar is not None:
                        texto += f"\nDerecha   ≈ {round(der_mostrar, 6)}"
                    texto += validacion
                else:
                    texto = "El límite no existe\n(límites laterales distintos)"
                    if izq_mostrar is not None:
                        texto += f"\n\nIzquierda ≈ {round(izq_mostrar, 6)}"
                    if der_mostrar is not None:
                        texto += f"\nDerecha   ≈ {round(der_mostrar, 6)}"
                    texto += validacion

                label_resultado.configure(text=texto)

        else:

            try:
                resultado_limite_sympy = sp.limit(f, x, h)
                label_resultado.configure(
                    text=f"Resultado: {formato_resultado(resultado_limite_sympy)}"
                )
            except Exception as e:
                label_resultado.configure(text=f"No se pudo calcular: {e}")


        ax.clear()

        if h_num is not None and abs(h_num) != float('inf'):
            rango = 5
            xs = [h_num - rango + i * (2 * rango / 300) for i in range(301)]
        else:
            xs = [i * 0.05 for i in range(-200, 201)]


        ys_raw = []
        for point in xs:
            try:
                y_val = float(f.subs(x, point))
                if abs(y_val) > 1000:
                    ys_raw.append(float('nan'))
                else:
                    ys_raw.append(y_val)
            except:
                ys_raw.append(float('nan'))


        validos = [v for v in ys_raw if v == v]
        if validos:
            vs = sorted(validos)
            n = len(vs)
            q1 = vs[n // 4]
            q3 = vs[(3 * n) // 4]
            iqr = q3 - q1
            margen = max(iqr * 3, 5)
            y_min_clip = q1 - margen
            y_max_clip = q3 + margen
        else:
            y_min_clip, y_max_clip = -50, 50

        ys = [v if (v == v and y_min_clip <= v <= y_max_clip) else float('nan') for v in ys_raw]

        if not any(v == v for v in ys):
            ax.text(0.5, 0.5, "Sin valores graficables\nen el rango seleccionado",
                    transform=ax.transAxes, ha="center", va="center",
                    fontsize=11, color="gray")
        else:
            ax.plot(xs, ys, color="#1f77b4", linewidth=2, label="f(x)")

        if h_num is not None and abs(h_num) != float('inf'):
            ax.axvline(x=h_num, color="#e74c3c", linestyle="--",
                       linewidth=1.5, label=f"x → {h}")


            ax.set_xlim(h_num - 2, h_num + 2)


            try:
                if resultado_limite_sympy is not None:
                    lim_float = float(resultado_limite_sympy)
                    if abs(lim_float) != float('inf') and y_min_clip <= lim_float <= y_max_clip:
                        ax.plot(h_num, lim_float, 'o', color="#f39c12",
                                markersize=8, label=f"lím ≈ {round(lim_float, 4)}")
            except (TypeError, ValueError):
                pass

        ax.grid(True, linestyle=":", alpha=0.6)

        handles, labels = ax.get_legend_handles_labels()
        if handles:
            ax.legend()

        ax.set_title("Comportamiento de la Función")
        ax.set_xlabel("x")
        ax.set_ylabel("f(x)")
        canvas.draw()

    except Exception as error:
        label_resultado.configure(text=f"Error: {str(error)}")



app.grid_columnconfigure(0, weight=0)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

frame_controles = ctk.CTkFrame(app, width=280, corner_radius=10)
frame_controles.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
frame_controles.grid_propagate(False)

ctk.CTkLabel(frame_controles, text="Configuración",
             font=ctk.CTkFont(size=18, weight="bold")).pack(pady=(20, 15))

ctk.CTkLabel(frame_controles, text="Función f(x):",
             font=ctk.CTkFont(size=13)).pack(anchor="w", padx=20, pady=(10, 2))
entry_funcion = ctk.CTkEntry(frame_controles, placeholder_text="Ej: sin(x)/x", width=240)
entry_funcion.pack(padx=20, pady=5)

ctk.CTkLabel(frame_controles, text="Valor de tendencia (h):",
             font=ctk.CTkFont(size=13)).pack(anchor="w", padx=20, pady=(10, 2))
entry_h = ctk.CTkEntry(frame_controles, placeholder_text="Ej: 0 u oo", width=240)
entry_h.pack(padx=20, pady=5)

ctk.CTkButton(frame_controles, text="Calcular y Graficar", command=boton_calcular,
              font=ctk.CTkFont(weight="bold")).pack(padx=20, pady=25)

ctk.CTkFrame(frame_controles, height=2, fg_color="gray").pack(fill="x", padx=20, pady=10)

label_resultado = ctk.CTkLabel(frame_controles, text="Resultado: ?",
                                font=ctk.CTkFont(size=14, weight="bold"), wraplength=240)
label_resultado.pack(padx=20, pady=15)

ctk.CTkFrame(frame_controles, height=2, fg_color="gray").pack(fill="x", padx=20, pady=(10, 15))

ctk.CTkLabel(frame_controles, text="Guía de Sintaxis:",
             font=ctk.CTkFont(size=13, weight="bold")).pack(anchor="w", padx=20, pady=(0, 5))
ctk.CTkLabel(
    frame_controles,
    text="• Potencias: x**2\n• Multiplicar: 3*x\n• Funciones: sin(x), cos(x), sqrt(x)\n• Infinito: oo\n• Agrupa con paréntesis ( )",
    font=ctk.CTkFont(size=11),
    justify="left",
    anchor="w"
).pack(padx=20, anchor="w")

frame_grafica = ctk.CTkFrame(app, corner_radius=10)
frame_grafica.grid(row=0, column=1, padx=(0, 15), pady=15, sticky="nsew")

fig, ax = plt.subplots(figsize=(5, 4), dpi=100)
ax.grid(True)

canvas = FigureCanvasTkAgg(fig, master=frame_grafica)
canvas.get_tk_widget().pack(fill="both", expand=True, padx=10, pady=10)

app.mainloop()