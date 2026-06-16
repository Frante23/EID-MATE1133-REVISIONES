import customtkinter as ctk
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

# ==========================================
# 1. FUNCIÓN PRINCIPAL DE CÁLCULO
# ==========================================
def calcular_limite():
    x = sp.Symbol('x')
    func_str = entry_funcion.get()
    c_str = entry_c.get()

    try:
        f = sp.sympify(func_str)
        c = sp.sympify(c_str)

        # --- CÁLCULO ANALÍTICO MATEMÁTICO ---
        limite_exacto = ""
        
        if c == sp.oo or c == -sp.oo:
            # Sección para límites al infinito
            try:
                num, den = sp.fraction(f)
                
                grado_den = sp.degree(den, gen=x)
                termino_divisor = x**grado_den
                
                # Usamos expand para asegurar la separación de términos (ej: 3 + 5/x)
                num_div = sp.expand(num / termino_divisor) 
                den_div = sp.expand(den / termino_divisor) 
                
                # Evaluación individual para evitar nan
                lim_num = num_div.subs(x, c)
                lim_den = den_div.subs(x, c)
                
                if lim_num.is_number and lim_den.is_number and not lim_den.is_zero:
                    limite_exacto = lim_num / lim_den
                else:
                    limite_exacto = "Indeterminado o Diverge (∞)"

            except Exception:
                evaluacion_directa = f.subs(x, c)
                if evaluacion_directa.has(sp.nan) or evaluacion_directa.has(sp.zoo):
                    limite_exacto = "Indeterminado o Diverge"
                else:
                    limite_exacto = evaluacion_directa
        
        else:
            evaluacion_directa = f.subs(x, c)
            
            if evaluacion_directa.has(sp.nan) or evaluacion_directa.has(sp.zoo):
                # Intentar simplificar algebraicamente (caso 0/0)
                f_simplificada = sp.cancel(f)
                limite_exacto = f_simplificada.subs(x, c)
                
                if limite_exacto.has(sp.nan) or limite_exacto.has(sp.zoo):
                    # Verificar si es asíntota vertical (zoo) o indeterminación (nan)
                    if limite_exacto.has(sp.zoo):
                         limite_exacto = "Diverge a ∞ (Asíntota)"
                    else:
                         limite_exacto = "No existe (Diverge)"
            else:
                limite_exacto = evaluacion_directa

        # --- CÁLCULO NUMÉRICO POR APROXIMACIÓN ---
        limite_aprox = ""
        if c == sp.oo:
            valor = f.subs(x, 1000000).evalf()
            limite_aprox = str(round(valor, 4))
        elif c == -sp.oo:
            valor = f.subs(x, -1000000).evalf()
            limite_aprox = str(round(valor, 4))
        else:
            epsilon = 1e-6
            limite_izq = f.subs(x, c - epsilon).evalf()
            limite_der = f.subs(x, c + epsilon).evalf()
            
            if abs(limite_izq - limite_der) < 1e-3:
                limite_promedio = (limite_izq + limite_der) / 2
                limite_aprox = str(round(limite_promedio, 4))
            else:
                limite_aprox = f"Diverge\nIzq: {round(limite_izq, 4)}\nDer: {round(limite_der, 4)}"

        resultado_txt.configure(state="normal")
        resultado_txt.delete("1.0", "end")
        resultado_txt.insert("1.0", f"Función: {f}\nLímite cuando x -> {c}\n\nLímite Exacto (Analítico):\n{limite_exacto}\n\nAproximación (Numérica):\n{limite_aprox}")
        resultado_txt.configure(state="disabled")

        # --- GRÁFICA ---
        ax.clear()
        
        if c == sp.oo: 
            inicio, fin = 1, 50
        elif c == -sp.oo: 
            inicio, fin = -50, -1
        else:
            c_val = float(c.evalf())
            inicio, fin = c_val - 5, c_val + 5

        num_puntos = 200
        paso = (fin - inicio) / (num_puntos - 1)
        x_vals = [inicio + i * paso for i in range(num_puntos)]

        f_numerica = sp.lambdify(x, f, modules=['math'])
        y_vals = []
        
        # Evaluar puntos cuidando no romper la gráfica en discontinuidades
        for val in x_vals:
            try:
                if c != sp.oo and c != -sp.oo and abs(val - c_val) < 0.001:
                    y_vals.append(float('nan'))
                    continue
                y = f_numerica(val)
                y_vals.append(y)
            except:
                y_vals.append(float('nan'))

        ax.plot(x_vals, y_vals, label=f"f(x)", color="cyan")
        
        # Marcadores visuales para límites finitos
        if c != sp.oo and c != -sp.oo:
            ax.axvline(x=c_val, color="gray", linestyle="--", alpha=0.4, label=f"x = {c}")
            
            try:
                lim_num = float(limite_exacto)
                eval_original = f.subs(x, c).evalf()
                
                # Graficar Punto Definido o Agujero según corresponda
                if eval_original.is_number and not eval_original.has(sp.nan):
                    ax.plot(c_val, lim_num, marker='o', markersize=8, color='red', label="Punto Definido")
                else:
                    ax.plot(c_val, lim_num, marker='o', markersize=8, markerfacecolor='black', markeredgecolor='red', markeredgewidth=2, label="Agujero (Límite)")
            except:
                pass 

        ax.legend()
        ax.grid(True, linestyle=":", alpha=0.4)
        canvas.draw()

    except Exception as e:
        # Capturar errores si el usuario ingresa una expresión inválida
        resultado_txt.configure(state="normal")
        resultado_txt.delete("1.0", "end")
        resultado_txt.insert("1.0", f"Error en la expresión matemática:\n{e}\n\nRecuerda usar * para multiplicar y ** para potencias.")
        resultado_txt.configure(state="disabled")

# ==========================================
# 2. CONFIGURACIÓN DE LA INTERFAZ GRÁFICA
# ==========================================
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk() 
app.geometry("900x600")
app.title("Analizador de Límites")

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(0, weight=1)

tabs = ctk.CTkTabview(app)
tabs.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")

tab_inicio = tabs.add("Inicio")
tab_calculadora = tabs.add("Calculadora de Límites")

# --- Pestaña de Inicio ---
titulo = ctk.CTkLabel(tab_inicio, text="Bienvenido al Analizador", font=("Arial", 30, "bold"))
titulo.pack(pady=25)

texto_intro = """Programa para calcular y representar límites matemáticos.

Características de este software:
- Interfaz gráfica con CustomTkinter usando pestañas.
- Gráficos integrados con Matplotlib.
- Cálculo de límites analítico por sustitución y factorización (sin sp.limit).
- Evaluación lateral numérica.
- Generación de coordenadas con Python puro (sin numpy)."""

caja = ctk.CTkTextbox(tab_inicio, width=600, height=200, font=("Arial", 14))
caja.pack(pady=20)
caja.insert("1.0", texto_intro)
caja.configure(state="disabled")

# --- Pestaña Calculadora ---
contenedor = ctk.CTkFrame(tab_calculadora) 
contenedor.pack(fill="both", expand=True, padx=10, pady=10)

panel = ctk.CTkFrame(contenedor, width=320)
panel.pack(side="left", fill="y", padx=10, pady=10)

grafico_frame = ctk.CTkFrame(contenedor)
grafico_frame.pack(side="right", fill="both", expand=True, padx=10, pady=10)

ctk.CTkLabel(panel, text="Cálculo de Límite", font=("Arial", 20, "bold")).pack(pady=15)

ctk.CTkLabel(panel, text="Función f(x):").pack()
entry_funcion = ctk.CTkEntry(panel, placeholder_text="Ej: (x**2-1)/(x-1)", width=250)
entry_funcion.pack(pady=5)

ctk.CTkLabel(panel, text="Valor al que tiende x (c):").pack()
entry_c = ctk.CTkEntry(panel, placeholder_text="Ej: 0, pi, oo", width=250)
entry_c.pack(pady=5)

ctk.CTkButton(panel, text="Calcular y Graficar", command=calcular_limite).pack(pady=20)

resultado_txt = ctk.CTkTextbox(panel, width=280, height=200)
resultado_txt.pack(pady=10)
resultado_txt.insert("1.0", "Ingresa los datos y presiona calcular.")
resultado_txt.configure(state="disabled")

# Configuración inicial del lienzo de Matplotlib
figura = Figure(figsize=(5, 4), dpi=100)
figura.patch.set_facecolor('#2b2b2b')
ax = figura.add_subplot(111)
ax.set_facecolor('#2b2b2b')
ax.tick_params(colors='white')

canvas = FigureCanvasTkAgg(figura, master=grafico_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

# ==========================================
# 3. PUNTO DE ARRANQUE
# ==========================================
if __name__ == "__main__":
    app.mainloop()