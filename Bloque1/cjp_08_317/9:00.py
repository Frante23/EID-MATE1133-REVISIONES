import customtkinter as ctk  
import matplotlib.pyplot as plt  
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg  
import sympy as sp  

x = sp.Symbol("x")
canvas_actual = None

def calcular_todo():
    global canvas_actual

    texto_funcion = entrada_funcion.get()
    texto_h = entrada_h.get()

    try:
        expresion = sp.sympify(texto_funcion)

        if texto_h.strip().lower() in ["oo", "inf", "infinito", "+inf"]:
            valor_h = sp.oo
        elif texto_h.strip().lower() in ["-oo", "-inf", "-infinito"]:
            valor_h = -sp.oo
        else:
            valor_h = sp.sympify(texto_h)

        numerador, denominador = sp.fraction(expresion)
        paso_a_paso = "--- DESARROLLO LÓGICO ALGORÍTMICO PASO A PASO ---\n\n"

        if valor_h == sp.oo or valor_h == -sp.oo:
            paso_a_paso += f"Paso 1: Analizando comportamiento asintótico en el infinito ({valor_h}).\n"
            grado_num = sp.degree(numerador, gen=x)
            grado_den = sp.degree(denominador, gen=x)
            
            paso_a_paso += f"        Grado máx numerador: {grado_num} | Grado máx denominador: {grado_den}\n"
            
            if grado_num > grado_den:
                limite_calculado = sp.oo if valor_h == sp.oo else -sp.oo
                paso_a_paso += "        Como el grado del numerador es MAYOR, el límite tiende al infinito.\n"
            elif grado_num < grado_den:
                limite_calculado = 0
                paso_a_paso += "        Como el grado del denominador es MAYOR, el límite es 0.\n"
            else:
                coef_num = numerador.leading_coefficient(x)
                coef_den = denominador.leading_coefficient(x)
                limite_calculado = coef_num / coef_den
                paso_a_paso += f"        Grados iguales. Dividiendo coeficientes principales: {coef_num} / {coef_den}\n"
        
        else:
            paso_a_paso += f"Paso 1: Evaluando por sustitución directa x = {valor_h}:\n"
            eval_num = numerador.subs(x, valor_h)
            eval_den = denominador.subs(x, valor_h)
            
            paso_a_paso += f"        Sustitución Numerador: {eval_num}\n"
            paso_a_paso += f"        Sustitución Denominador: {eval_den}\n\n"

            if eval_num == 0 and eval_den == 0:
                paso_a_paso += "Paso 2: [ALERTA] Se detectó una Indeterminación del tipo [0/0].\n"
                paso_a_paso += "        Aplicando algoritmo de ruptura algebraico (Factorización manual):\n"
                
                expresion_factorizada = sp.factor(expresion)
                paso_a_paso += f"        Expresión reestructurada y simplificada: {expresion_factorizada}\n"
                
                limite_calculado = expresion_factorizada.subs(x, valor_h)
            else:
                paso_a_paso += "Paso 2: No se detecta indeterminación directa.\n"
                if eval_den == 0 and eval_num != 0:
                    limite_calculado = sp.limit(expresion, x, valor_h)
                    paso_a_paso += "        División por cero con numerador distinto de cero (Tendencia infinita).\n"
                else:
                    limite_calculado = eval_num / eval_den

        paso_a_paso += f"\nPaso 3: Resultado final de la equivalencia lógica:\n"
        paso_a_paso += f"        Resultado Analítico Seguro = {limite_calculado}"

        etiqueta_resultado.configure(text=f"Resultado: {limite_calculado}", text_color="#880E4F")
        
        caja_pasos.configure(state="normal")
        caja_pasos.delete("1.0", ctk.END)
        caja_pasos.insert("1.0", paso_a_paso)
        caja_pasos.configure(state="disabled")

        if canvas_actual is not None:
            canvas_actual.get_tk_widget().destroy()

        plt.clf()
        plt.gcf().patch.set_facecolor("#FFF0F5")
        ax = plt.gca()
        ax.set_facecolor("#FFFFFF")

        centro = 0.0 if (valor_h == sp.oo or valor_h == -sp.oo) else float(valor_h)

        puntos_x = [centro - 5 + (i * 10 / 200) for i in range(201)]
        puntos_y = []

        for px in puntos_x:
            try:
                if abs(px - centro) < 1e-5 and (valor_h != sp.oo and valor_h != -sp.oo):
                    puntos_y.append(None)
                    continue
                
                valor_y = expresion.subs(x, px)
                val_float = float(sp.re(valor_y))
                if abs(val_float) > 100:
                    puntos_y.append(None)
                else:
                    puntos_y.append(val_float)
            except:
                puntos_y.append(None)

        plt.plot(puntos_x, puntos_y, label=f"f(x) = {texto_funcion}", color="#FF69B4", lw=2.5)

        if valor_h != sp.oo and valor_h != -sp.oo:
            plt.axvline(x=centro, color="#D81B60", linestyle="--", alpha=0.7, label=f"x = {centro}")
            try:
                plt.axhline(y=float(sp.re(limite_calculado)), color="#4A148C", linestyle=":", alpha=0.5)
            except:
                pass
        else:
            try:
                plt.axhline(y=float(sp.re(limite_calculado)), color="#D81B60", linestyle=":", alpha=0.7, label=f"Asíntota y = {limite_calculado}")
            except:
                pass

        plt.title("Visualización del Comportamiento de la Curva", color="#880E4F", fontsize=12, fontweight='bold')
        plt.grid(True, color="#FFC0CB", linestyle=":")
        plt.legend()

        canvas_actual = FigureCanvasTkAgg(plt.gcf(), master=app)
        canvas_actual.draw()
        canvas_actual.get_tk_widget().pack(pady=15)

    except Exception as error:
        etiqueta_resultado.configure(text=f"Error en Expresión: {error}", text_color="#FF0000")

ctk.set_appearance_mode("light")
app = ctk.CTk()
app.title("Analizador de Límites - UCT")
app.geometry("850x850")
app.configure(fg_color="#FFF0F5")

titulo = ctk.CTkLabel(app, text="🍓 Calculadora Analítica de Límites 🍓", font=("Arial", 20, "bold"), text_color="#880E4F")
titulo.pack(pady=12)

label_funcion = ctk.CTkLabel(app, text="Ingresa la función f(x):", font=("Arial", 12, "bold"), text_color="#880E4F")
label_funcion.pack(pady=2)

entrada_funcion = ctk.CTkEntry(app, placeholder_text="Ejemplo: (x**2 - 1) / (x - 1)", width=320, fg_color="#FFFFFF", border_color="#FFB6C1", text_color="#000000")
entrada_funcion.pack(pady=5)

label_h = ctk.CTkLabel(app, text="¿A qué valor tiende x (valor h)?:", font=("Arial", 12, "bold"), text_color="#880E4F")
label_h.pack(pady=2)

entrada_h = ctk.CTkEntry(app, placeholder_text="Ejemplo: 1 u oo", width=320, fg_color="#FFFFFF", border_color="#FFB6C1", text_color="#000000")
entrada_h.pack(pady=5)

boton_calcular = ctk.CTkButton(app, text="🩰 Calcular Límite, Explicar y Graficar 🩰", command=calcular_todo, fg_color="#FF69B4", hover_color="#FF1493", text_color="#FFFFFF", font=("Arial", 12, "bold"))
boton_calcular.pack(pady=12)

etiqueta_resultado = ctk.CTkLabel(app, text="Resultado: Esperando datos...", font=("Arial", 14, "bold"), text_color="#880E4F")
etiqueta_resultado.pack(pady=5)

label_pasos = ctk.CTkLabel(app, text="✨ Memoria de Cálculo Teórico ✨", font=("Arial", 12, "bold"), text_color="#880E4F")
label_pasos.pack(pady=2)

caja_pasos = ctk.CTkTextbox(app, width=550, height=150, fg_color="#FFFFFF", border_color="#FFB6C1", border_width=2, text_color="#880E4F", font=("Courier New", 12))
caja_pasos.insert("1.0", "Los pasos del desarrollo matemático aparecerán aquí al calcular...")
caja_pasos.configure(state="disabled")
caja_pasos.pack(pady=5)

app.mainloop()