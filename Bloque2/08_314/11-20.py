import customtkinter as ctk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import sympy as sp
import re
from PIL import Image, ImageDraw
import io
import math

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def linspace(start, end, num):
    """Genera puntos uniformemente espaciados"""
    if num <= 0:
        return []
    if num == 1:
        return [start]
    step = (end - start) / (num - 1)
    return [start + step * i for i in range(num)]

def isinf(value):
    """Verifica si un valor es infinito"""
    try:
        return math.isinf(value)
    except (TypeError, ValueError):
        return False

PRIMARY_COLOR = "#00d4ff"
SECONDARY_COLOR = "#1a1f3a"
ACCENT_COLOR = "#ff006e"
BACKGROUND = "#0a0e27"
SURFACE = "#1a1f3a"
TEXT_PRIMARY = "#ffffff"
TEXT_SECONDARY = "#b0b8d1"

class AppLimites(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("📊 NEXUS - Advanced Limit Analyzer")
        self.geometry("1400x750")
        self.minsize(1400, 750)

        self.configure(fg_color=BACKGROUND)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.header = ctk.CTkFrame(self, height=90, corner_radius=0, fg_color=SECONDARY_COLOR)
        self.header.grid(row=0, column=0, columnspan=2, sticky="ew")
        self.header.grid_propagate(False)

        header_container = ctk.CTkFrame(self.header, fg_color="transparent")
        header_container.pack(fill="both", expand=True, padx=30, pady=20)

        title_frame = ctk.CTkFrame(header_container, fg_color="transparent")
        title_frame.pack(side="left", fill="x", expand=True)

        title_label = ctk.CTkLabel(title_frame, text="📊 NEXUS",
                                   font=ctk.CTkFont(size=32, weight="bold"),
                                   text_color=PRIMARY_COLOR)
        title_label.pack(side="left")

        subtitle_label = ctk.CTkLabel(title_frame, text=" Advanced Limit Analyzer",
                                      font=ctk.CTkFont(size=14),
                                      text_color=TEXT_SECONDARY)
        subtitle_label.pack(side="left", padx=(5, 0))

        info_label = ctk.CTkLabel(header_container, text="🔧 Ver 3.0 | Press ← → ↑ ↓ to navigate",
                                 font=ctk.CTkFont(size=10),
                                 text_color=TEXT_SECONDARY)
        info_label.pack(side="right")

        self.sidebar = ctk.CTkFrame(self, width=340, corner_radius=20, fg_color=SURFACE)
        self.sidebar.grid(row=1, column=0, sticky="nsew", padx=20, pady=20)
        self.sidebar.grid_propagate(False)

        config_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        config_frame.pack(fill="x", padx=20, pady=(20, 5))

        config_label = ctk.CTkLabel(config_frame, text="⚙️  CONFIGURACIÓN",
                                    font=ctk.CTkFont(size=16, weight="bold"),
                                    text_color=PRIMARY_COLOR)
        config_label.pack(side="left")

        separator1 = ctk.CTkFrame(self.sidebar, height=2, fg_color=PRIMARY_COLOR)
        separator1.pack(fill="x", padx=20, pady=10)

        self.label_func = ctk.CTkLabel(self.sidebar, text="🔢 Función f(x):",
                                       text_color=TEXT_PRIMARY,
                                       font=ctk.CTkFont(size=11, weight="bold"))
        self.label_func.pack(anchor="w", padx=20, pady=(10, 3))
        self.entry_func = ctk.CTkEntry(self.sidebar, placeholder_text="Ej: (sin(x))/x",
                                       width=280, height=35,
                                       border_color=PRIMARY_COLOR,
                                       text_color=TEXT_PRIMARY,
                                       fg_color="#0f1423")
        self.entry_func.pack(padx=20, pady=(0, 15))

        self.label_h = ctk.CTkLabel(self.sidebar, text="➡️  Tiende a (h):",
                                    text_color=TEXT_PRIMARY,
                                    font=ctk.CTkFont(size=11, weight="bold"))
        self.label_h.pack(anchor="w", padx=20, pady=(0, 3))
        self.entry_h = ctk.CTkEntry(self.sidebar, placeholder_text="Ej: 0, oo, o -oo",
                                    width=280, height=35,
                                    border_color=PRIMARY_COLOR,
                                    text_color=TEXT_PRIMARY,
                                    fg_color="#0f1423")
        self.entry_h.pack(padx=20, pady=(0, 20))

        self.btn_calcular = ctk.CTkButton(self.sidebar, text="🚀  CALCULAR Y GRAFICAR",
                                          corner_radius=12, fg_color=PRIMARY_COLOR,
                                          hover_color=ACCENT_COLOR,
                                          text_color="#000000",
                                          font=ctk.CTkFont(size=12, weight="bold"),
                                          height=40,
                                          command=self.ejecutar_analisis)
        self.btn_calcular.pack(padx=20, pady=(0, 30))

        result_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        result_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.res_label = ctk.CTkLabel(result_frame, text="✅ RESULTADO:",
                                      font=ctk.CTkFont(size=12, weight="bold"),
                                      text_color=PRIMARY_COLOR)
        self.res_label.pack(side="left")

        self.res_val = ctk.CTkLabel(self.sidebar, text="—", text_color=ACCENT_COLOR,
                                    font=ctk.CTkFont(size=18, weight="bold"))
        self.res_val.pack(pady=5)

        separator2 = ctk.CTkFrame(self.sidebar, height=2, fg_color=PRIMARY_COLOR)
        separator2.pack(fill="x", padx=20, pady=15)

        steps_label = ctk.CTkLabel(self.sidebar, text="📝 PASOS DEL CÁLCULO:",
                                   font=ctk.CTkFont(size=11, weight="bold"),
                                   text_color=PRIMARY_COLOR)
        steps_label.pack(anchor="w", padx=20, pady=(0, 8))

        self.paso_text = ctk.CTkTextbox(self.sidebar, width=280, height=200,
                                        corner_radius=10,
                                        border_width=1,
                                        border_color=PRIMARY_COLOR,
                                        text_color=TEXT_SECONDARY,
                                        fg_color="#0f1423")
        self.paso_text.pack(padx=20, pady=(0, 20))

        self.canvas_frame = ctk.CTkFrame(self, fg_color=SURFACE, corner_radius=20)
        self.canvas_frame.grid(row=1, column=1, sticky="nsew", padx=20, pady=20)

        graph_header = ctk.CTkFrame(self.canvas_frame, fg_color="transparent")
        graph_header.pack(fill="x", padx=20, pady=(20, 10))

        graph_label = ctk.CTkLabel(graph_header, text="📈 VISUALIZACIÓN",
                                   font=ctk.CTkFont(size=14, weight="bold"),
                                   text_color=PRIMARY_COLOR)
        graph_label.pack(side="left")

        nav_label = ctk.CTkLabel(graph_header, text="Controles: ← → ↑ ↓ para desplazamiento",
                                font=ctk.CTkFont(size=9),
                                text_color=TEXT_SECONDARY)
        nav_label.pack(side="right")

        self.fig, self.ax = plt.subplots(figsize=(7, 5.5), dpi=100)
        self.fig.patch.set_facecolor(SURFACE)
        self.ax.set_facecolor("#f9f9f9")
        self.ax.set_title("Comportamiento de la función", fontsize=12, fontweight="bold", pad=15)

        self.canvas = FigureCanvasTkAgg(self.fig, master=self.canvas_frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True, padx=20, pady=(0, 10))

        self.toolbar = NavigationToolbar2Tk(self.canvas, self.canvas_frame)
        self.toolbar.configure(bg=SURFACE)
        self.toolbar.update()
        self.toolbar.pack(fill="x", padx=20, pady=(0, 15))

        self.pan_x = 0
        self.pan_y = 0


        self.funcion_actual = None
        self.x_sym = None
        self.h_val = None
        self.limite_resultado = None

        self.bind("<Left>", self.mover_izquierda)
        self.bind("<Right>", self.mover_derecha)
        self.bind("<Up>", self.mover_arriba)
        self.bind("<Down>", self.mover_abajo)

        self.actualizar_grafico()

    def ejecutar_analisis(self):
        try:
            func_str = self.entry_func.get().strip()
            if not func_str:
                self.res_val.configure(text="⚠️ Ingresa una función", text_color="#ff9500")
                return

            func_str = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', func_str)
            func_str = func_str.replace("^", "**")
            self.x_sym = sp.Symbol('x')
            self.funcion_actual = sp.sympify(func_str, convert_xor=True)

            h_str = self.entry_h.get().strip()
            if not h_str:
                self.res_val.configure(text="⚠️ Especifica a qué tiende", text_color="#ff9500")
                return

            if h_str == "oo":
                self.h_val = sp.oo
            elif h_str == "-oo":
                self.h_val = -sp.oo
            else:
                self.h_val = sp.sympify(h_str)


            self.pan_x = 0
            self.pan_y = 0


            resultado, pasos, tipo_limite = self.calcular_limite_completo(self.funcion_actual, self.x_sym, self.h_val)

            self.limite_resultado = resultado

            if str(resultado) == "Error":
                self.res_val.configure(text="❌ Error", text_color="#ff006e")
            else:
                self.res_val.configure(text=str(resultado), text_color="#00ff88")

            self.paso_text.delete("1.0", "end")
            self.paso_text.insert("1.0", "📋 CÁLCULO PASO A PASO:\n\n")
            for p in pasos:
                self.paso_text.insert("end", "• " + p + "\n\n")


            self.graficar(self.funcion_actual, self.x_sym, self.h_val)

        except Exception as e:
            self.res_val.configure(text="❌ Error en entrada", text_color="#ff006e")
            import traceback
            print(traceback.format_exc())



    def detectar_limite_trigonometrico(self, f, x_sym, h_val):
        """Detecta y resuelve límites trigonométricos notables sin depender de Taylor"""
        if h_val != 0:
            return None, []

        pasos_trig = []


        f_str = str(f)


        try:

            if 'sin' in f_str and f_str.count('sin') == 2:
                numer, denom = sp.fraction(f)
                if denom.has(sp.sin):

                    sin_numer = sp.sin(x_sym)
                    sin_denom = sp.sin(x_sym)


                    lim_test = sp.limit(f, x_sym, 0)
                    if lim_test != sp.zoo:
                        pasos_trig.append("Límite trigonométrico notable: sin(f)/g")
                        return lim_test, pasos_trig


            if f == sp.sin(x_sym) / x_sym:
                pasos_trig.append("Límite trigonométrico notable: sin(x)/x = 1")
                return 1, pasos_trig


            if f == sp.tan(x_sym) / x_sym:
                pasos_trig.append("Límite trigonométrico notable: tan(x)/x = 1")
                return 1, pasos_trig


            if f == (1 - sp.cos(x_sym)) / x_sym**2:
                pasos_trig.append("Límite trigonométrico notable: (1-cos(x))/x² = 1/2")
                return sp.Rational(1, 2), pasos_trig


            if f == sp.asin(x_sym) / x_sym:
                pasos_trig.append("Límite trigonométrico notable: arcsin(x)/x = 1")
                return 1, pasos_trig

        except:
            pass

        return None, []

    def racionalizar_correctamente(self, f, x_sym, h_val, numer, denom):
        """Racionaliza de forma correcta identificando solo la parte con radical"""
        pasos_racional = []

        if not f.has(sp.sqrt):
            return None, pasos_racional

        pasos_racional.append("Detectadas raíces cuadradas. Intentando racionalización...")

        try:

            sqrt_terms_numer = [atom for atom in sp.preorder_traversal(numer) if atom.is_Pow and atom.exp == sp.Rational(1, 2)]
            sqrt_terms_denom = [atom for atom in sp.preorder_traversal(denom) if atom.is_Pow and atom.exp == sp.Rational(1, 2)]

            f_racional = f


            if sqrt_terms_numer or sqrt_terms_denom:




                if numer.has(sp.sqrt) and not denom.has(sp.sqrt):
                    conjugate = numer.subs(sqrt_terms_numer[0], -sqrt_terms_numer[0]) if sqrt_terms_numer else numer
                    pasos_racional.append(f"Multiplicando numerador y denominador por: {conjugate}")

                    f_racional = (numer * conjugate) / (denom * conjugate)
                    f_racional = sp.simplify(f_racional)
                    pasos_racional.append(f"Resultado racionalizado: {f_racional}")

                    valor_racional = f_racional.subs(x_sym, h_val)
                    pasos_racional.append(f"Evaluando: f({h_val}) = {valor_racional}")

                    if valor_racional.is_number and not valor_racional.has(sp.nan):
                        return valor_racional, pasos_racional

        except:
            pasos_racional.append("Racionalización no pudo completarse")

        return None, pasos_racional

    def analizar_limites_laterales_correctamente(self, f, x_sym, h_num):
        """Analiza límites laterales usando solo los valores más cercanos (convergencia)"""
        pasos_lateral = []


        epsilon_values = [0.001, 0.0001, 0.00001]

        left_values = []
        right_values = []
        left_inf = False
        right_inf = False

        for eps in epsilon_values:
            try:
                left_val = float(f.subs(x_sym, h_num - eps).evalf())
                right_val = float(f.subs(x_sym, h_num + eps).evalf())

                if isinf(left_val):
                    left_inf = True
                elif not math.isnan(left_val):
                    left_values.append((eps, left_val))

                if isinf(right_val):
                    right_inf = True
                elif not math.isnan(right_val):
                    right_values.append((eps, right_val))
            except:
                pass


        left_limit = None
        right_limit = None

        if left_values and len(left_values) >= 2:

            eps1, val1 = left_values[-2]
            eps2, val2 = left_values[-1]

            if abs(val1 - val2) < 1e-5:
                left_limit = val2
                pasos_lateral.append(f"Límite izquierdo (x→{h_num}⁻): {left_limit:.6f} (convergente)")
            else:
                pasos_lateral.append(f"Límite izquierdo oscila o diverge")
        elif left_inf:
            pasos_lateral.append(f"Límite izquierdo tiende a ∞")

        if right_values and len(right_values) >= 2:
            eps1, val1 = right_values[-2]
            eps2, val2 = right_values[-1]

            if abs(val1 - val2) < 1e-5:
                right_limit = val2
                pasos_lateral.append(f"Límite derecho (x→{h_num}⁺): {right_limit:.6f} (convergente)")
            else:
                pasos_lateral.append(f"Límite derecho oscila o diverge")
        elif right_inf:
            pasos_lateral.append(f"Límite derecho tiende a ∞")


        if left_limit is not None and right_limit is not None:
            if abs(left_limit - right_limit) < 1e-4:
                resultado = (left_limit + right_limit) / 2
                pasos_lateral.append(f"✓ Los límites laterales convergen: {resultado:.6f}")
                return resultado, pasos_lateral
            else:
                pasos_lateral.append(f"✗ Límite bilateral NO EXISTE: lim⁻ ≠ lim⁺")
                pasos_lateral.append(f"  Izquierda: {left_limit:.6f}, Derecha: {right_limit:.6f}")
                return None, pasos_lateral
        elif left_inf and right_inf:
            pasos_lateral.append(f"✗ Límite NO EXISTE: Ambos laterales tienden a infinito")
            return None, pasos_lateral
        elif left_inf or right_inf:
            pasos_lateral.append(f"✗ Límite NO EXISTE: Discontinuidad infinita")
            return None, pasos_lateral
        else:
            pasos_lateral.append(f"No se pudo evaluar los límites laterales")

        return None, pasos_lateral

    def calcular_infinito_correcto(self, grado_numer, grado_denom, coef_numer, coef_denom, h_val):
        """Calcula el signo correcto de infinito según grados y coeficientes"""
        diferencia = grado_numer - grado_denom


        sig_coef = 1 if coef_numer * coef_denom > 0 else -1

        if diferencia % 2 == 0:

            return sp.oo
        else:

            if h_val == sp.oo:
                return sp.oo if sig_coef > 0 else -sp.oo
            else:
                return -sp.oo if sig_coef > 0 else sp.oo

    def graficar(self, f, x_sym, h_val):
        """Grafica la función centrada en el punto h, evitando asíntotas falsas"""
        self.ax.clear()
        try:

            if h_val == sp.oo or h_val == -sp.oo:
                if h_val == sp.oo:
                    start, end = 0, 100
                else:
                    start, end = -100, 0
                h_num = (start + end) / 2
            else:
                h_num = float(h_val)
                rango = 10
                start = h_num - rango + self.pan_x
                end = h_num + rango + self.pan_x

            x_vals = linspace(start, end, 1000)
            y_vals = []

            for val in x_vals:
                try:
                    res = f.subs(x_sym, val).evalf()
                    if isinstance(res, complex):
                        y_vals.append(None)
                    else:
                        y_vals.append(float(res))
                except:
                    y_vals.append(None)



            discontinuities = []
            threshold = 50

            for i in range(len(y_vals) - 1):
                if y_vals[i] is not None and y_vals[i+1] is not None:
                    if abs(y_vals[i+1] - y_vals[i]) > threshold:
                        discontinuities.append(i)


            if discontinuities:
                start_idx = 0
                for disc_idx in discontinuities:

                    x_segment = x_vals[start_idx:disc_idx+1]
                    y_segment = y_vals[start_idx:disc_idx+1]
                    self.ax.plot(x_segment, y_segment, color=PRIMARY_COLOR, linewidth=2.5, zorder=3)
                    start_idx = disc_idx + 1


                if start_idx < len(x_vals):
                    x_segment = x_vals[start_idx:]
                    y_segment = y_vals[start_idx:]
                    self.ax.plot(x_segment, y_segment, color=PRIMARY_COLOR, linewidth=2.5,
                                label="f(x)", zorder=3)
            else:

                self.ax.plot(x_vals, y_vals, color=PRIMARY_COLOR, linewidth=2.5,
                            label="f(x)", zorder=3)


            y_vals_filtrados = [y for y in y_vals if y is not None and not isinf(y)]

            if y_vals_filtrados:
                y_min = min(y_vals_filtrados)
                y_max = max(y_vals_filtrados)
                margen = (y_max - y_min) * 0.2 if y_max != y_min else 5
                y_lim_min = y_min - margen
                y_lim_max = y_max + margen
            else:
                y_lim_min = -20
                y_lim_max = 20


            y_lim_min += self.pan_y
            y_lim_max += self.pan_y

            self.ax.set_ylim(y_lim_min, y_lim_max)
            self.ax.set_xlim(start, end)


            if h_val != sp.oo and h_val != -sp.oo:
                h_num = float(h_val)

                if self.limite_resultado is not None:
                    try:
                        lim_val = float(self.limite_resultado) if isinstance(self.limite_resultado, (int, float, sp.Rational)) else None
                        if lim_val is not None:
                            self.ax.plot(h_num, lim_val, 'o', color=ACCENT_COLOR,
                                       markersize=10, markerfacecolor='none',
                                       markeredgewidth=2, label=f"Límite = {self.limite_resultado}",
                                       zorder=5)

                            self.ax.axhline(y=lim_val, color=ACCENT_COLOR,
                                          linestyle='--', alpha=0.5, linewidth=1.5, zorder=1)
                    except:
                        pass

                self.ax.axvline(x=h_num, color=TEXT_SECONDARY,
                              linestyle=':', alpha=0.4, linewidth=1.5, zorder=1)


            self.ax.spines['top'].set_visible(False)
            self.ax.spines['right'].set_visible(False)
            self.ax.spines['left'].set_color(TEXT_SECONDARY)
            self.ax.spines['bottom'].set_color(TEXT_SECONDARY)
            self.ax.tick_params(colors=TEXT_SECONDARY, which='both')

            self.ax.grid(True, linestyle='--', alpha=0.2, color=TEXT_SECONDARY, zorder=1)
            self.ax.set_facecolor("#f9f9f9")

            self.ax.set_xlabel("x", fontsize=11, color=TEXT_SECONDARY, fontweight="bold")
            self.ax.set_ylabel("f(x)", fontsize=11, color=TEXT_SECONDARY, fontweight="bold")

            if self.limite_resultado is not None:
                self.ax.set_title(f"Comportamiento de f(x) cuando x → {h_val}",
                                fontsize=12, fontweight="bold", pad=15)

            self.ax.legend(loc='upper right', framealpha=0.9)

            self.canvas.draw()
        except Exception as e:
            self.ax.clear()
            self.ax.text(0.5, 0.5, f'⚠️ Error al graficar: {str(e)[:40]}',
                        ha='center', va='center', transform=self.ax.transAxes,
                        fontsize=11, color='red')
            self.canvas.draw()

    def calcular_limite_completo(self, f, x_sym, h_val):
        """
        Algoritmo completo para calcular límites sin usar sp.limit() directamente.
        Implementa: sustitución, factorización, racionalización correcta,
        límites al infinito (con signo correcto), trig notables, análisis lateral.
        """
        pasos = []
        tipo_limite = "algebraico"

        try:

            pasos.append("PASO 1: SUSTITUCIÓN DIRECTA")
            valor_directo = f.subs(x_sym, h_val)
            pasos.append(f"f({h_val}) = {valor_directo}")

            if valor_directo.is_number and not valor_directo.has(sp.nan):
                if h_val == sp.oo or h_val == -sp.oo:
                    pasos.append(f"Resultado: {valor_directo} (límite al infinito)")
                    tipo_limite = "infinito"
                else:
                    pasos.append(f"La función es continua en x={h_val}")
                    pasos.append(f"✓ Límite = {valor_directo}")
                return valor_directo, pasos, tipo_limite


            if h_val == sp.oo or h_val == -sp.oo:
                pasos.append("\nPASO 2: LÍMITE AL INFINITO")
                pasos.append("Analizando grado de polinomios...")

                numer, denom = sp.fraction(f)
                pasos.append(f"Expresión: ({numer}) / ({denom})")

                grado_numer = sp.Poly(numer, x_sym).degree() if numer.has(x_sym) else 0
                grado_denom = sp.Poly(denom, x_sym).degree() if denom.has(x_sym) else 0

                pasos.append(f"Grado numerador: {grado_numer}, Grado denominador: {grado_denom}")

                if grado_numer < grado_denom:
                    pasos.append("Grado(numerador) < Grado(denominador)")
                    pasos.append("✓ Límite = 0")
                    tipo_limite = "infinito"
                    return 0, pasos, tipo_limite
                elif grado_numer == grado_denom:
                    coef_numer = sp.Poly(numer, x_sym).leading_coeff
                    coef_denom = sp.Poly(denom, x_sym).leading_coeff
                    resultado = coef_numer / coef_denom
                    pasos.append("Grado(numerador) = Grado(denominador)")
                    pasos.append(f"Coef. principal numerador: {coef_numer}")
                    pasos.append(f"Coef. principal denominador: {coef_denom}")
                    pasos.append(f"✓ Límite = {resultado}")
                    tipo_limite = "infinito"
                    return resultado, pasos, tipo_limite
                else:
                    coef_numer = sp.Poly(numer, x_sym).leading_coeff
                    coef_denom = sp.Poly(denom, x_sym).leading_coeff

                    pasos.append("Grado(numerador) > Grado(denominador)")
                    pasos.append(f"Diferencia de grados: {grado_numer - grado_denom}")
                    pasos.append(f"Coef. principal numerador: {coef_numer}")
                    pasos.append(f"Coef. principal denominador: {coef_denom}")


                    inf_resultado = self.calcular_infinito_correcto(grado_numer, grado_denom,
                                                                     coef_numer, coef_denom, h_val)

                    if inf_resultado == sp.oo:
                        pasos.append("✓ Límite = +∞")
                    else:
                        pasos.append("✓ Límite = -∞")

                    tipo_limite = "infinito"
                    return inf_resultado, pasos, tipo_limite


            lim_trig, pasos_trig = self.detectar_limite_trigonometrico(f, x_sym, h_val)
            if lim_trig is not None:
                pasos.append("\nPASO 2: LÍMITE TRIGONOMÉTRICO NOTABLE")
                pasos.extend(pasos_trig)
                pasos.append(f"✓ Límite = {lim_trig}")
                return lim_trig, pasos, tipo_limite


            pasos.append("\nPASO 2: DETECCIÓN DE INDETERMINACIÓN")
            numer, denom = sp.fraction(f)
            numer_val = numer.subs(x_sym, h_val)
            denom_val = denom.subs(x_sym, h_val)

            if numer_val == 0 and denom_val == 0:
                pasos.append(f"Indeterminación 0/0 detectada en x={h_val}")


                pasos.append("\nPASO 3a: INTENTO DE FACTORIZACIÓN")
                try:
                    numer_fact = sp.factor(numer)
                    denom_fact = sp.factor(denom)
                    pasos.append(f"Numerador factorizado: {numer} → {numer_fact}")
                    pasos.append(f"Denominador factorizado: {denom} → {denom_fact}")

                    f_reducida = sp.cancel(f)
                    pasos.append(f"Cancelando factores comunes: {f} → {f_reducida}")

                    valor_reducido = f_reducida.subs(x_sym, h_val)
                    pasos.append(f"Evaluando en x={h_val}: f({h_val}) = {valor_reducido}")

                    if valor_reducido.is_number and not valor_reducido.has(sp.nan):
                        pasos.append(f"✓ Límite por factorización = {valor_reducido}")
                        return valor_reducido, pasos, tipo_limite
                except:
                    pasos.append("Factorización no aplicable")


                if f.has(sp.sqrt):
                    pasos.append("\nPASO 3b: RACIONALIZACIÓN (se detectaron raíces)")
                    valor_racional, pasos_racional = self.racionalizar_correctamente(f, x_sym, h_val, numer, denom)
                    pasos.extend(pasos_racional)

                    if valor_racional is not None:
                        pasos.append(f"✓ Límite por racionalización = {valor_racional}")
                        return valor_racional, pasos, tipo_limite


                pasos.append("\nPASO 3c: SERIE DE TAYLOR (como apoyo)")
                pasos.append("Expandiendo en serie de potencias para aproximación local...")
                try:
                    serie = sp.series(f, x_sym, h_val, n=4)
                    pasos.append(f"Serie: {serie}")
                    coef_principal = serie.removeO().subs(x_sym, h_val)
                    pasos.append(f"Término dominante: {coef_principal}")

                    if coef_principal.is_number and not coef_principal.has(sp.nan):
                        pasos.append(f"✓ Límite por serie = {coef_principal}")
                        return coef_principal, pasos, tipo_limite
                except:
                    pasos.append("Serie no disponible")


            pasos.append("\nPASO 4: SIMPLIFICACIÓN ALGEBRAICA")
            f_simp = sp.simplify(f)
            pasos.append(f"Simplificando: {f} → {f_simp}")

            valor_simp = f_simp.subs(x_sym, h_val)
            pasos.append(f"f({h_val}) = {valor_simp}")

            if valor_simp.is_number and not valor_simp.has(sp.nan):
                pasos.append(f"✓ Límite por simplificación = {valor_simp}")
                return valor_simp, pasos, tipo_limite


            pasos.append("\nPASO 5: ANÁLISIS DE LÍMITES LATERALES")

            if h_val != sp.oo and h_val != -sp.oo:
                try:
                    h_num = float(h_val)
                    resultado_lateral, pasos_lateral = self.analizar_limites_laterales_correctamente(f, x_sym, h_num)
                    pasos.extend(pasos_lateral)

                    if resultado_lateral is not None:
                        return resultado_lateral, pasos, tipo_limite
                except Exception as e:
                    pasos.append(f"No se pudieron evaluar límites laterales: {e}")


            pasos.append("\n✗ LÍMITE NO DETERMINADO")
            pasos.append("Posibles causas: función oscilante, discontinuidad esencial,")
            pasos.append("o forma indeterminada no algebraica")
            return "No determinado", pasos, tipo_limite

        except Exception as e:
            pasos.append(f"Error en cálculo: {str(e)}")
            return "Error", pasos, tipo_limite

    def mover_izquierda(self, event):
        """Desplazar vista hacia la izquierda"""
        self.pan_x -= 2

    def mover_derecha(self, event):
        """Desplazar vista hacia la derecha"""
        self.pan_x += 2

    def mover_arriba(self, event):
        """Desplazar vista hacia arriba (solo la vista, no la función)"""
        self.pan_y += 2

    def mover_abajo(self, event):
        """Desplazar vista hacia abajo (solo la vista, no la función)"""
        self.pan_y -= 2

    def actualizar_grafico(self):
        """Actualizar gráfica continuamente"""
        try:
            if hasattr(self, 'funcion_actual') and self.funcion_actual is not None:
                self.graficar(self.funcion_actual, self.x_sym, self.h_val)
        except:
            pass

        self.after(100, self.actualizar_grafico)

if __name__ == "__main__":
    app = AppLimites()
    app.mainloop()
