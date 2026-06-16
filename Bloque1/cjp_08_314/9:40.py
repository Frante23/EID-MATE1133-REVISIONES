import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt  
import math
import sympy as sp
import tkinter as tk  

PINK_PASTEL = "#FFC0CB"
PINK_SOFT = "#FFB6C1"
PINK_HOT = "#FF69B4"
DARK_BG = "#2A1E24"       
DARK_INNER = "#1F1419"    
WHITE_TEXT = "#FFF0F5"    

def np_is_nan(valor):
    try:
        return math.isnan(float(valor))
    except:
        return True

class App(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.title("Calculadora de Límites") 
        self.geometry("1240x760")
        self.minsize(1100, 680)

        ctk.set_appearance_mode("dark")
        self.configure(fg_color=DARK_BG)

        self.contenedor_principal = ctk.CTkFrame(self, fg_color=DARK_BG)
        self.contenedor_principal.pack(fill="both", expand=True, padx=25, pady=25)

        self.pantalla_inicio = ctk.CTkFrame(self.contenedor_principal, fg_color=DARK_BG)
        self.pantalla_inicio.pack(fill="both", expand=True)

        self.pantalla_calculadora = ctk.CTkFrame(self.contenedor_principal, fg_color=DARK_BG)

        self.crear_interfaz_inicio()

    def crear_interfaz_inicio(self):
        frame_central = ctk.CTkFrame(self.pantalla_inicio, fg_color=DARK_INNER, corner_radius=20, border_width=1, border_color=DARK_INNER)
        frame_central.pack(expand=True, padx=40, pady=40, ipadx=50, ipady=30)

        titulo = ctk.CTkLabel(
            frame_central,
            text="Calculadora de Límites\nAlgebraicos y Trigonométricos 🎀",
            font=("Georgia", 36, "italic", "bold"),
            text_color=PINK_PASTEL,
            justify="center"
        )
        titulo.pack(pady=(40, 20))
        
        descripcion = ctk.CTkLabel(
            frame_central,
            text="Resuelve indeterminaciones complejas con pasos detallados,\nvisualiza comportamientos gráficos y analiza aproximaciones numéricas.",
            font=("Segoe UI", 15),
            text_color=WHITE_TEXT,
            justify="center"
        )
        descripcion.pack(pady=20)

        boton_comenzar = ctk.CTkButton(
            frame_central,
            text="Comenzar a Calcular 🌟",
            font=("Segoe UI", 16, "bold"),
            hover_color=PINK_SOFT,
            fg_color=PINK_HOT,
            text_color="#FFFFFF",
            height=48,
            width=260,
            corner_radius=12,
            command=self.mostrar_calculadora
        )
        boton_comenzar.pack(pady=(20, 40))

    def mostrar_calculadora(self):
        self.pantalla_inicio.pack_forget()
        self.pantalla_calculadora.pack(fill="both", expand=True)
        self.crear_interfaz_calculadora()

    def crear_interfaz_calculadora(self):
        panel_izquierdo = ctk.CTkFrame(self.pantalla_calculadora, width=360, fg_color=DARK_INNER, corner_radius=15)
        panel_izquierdo.pack(side="left", fill="y", padx=(0, 15), pady=0)
        panel_izquierdo.pack_propagate(False)

        ctk.CTkLabel(panel_izquierdo, text="Entrada de Datos ✨", font=("Georgia", 22, "bold", "italic"), text_color=PINK_PASTEL).pack(pady=(25, 20))

        ctk.CTkLabel(panel_izquierdo, text="Función f(x):", font=("Segoe UI", 13, "bold"), text_color=WHITE_TEXT).pack(anchor="w", padx=30, pady=(10, 2))
        self.entrada_funcion = ctk.CTkEntry(panel_izquierdo, placeholder_text="Ej: sin(x)/x", width=300, height=40, border_color=PINK_SOFT, fg_color=DARK_BG, text_color=WHITE_TEXT, corner_radius=8)
        self.entrada_funcion.pack(padx=30, pady=5)

        ctk.CTkLabel(panel_izquierdo, text="X tiende a (c):", font=("Segoe UI", 13, "bold"), text_color=WHITE_TEXT).pack(anchor="w", padx=30, pady=(10, 2))
        self.entrada_c = ctk.CTkEntry(panel_izquierdo, placeholder_text="Ej: 0 o pi", width=300, height=40, border_color=PINK_SOFT, fg_color=DARK_BG, text_color=WHITE_TEXT, corner_radius=8)
        self.entrada_c.pack(padx=30, pady=5)

        ctk.CTkButton(
            panel_izquierdo,
            text="Calcular y Graficar 🌟",
            font=("Segoe UI", 14, "bold"),
            hover_color=PINK_SOFT,
            fg_color=PINK_HOT,
            text_color="#FFFFFF",
            height=42,
            width=300,
            corner_radius=10,
            command=self.calcular_y_graficar_limite
        ).pack(pady=25)

        self.resultado_limite = ctk.CTkTextbox(panel_izquierdo, width=300, fg_color=DARK_BG, text_color=WHITE_TEXT, border_color=PINK_SOFT, border_width=1, corner_radius=8)
        self.resultado_limite.pack(fill="both", expand=True, padx=30, pady=(0, 25))

        contenedor_derecho = ctk.CTkFrame(self.pantalla_calculadora, fg_color=DARK_INNER, corner_radius=15)
        contenedor_derecho.pack(side="right", fill="both", expand=True)

        grafico_canvas = tk.Canvas(contenedor_derecho, bg=DARK_INNER, highlightthickness=0)
        grafico_canvas.pack(side="left", fill="both", expand=True, padx=15, pady=15)

        scroll_y = ctk.CTkScrollbar(contenedor_derecho, orientation="vertical", command=grafico_canvas.yview, button_color=PINK_SOFT, button_hover_color=PINK_HOT)
        scroll_y.pack(side="right", fill="y", padx=(0, 10), pady=15)

        grafico_canvas.configure(yscrollcommand=scroll_y.set)

        self.grafico_interior = ctk.CTkFrame(grafico_canvas, width=1000, height=800, fg_color=DARK_INNER)
        grafico_canvas.create_window((0, 0), window=self.grafico_interior, anchor="nw")

        def al_configurar_interior(event):
            grafico_canvas.configure(scrollregion=grafico_canvas.bbox("all"))

        self.grafico_interior.bind("<Configure>", al_configurar_interior)

        self.fig_lim, self.ax_lim, self.canvas_lim = self.crear_canvas(self.grafico_interior)

    def intentar_factorizacion(self, expresion, x, valor_c):
        if valor_c == sp.oo or valor_c == -sp.oo:
            return expresion, ""
        try:
            numerador, denominador = sp.fraction(expresion)
            num_eval = numerador.subs(x, valor_c)
            den_eval = denominador.subs(x, valor_c)
            if num_eval == 0 and den_eval == 0:
                num_factorizado = sp.factor(numerador)
                den_factorizado = sp.factor(denominador)
                expresion_simplificada = sp.simplify(expresion)
                info_paso = (
                    f"¡Indeterminación [0/0] detectada! ✨\n\n"
                    f"a) Factorizando numerador:\n"
                    f"   {numerador}  =>  {num_factorizado}\n\n"
                    f"b) Factorizando denominador:\n"
                    f"   {denominador}  =>  {den_factorizado}\n\n"
                    f"c) Expresión con factores:\n"
                    f"   ({num_factorizado}) / ({den_factorizado})\n\n"
                    f"d) Cancelando términos comunes...\n"
                    f"   Nueva expresión: {expresion_simplificada}\n\n"
                )
                return expresion_simplificada, info_paso
        except:
            pass
        return expresion, ""

    def calcular_limite_numerico(self, expresion, x, c_float):
        h = 1e-7  
        try:
            val_izq = float(expresion.subs(x, c_float - h).evalf())
            val_der = float(expresion.subs(x, c_float + h).evalf())
            if abs(val_izq - val_der) < 1e-2:
                return (val_izq + val_der) / 2
            else:
                return "No existe (Límites laterales distintos)"
        except:
            return "Indefinido"

    def calcular_limite_infinito(self, expresion, x, tendencia):
        try:
            if tendencia == sp.oo:
                val1 = float(expresion.subs(x, 100000).evalf())
                val2 = float(expresion.subs(x, 1000000).evalf())
            else:
                val1 = float(expresion.subs(x, -100000).evalf())
                val2 = float(expresion.subs(x, -1000000).evalf())
            if abs(val1 - val2) < 1e-4:
                return val2
            elif val2 > val1 and val2 > 10000:
                return "oo"
            elif val2 < val1 and val2 < -10000:
                return "-oo"
            else:
                return "No converge"
        except:
            return "Indefinido"

    def calcular_y_graficar_limite(self):
        try:
            x = sp.Symbol('x')
            texto_funcion = self.entrada_funcion.get()
            texto_c = self.entrada_c.get().strip()
            traducciones = {
                "oo": sp.oo, "inf": sp.oo, "-oo": -sp.oo,
                "pi": sp.pi, "PI": sp.pi,
                "sen": sp.sin, "sin": sp.sin,
                "cos": sp.cos, "tan": sp.tan, "tg": sp.tan     
            }
            funcion_simbolica = sp.sympify(texto_funcion, locals=traducciones)
            valor_c = sp.sympify(texto_c, locals=traducciones)
            resultado = None
            txt_factorizacion = ""
            indeterminado_original = False
            evaluacion_directa = sp.nan
            pasos = f"Evaluando el límite 🎀:\n\nlim   ({texto_funcion})\nx→{valor_c}\n\n"
            if valor_c == sp.oo or valor_c == -sp.oo:
                pasos += "Paso 1: Analizar el comportamiento al infinito numéricamente. ✨\n"
                resultado = self.calcular_limite_infinito(funcion_simbolica, x, valor_c)
            else:
                pasos += "Paso 1: Intentar sustitución directa. ✨\n"
                try:
                    evaluacion_directa = funcion_simbolica.subs(x, valor_c)
                    if evaluacion_directa == sp.nan or evaluacion_directa.has(sp.AccumBounds) or not evaluacion_directa.is_real:
                        indeterminado_original = True
                except (ZeroDivisionError, ValueError):
                    indeterminado_original = True
                if not indeterminado_original and evaluacion_directa != sp.nan:
                    resultado = evaluacion_directa
                    pasos += f"Resultado directo = {evaluacion_directa}\n\n"
                else:
                    pasos += f"Resultado directo = No definido (Indeterminación o discontinuidad). 🔍\n\n"
                    funcion_trabajo, txt_factorizacion = self.intentar_factorizacion(funcion_simbolica, x, valor_c)
                    if txt_factorizacion != "":
                        pasos += f"Paso 2: Desarrollar procesos algebraicos. ✨\n\n{txt_factorizacion}"
                        pasos += f"Paso 3: Evaluar la nueva expresión simplificada en x = {valor_c}:\n"
                        resultado = funcion_trabajo.subs(x, valor_c)
                        pasos += f"Resultado = {resultado}\n\n"
                    else:
                        pasos += f"Paso 2: Resolver numéricamente mediante aproximación lateral (Tabulación). ✨\n"
                        resultado = self.calcular_limite_numerico(funcion_simbolica, x, float(valor_c.evalf()))
                        pasos += f"Resultado por aproximación h→0 = {resultado}\n\n"
            if isinstance(resultado, float):
                resultado = round(resultado, 5)
            elif resultado is not None and not isinstance(resultado, str):
                resultado = resultado.evalf()
                if resultado.is_real:
                    resultado = round(float(resultado), 5)
            self.ax_lim.clear()
            x_vals, y_vals = [], []
            if valor_c == sp.oo:
                inicio, fin, paso = 1, 50, 0.2
            elif valor_c == -sp.oo:
                inicio, fin, paso = -50, -1, 0.2
            else:
                c_float = float(valor_c.evalf())
                inicio, fin, paso = c_float - 5, c_float + 5, 0.02
            actual = inicio
            while actual <= fin:
                if valor_c.is_real and abs(actual - float(valor_c.evalf())) < 0.01:
                    actual += paso
                    continue
                try:
                    y_res = funcion_simbolica.subs(x, actual)
                    if y_res.is_real and not y_res.has(sp.I):
                        x_vals.append(actual)
                        y_vals.append(float(y_res))
                except:
                    pass
                actual += paso
            self.ax_lim.plot(x_vals, y_vals, label=f"f(x) = {texto_funcion}", color=PINK_HOT, linewidth=3)
            if resultado is not None and not np_is_nan(resultado) and valor_c.is_real:
                c_f = float(valor_c.evalf())
                r_f = float(resultado)
                if indeterminado_original:
                    self.ax_lim.scatter([c_f], [r_f], facecolors=DARK_INNER, edgecolors=PINK_PASTEL, s=140, zorder=6, linewidth=2.5, label="Discontinuidad Evitable")
                else:
                    self.ax_lim.scatter([c_f], [r_f], color=PINK_PASTEL, s=120, zorder=6, label="Límite")
            if y_vals:
                if resultado is not None and not np_is_nan(resultado):
                    r_f = float(resultado)
                    self.ax_lim.set_ylim(r_f - 3, r_f + 3)
                else:
                    min_y, max_y = min(y_vals), max(y_vals)
                    self.ax_lim.set_ylim(max(min_y, -10), min(max_y, 10))
            self.ax_lim.axhline(0, color=PINK_SOFT, linewidth=1.2, alpha=0.4)
            self.ax_lim.axvline(0, color=PINK_SOFT, linewidth=1.2, alpha=0.4)
            self.ax_lim.grid(True, linestyle="--", color="#403038", alpha=0.6)
            self.ax_lim.set_title(f"Gráfica en torno a x = {valor_c} ✧", fontsize=12, pad=10, color=PINK_PASTEL, fontname="Georgia")
            self.ax_lim.legend(facecolor=DARK_INNER, edgecolor='none', labelcolor=WHITE_TEXT)
            self.canvas_lim.draw()
            pasos += f"---------------------------------\n✨ RESULTADO FINAL: {resultado} ✨\n---------------------------------\n"
            self.mostrar_texto(self.resultado_limite, pasos)
        except Exception as e:
            self.mostrar_texto(self.resultado_limite, f"Ups! Hubo un error en los datos. 💕\nDetalle: {e}")

    def crear_canvas(self, frame):
        figura = Figure(figsize=(8, 6), dpi=100)
        eje = figura.add_subplot(111)
        figura.patch.set_facecolor(DARK_INNER)
        eje.set_facecolor(DARK_BG)
        eje.spines['bottom'].set_color(PINK_SOFT)
        eje.spines['top'].set_color(PINK_SOFT)
        eje.spines['left'].set_color(PINK_SOFT)
        eje.spines['right'].set_color(PINK_SOFT)
        eje.tick_params(colors=WHITE_TEXT)
        eje.xaxis.label.set_color(PINK_PASTEL)
        eje.yaxis.label.set_color(PINK_PASTEL)
        canvas = FigureCanvasTkAgg(figura, master=frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        return figura, eje, canvas

    def mostrar_texto(self, caja, texto):
        caja.configure(state="normal")
        caja.delete("1.0", "end")
        caja.insert("1.0", texto)
        caja.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()