import customtkinter as ctk
import matplotlib.pyplot as plt
import math
import sympy as sp

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from logica import procesar_limite


def crear_pantalla_graficadora(ventana_maestra, comando_volver, estilo_frame, estilo_entrada, estilo_boton, fuente_retro):
    frame = ctk.CTkFrame(ventana_maestra, **estilo_frame)


    frame_barra = ctk.CTkFrame(frame, fg_color="#3B1F6B", corner_radius=0, height=30)
    frame_barra.pack(fill="x", padx=2, pady=2)


    frame_contenedor = ctk.CTkFrame(frame, fg_color="transparent")
    frame_contenedor.pack(fill="both", expand=True, padx=20, pady=20)


    frame_contenido = ctk.CTkFrame(frame_contenedor, fg_color="transparent")
    frame_contenido.pack(side="left", fill="both", expand=True, padx=(0,10))


    frame_pasos = ctk.CTkFrame(frame_contenedor, width=280, **estilo_frame)
    frame_pasos.pack(side="right", fill="y", padx=(10, 0))
    frame_pasos.pack_propagate(False)


    lbl_pasos = ctk.CTkLabel(frame_pasos, text="Paso a paso", font=("Courier New", 16, "bold"), text_color="black")
    lbl_pasos.pack(pady=(12, 6))


    textbox_pasos = ctk.CTkTextbox(frame_pasos, width=260, height=520, font=("Courier New", 12), fg_color="white", text_color="black", border_width=2, border_color="black", corner_radius=0, wrap="word")
    textbox_pasos.pack(padx=10, pady=(0, 10), fill="both", expand=True)


    textbox_pasos.insert("0.0", "El paso a paso del límite. \n")
    textbox_pasos.configure(state="disabled")


    lbl_barra = ctk.CTkLabel(frame_barra, text=" Graficar_Limites.exe", font=("Courier New", 12, "bold"), text_color="white")
    lbl_barra.pack(side="left", padx=10)


    boton_volver = ctk.CTkButton(frame_barra, text="[X] Cerrar", fg_color="black", text_color="white", hover_color="red", corner_radius=0, border_width=0, font=("Courier New", 12, "bold"), width=80, command=comando_volver)
    boton_volver.pack(side="right")


    def mostrar_pasos(func_str, h_str, resultado):
        textbox_pasos.configure(state="normal")
        textbox_pasos.delete("0.0", "end")


        textbox_pasos.insert("end", "PASO 1\n")
        textbox_pasos.insert("end", f"Se lee la función ingresada:\n")
        textbox_pasos.insert("end", f"f(x) = {func_str}\n\n")


        textbox_pasos.insert("end", "PASO 2\n")
        textbox_pasos.insert("end", f"Se identifica el punto al que tiende x:\n")
        textbox_pasos.insert("end", f"x -> {h_str}\n\n")

        try:
            x = sp.symbols('x')
            funcion = sp.sympify(func_str)
            h_val = sp.sympify(h_str)

            textbox_pasos.insert("end", "PASO 3\n")
            textbox_pasos.insert("end", "Se revisa el comportamiento por ambos lados del punto.\n")


            if not h_val.is_infinite:
                try:
                    lim_izq_sym = sp.limit(funcion, x, h_val, '-')
                    textbox_pasos.insert("end", f"Límite por la izquierda: {lim_izq_sym}\n")
                except Exception:
                    textbox_pasos.insert("end", "Límite por la izquierda: no se pudo calcular simbólicamente.\n")

                try:
                    lim_der_sym = sp.limit(funcion, x, h_val, '+')
                    textbox_pasos.insert("end", f"Límite por la derecha: {lim_der_sym}\n")
                except Exception:
                    textbox_pasos.insert("end", "Límite por la derecha: no se pudo calcular simbólicamente.\n")
            else:
                textbox_pasos.insert("end", "El punto es infinito, así que se analiza el comportamiento hacia el infinito.\n")


            textbox_pasos.insert("end", "\nPASO 4\n")
            textbox_pasos.insert("end", f"Tipo detectado: {resultado['tipo_limite']}\n")


            if resultado["salto"]:
                textbox_pasos.insert("end", "Los límites laterales son distintos.\n")
                textbox_pasos.insert("end", f"Aproximación izquierda: {resultado['lim_izq']}\n")
                textbox_pasos.insert("end", f"Aproximación derecha: {resultado['lim_der']}\n")
                textbox_pasos.insert("end", "Por eso el límite no existe como valor único.\n")
            else:
                textbox_pasos.insert("end", "No se detectó discontinuidad de salto.\n")


            textbox_pasos.insert("end", "\nPASO 5\n")
            textbox_pasos.insert("end", f"Resultado final del límite: {resultado['limite']}\n")


        except Exception as e:
            textbox_pasos.insert("end", "\nNo fue posible construir el paso a paso completo.\n")
            textbox_pasos.insert("end", f"Detalle: {str(e)}\n")


        textbox_pasos.configure(state="disabled")




    ventana_guia = None


    def abrir_guia():
        nonlocal ventana_guia


        if ventana_guia is None or not ventana_guia.winfo_exists():

            ventana_guia = ctk.CTkToplevel(ventana_maestra)
            ventana_guia.title("guia_sintaxis.txt")
            ventana_guia.geometry("380x360")
            ventana_guia.configure(fg_color="#D1D1D0")
            ventana_guia.attributes('-topmost', True)

            frame_guia = ctk.CTkFrame(ventana_guia, fg_color="#F4F0E6", border_width=3, border_color="black", corner_radius=0)
            frame_guia.pack(pady=15, padx=15, fill="both", expand=True)


            lbl_tit = ctk.CTkLabel(frame_guia, text="> SINTAXIS MATEMÁTICA", font=("Courier New", 15, "bold"), text_color="black")
            lbl_tit.pack(pady=(15, 10))


            texto_ayuda = (
                " * Potencia     : ** (Ej: x**2)\n"
                " * Raíz cuad.   : sqrt() (Ej: sqrt(x))\n"
                " * Infinito     : oo     (Letra 'o' x2)\n"
                " * Menos inf.   : -oo\n"
                " * Seno         : sin(x)\n"
                " * Coseno       : cos(x)\n"
                " * Tangente     : tan(x)\n"
                " * Exponencial  : exp(x)\n"
                " * Logaritmo    : log(x)\n"
                " * V. Absoluto  : abs(x)\n"
                " * Número Pi    : pi\n"
            )

            lbl_texto = ctk.CTkLabel(frame_guia, text=texto_ayuda, font=("Courier New", 13), text_color="black", justify="left")
            lbl_texto.pack(pady=5, padx=20, anchor="w")


            btn_ok = ctk.CTkButton(frame_guia, text="ENTENDIDO", **estilo_boton, command=ventana_guia.destroy)
            btn_ok.pack(pady=(15, 20))

        else:

            ventana_guia.focus()


    boton_guia = ctk.CTkButton(frame_barra, text="[?] Guía", fg_color="#3B1F6B", text_color="#E8D5FF", hover_color="#555555", corner_radius=0, border_width=0, font=("Courier New", 12, "bold"), width=80, command=abrir_guia)
    boton_guia.pack(side="right", padx=(0, 5))






    frame_controles = ctk.CTkFrame(frame_contenido, fg_color="transparent")
    frame_controles.pack(pady=20, padx=20, fill="x")


    entrada_funcion = ctk.CTkEntry(frame_controles, placeholder_text="f(x)", **estilo_entrada)
    entrada_funcion.pack(side="left", padx=10, expand=True, fill="x")


    entrada_h = ctk.CTkEntry(frame_controles, placeholder_text="h", width=100, **estilo_entrada)
    entrada_h.pack(side="left", padx=10)


    boton_calcular = ctk.CTkButton(frame_controles, text="Ejecutar", **estilo_boton)
    boton_calcular.pack(side="left", padx=10)
    boton_limpiar = ctk.CTkButton(frame_controles, text="Limpiar", **estilo_boton)
    boton_limpiar.pack(side="left", padx=10)


    etiqueta_resultado = ctk.CTkLabel(frame_contenido, text="> Esperando parámetros...", font=fuente_retro, text_color="black")
    etiqueta_resultado.pack(pady=5, anchor="w", padx=30)


    frame_canvas = ctk.CTkFrame(frame_contenido, border_width=3, border_color="#7E57C2", corner_radius=0)
    frame_canvas.pack(pady=15, padx=30, expand=True, fill="both")


    fig, ax = plt.subplots(figsize=(6, 4), dpi=100)
    fig.patch.set_facecolor("#F4F0E6")
    ax.set_facecolor("#F4F0E6")


    canvas = FigureCanvasTkAgg(fig, master=frame_canvas)
    canvas.get_tk_widget().pack(expand=True, fill="both", padx=2, pady=2)


    toolbar = NavigationToolbar2Tk(canvas, frame_canvas)
    toolbar.update()


    def accion_limpiar():
        entrada_funcion.delete(0, "end")
        entrada_h.delete(0, "end")
        ax.clear()
        ax.set_facecolor("#F0ECF8")
        fig.patch.set_facecolor("#F0ECF8")
        etiqueta_resultado.configure(text="> Esperando parámetros...")
        canvas.draw()


        textbox_pasos.configure(state="normal")
        textbox_pasos.delete("0.0", "end")
        textbox_pasos.insert("0.0", "El paso a paso del límite. \n")
        textbox_pasos.configure(state="disabled")


    def accion_calcular():
        func_str = entrada_funcion.get()
        h_str = entrada_h.get()
        resultado = procesar_limite(func_str, h_str)


        if resultado["exito"]:
            etiqueta_resultado.configure(text=f"> Resultado del límite: {resultado['limite']}")

            mostrar_pasos(func_str, h_str, resultado)


            ax.clear()
            ax.set_facecolor("#F4F0E6")
            fig.patch.set_facecolor("#F4F0E6")


            ax.plot(resultado["x_vals"], resultado["y_vals"], color='#5C3D8F', linewidth=2, label=f'f(x) = {func_str}')


            if resultado["marcar_asintota"]:
                ax.axvline(x=resultado["h_float"], color='#C084A0', linestyle='--', linewidth=2, label=f'h = {resultado["h_float"]}')


                if resultado["salto"]:
                    ax.plot(resultado["h_float"], resultado["lim_izq"], marker='o', markersize=8, markerfacecolor='#F0ECF8', markeredgecolor='black', linestyle='None')
                    ax.plot(resultado["h_float"], resultado["lim_der"], marker='o', markersize=8, markerfacecolor='#F0ECF8', markeredgecolor='black', linestyle='None')
                    if resultado["punto_exacto"] is not None:
                        ax.plot(resultado["h_float"], resultado["punto_exacto"], marker='o', markersize=8, color='#5C3D8F', linestyle='None')


            ax.plot([], [], ' ', label=f'Tipo: {resultado["tipo_limite"]}')


            y_validos = sorted([y for y in resultado["y_vals"] if not math.isnan(y)])
            if y_validos:
                idx_min = int(len(y_validos) * 0.05)
                idx_max = int(len(y_validos) * 0.95)
                y_piso = y_validos[idx_min]
                y_techo = y_validos[idx_max]
                margen = (y_techo - y_piso) * 0.5
                if margen == 0: margen = 10
                ax.set_ylim([y_piso - margen, y_techo + margen])


            ax.set_title("COMPORTAMIENTO DE LA FUNCIÓN", fontname="Courier New", fontweight="bold")
            ax.set_xlabel("Eje X", fontname="Courier New")
            ax.set_ylabel("Eje Y", fontname="Courier New")

            legend = ax.legend()
            legend.get_frame().set_edgecolor('black')
            legend.get_frame().set_linewidth(2)
            legend.get_frame().set_facecolor('white')

            ax.grid(True, color="#B8A9D4", linestyle=":", linewidth=1)
            canvas.draw()
        else:

            etiqueta_resultado.configure(text="> ERROR: Revisa la expresión.")
            textbox_pasos.configure(state="normal")
            textbox_pasos.delete("0.0", "end")
            textbox_pasos.insert("0.0", "No se pudo resolver el límite.\n\nRevisa la función o el valor de h.")
            textbox_pasos.configure(state="disabled")


    boton_calcular.configure(command=accion_calcular)
    boton_limpiar.configure(command=accion_limpiar)


    return frame