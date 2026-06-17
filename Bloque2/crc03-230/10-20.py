import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
import math


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class App(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("Analizador y Visualizador de Límites — MATE1133")
        self.geometry("1300x800")
        self.minsize(1050, 650)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.tab_inicio      = self.tabs.add("  Inicio  ")
        self.tab_calculadora = self.tabs.add("  Calculadora de Límites  ")
        self.tab_infinito    = self.tabs.add("  Límites al Infinito  ")
        self.tab_ejemplos    = self.tabs.add("  Ejemplos  ")

        self._construir_inicio()
        self._construir_calculadora()
        self._construir_infinito()
        self._construir_ejemplos()



    def _crear_canvas_matplotlib(self, frame):
        figura = Figure(figsize=(7, 5), dpi=100)
        figura.patch.set_facecolor("#1e1e2e")          
        eje = figura.add_subplot(111)
        eje.set_facecolor("#12121f")                    
        canvas = FigureCanvasTkAgg(figura, master=frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        return figura, eje, canvas

    def _mostrar_texto(self, caja: ctk.CTkTextbox, texto: str):
        caja.configure(state="normal")
        caja.delete("1.0", "end")
        caja.insert("1.0", texto)
        caja.configure(state="disabled")

    def _generar_x(self, inicio: float, fin: float, pasos: int = 600) -> list:
        if pasos <= 0:
            return [inicio]
        delta = (fin - inicio) / pasos
        return [inicio + i * delta for i in range(pasos + 1)]

    def _evaluar_funcion(self, expr, valores_x: list) -> tuple:
        x_sym = sp.Symbol('x')
        xs, ys = [], []
        for val in valores_x:
            try:
                resultado = expr.subs(x_sym, val)
                resultado_f = float(resultado)
                if math.isfinite(resultado_f):
                    xs.append(val)
                    ys.append(resultado_f)
                else:
                    xs.append(val)
                    ys.append(None)   
            except Exception:
                xs.append(val)
                ys.append(None)      
        return xs, ys

    def _aplicar_estilo_ejes(self, eje):
        eje.set_facecolor("#12121f")
        eje.tick_params(colors="white", labelsize=9)
        eje.set_xlabel("x", color="#aaaaaa", fontsize=11)
        eje.set_ylabel("f(x)", color="#aaaaaa", fontsize=11)
        eje.axhline(0, color="#444466", linewidth=0.8)
        eje.axvline(0, color="#444466", linewidth=0.8)
        eje.grid(True, alpha=0.2, color="#555577")
        for spine in eje.spines.values():
            spine.set_color('#444466')

    def _graficar_por_segmentos(self, eje, xs, ys, color, label="f(x)"):
        seg_x, seg_y = [], []
        primer_segmento = True
        for xi, yi in zip(xs, ys):
            if yi is not None:
                seg_x.append(xi)
                seg_y.append(yi)
            else:
                if seg_x:
                    lbl = label if primer_segmento else "_nolegend_"
                    eje.plot(seg_x, seg_y, color=color, linewidth=2.2, label=lbl)
                    primer_segmento = False
                    seg_x, seg_y = [], []
        if seg_x:
            lbl = label if primer_segmento else "_nolegend_"
            eje.plot(seg_x, seg_y, color=color, linewidth=2.2, label=lbl)

    def _ajustar_ylim(self, eje, ys, margen_ratio=0.15, limite_absoluto=80):
        finitos = [y for y in ys if y is not None]
        if not finitos:
            return
        y_min, y_max = min(finitos), max(finitos)
        margen = max((y_max - y_min) * margen_ratio, 0.5)
        eje.set_ylim(
            max(y_min - margen, -limite_absoluto),
            min(y_max + margen,  limite_absoluto)
        )



    def _calcular_limite(self, expr_str: str, h_val) -> tuple:
        x_sym = sp.Symbol('x')

        try:
            expr = sp.sympify(expr_str, locals={"x": x_sym})
        except Exception:
            return None, (
                "✗ Error de sintaxis en la función.\n\n"
                "Recuerda usar:\n"
                "  • x        como variable\n"
                "  • **       para potencias  (Ej: x**2)\n"
                "  • *        para multiplicar (Ej: 3*x)\n"
                "  • sin, cos, tan, exp, log, sqrt, Abs\n"
            )

        lineas = []
        def sep(char="─", largo=48):
            lineas.append(char * largo)

        sep("═")
        lineas.append("   RESOLUCIÓN ANALÍTICA DEL LÍMITE")
        sep("═")
        if h_val == sp.oo:
            lineas.append(f"  f(x) = {expr}")
            lineas.append(f"  Evaluando: lim f(x)  cuando  x → +∞\n")
        elif h_val == -sp.oo:
            lineas.append(f"  f(x) = {expr}")
            lineas.append(f"  Evaluando: lim f(x)  cuando  x → -∞\n")
        else:
            lineas.append(f"  f(x) = {expr}")
            lineas.append(f"  Evaluando: lim f(x)  cuando  x → {h_val}\n")

        resultado = None


        if h_val in (sp.oo, -sp.oo):
            signo    = 1 if h_val == sp.oo else -1
            simbolo  = "+∞" if h_val == sp.oo else "-∞"

            sep()
            lineas.append("  PASO 1 — Análisis Algebraico de la Forma")
            sep()
            try:
                num, den = sp.fraction(sp.cancel(expr))
                if den != 1:
                    gn = int(sp.degree(sp.expand(num), x_sym))
                    gd = int(sp.degree(sp.expand(den), x_sym))
                    cn = sp.LC(sp.expand(num), x_sym)
                    cd = sp.LC(sp.expand(den), x_sym)
                    lineas.append(f"  Función racional detectada.")
                    lineas.append(f"  Numerador:   grado {gn},  coef. líder = {cn}")
                    lineas.append(f"  Denominador: grado {gd},  coef. líder = {cd}\n")
                    if gn < gd:
                        lineas.append("  grado num < grado den  →  lim = 0")
                        resultado = sp.Integer(0)
                    elif gn == gd:
                        ratio = sp.Rational(cn, cd)
                        lineas.append(f"  grado num = grado den")
                        lineas.append(f"  lim = {cn} / {cd} = {ratio}")
                        resultado = ratio
                    else:
                        lineas.append("  grado num > grado den  →  lim = ±∞")
                else:
                    lineas.append("  No es una fracción racional simple.")
                    lineas.append("  Se procede con evaluación numérica.\n")
            except Exception:
                lineas.append("  Análisis algebraico no disponible para esta forma.\n")


            sep()
            lineas.append("  PASO 2 — Verificación Numérica")
            sep()
            lineas.append(f"  Evaluamos f(x) en valores grandes hacia {simbolo}:\n")

            potencias = [1e3, 1e5, 1e7, 1e9, 1e11]
            ultimos   = []
            for v in potencias:
                xv = signo * v
                try:
                    fv = float(expr.subs(x_sym, xv))
                    if math.isfinite(fv):
                        lineas.append(f"  f({xv:+.0e}) = {fv:.8f}")
                        ultimos.append(fv)
                    elif fv > 0:
                        lineas.append(f"  f({xv:+.0e}) = +∞")
                        ultimos.append(float('inf'))
                    else:
                        lineas.append(f"  f({xv:+.0e}) = -∞")
                        ultimos.append(float('-inf'))
                except Exception:
                    pass

            lineas.append("")
            if ultimos:
                ultimo = ultimos[-1]
                if math.isinf(ultimo):
                    resultado = sp.oo if ultimo > 0 else -sp.oo
                    lineas.append(f"  ✓ La secuencia diverge hacia {'+ ∞' if ultimo > 0 else '- ∞'}")
                elif resultado is None:
                    try:
                        resultado = sp.nsimplify(ultimo, rational=True, tolerance=1e-5)
                    except Exception:
                        resultado = round(ultimo, 6)
                    lineas.append(f"  ✓ La secuencia converge → lim ≈ {resultado}")


        else:
            h_float = float(h_val)

            sep()
            lineas.append("  PASO 1 — Sustitución Directa")
            sep()
            lineas.append(f"  Reemplazamos x = {h_val} directamente en f(x):\n")

            subs_exitosa = False
            try:
                subs_raw = expr.subs(x_sym, h_val)
                if subs_raw in (sp.nan, sp.zoo):
                    lineas.append(f"  f({h_val}) = {subs_raw}")
                    lineas.append("  → Forma indeterminada (0/0 ó ∞/∞).")
                    lineas.append("  → Se requiere simplificación algebraica.\n")
                else:
                    subs_f = float(sp.simplify(subs_raw))
                    if math.isnan(subs_f):
                        lineas.append(f"  f({h_val}) = 0/0  →  Forma indeterminada.\n")
                    elif math.isinf(subs_f):
                        lineas.append(f"  f({h_val}) = {'+ ∞' if subs_f > 0 else '- ∞'}")
                        lineas.append("  → La función diverge en este punto.\n")
                        resultado     = sp.oo if subs_f > 0 else -sp.oo
                        subs_exitosa  = True
                    else:
                        subs_val = sp.simplify(subs_raw)
                        lineas.append(f"  f({h_val}) = {subs_val}  ✓")
                        lineas.append("  → Sustitución directa exitosa.\n")
                        resultado    = subs_val
                        subs_exitosa = True
            except (ZeroDivisionError, Exception):
                lineas.append(f"  f({h_val}) → División por cero / indeterminado.\n")


            if not subs_exitosa:
                sep()
                lineas.append("  PASO 2 — Simplificación Algebraica")
                sep()
                lineas.append("  Intentamos eliminar la indeterminación:\n")

                intentos = [
                    ("sp.cancel()",   sp.cancel),
                    ("sp.factor()",   sp.factor),
                    ("sp.simplify()", sp.simplify),
                ]
                for nombre_fn, fn in intentos:
                    try:
                        expr_mod = fn(expr)
                        if str(expr_mod) == str(expr):
                            continue
                        lineas.append(f"  {nombre_fn}  →  {expr_mod}")
                        val_mod = expr_mod.subs(x_sym, h_val)
                        val_f   = float(sp.simplify(val_mod))
                        if math.isfinite(val_f) and not math.isnan(val_f):
                            resultado    = sp.simplify(val_mod)
                            subs_exitosa = True
                            lineas.append(f"  Sustituyendo x={h_val}: {resultado}  ✓\n")
                            break
                        else:
                            lineas.append(f"  Aún indeterminado con esta forma.\n")
                    except Exception:
                        pass

                if not subs_exitosa:
                    lineas.append("  No se resolvió algebraicamente.")
                    lineas.append("  → Se aplica análisis numérico lateral.\n")


            if not subs_exitosa or resultado is None:
                sep()
                lineas.append("  PASO 3 — Límites Laterales Numéricos")
                sep()
                lineas.append("  Evaluamos f(x) en valores muy próximos a h:\n")

                deltas    = [0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001]
                izq_vals  = []
                der_vals  = []

                lineas.append(f"  Por la IZQUIERDA (x → {h_val}⁻):")
                for d in deltas:
                    try:
                        fv = float(expr.subs(x_sym, h_float - d))
                        if math.isfinite(fv):
                            lineas.append(f"    f({h_float} - {d}) = {fv:.8f}")
                            izq_vals.append(fv)
                    except Exception:
                        pass

                lineas.append(f"\n  Por la DERECHA (x → {h_val}⁺):")
                for d in deltas:
                    try:
                        fv = float(expr.subs(x_sym, h_float + d))
                        if math.isfinite(fv):
                            lineas.append(f"    f({h_float} + {d}) = {fv:.8f}")
                            der_vals.append(fv)
                    except Exception:
                        pass

                lineas.append("")
                if izq_vals and der_vals:
                    li = izq_vals[-1]
                    ld = der_vals[-1]
                    lineas.append(f"  Límite izquierdo ≈ {li:.8f}")
                    lineas.append(f"  Límite derecho   ≈ {ld:.8f}\n")
                    if abs(li - ld) < 1e-5:
                        lim_num = (li + ld) / 2
                        lineas.append("  ✓ Ambos lados convergen al mismo valor.")
                        lineas.append(f"    → El límite EXISTE.\n")
                        try:
                            resultado = sp.nsimplify(lim_num, rational=True, tolerance=1e-5)
                        except Exception:
                            resultado = round(lim_num, 6)
                    else:
                        lineas.append("  ✗ Los límites laterales son distintos.")
                        lineas.append("    → El límite NO EXISTE (discontinuidad de salto).\n")
                        resultado = None
                else:
                    lineas.append("  No se pudieron obtener suficientes puntos.")


        sep("═")
        lineas.append("  RESULTADO FINAL")
        sep("═")

        if resultado is not None:
            flecha = ("+∞" if h_val == sp.oo else
                      "-∞" if h_val == -sp.oo else str(h_val))
            lineas.append(f"\n     lim   f(x)  =  {resultado}")
            lineas.append(f"    x→{flecha}\n")

            try:
                vd = float(resultado)
                if not math.isinf(vd):
                    lineas.append(f"  ≈  {vd:.8f}  (aproximación decimal)\n")
            except Exception:
                pass

            sep()
            lineas.append("  INTERPRETACIÓN")
            sep()
            if resultado == sp.oo:
                lineas.append("  La función crece sin límite (+∞).")
            elif resultado == -sp.oo:
                lineas.append("  La función decrece sin límite (-∞).")
            else:
                try:
                    vf = float(resultado)
                    if h_val not in (sp.oo, -sp.oo):
                        try:
                            fh = float(sp.simplify(expr.subs(x_sym, h_val)))
                            if abs(fh - vf) < 1e-9:
                                lineas.append(f"  f({h_val}) = {resultado}: función CONTINUA en x = {h_val}.")
                            else:
                                lineas.append(f"  DISCONTINUIDAD REMOVIBLE en x = {h_val}.")
                                lineas.append(f"  El límite existe pero f({h_val}) es distinto.")
                        except Exception:
                            lineas.append(f"  El límite converge al valor finito {resultado}.")
                    else:
                        lineas.append(f"  Asíntota horizontal en y = {resultado}.")
                except Exception:
                    lineas.append(f"  El límite es {resultado}.")
        else:
            lineas.append("\n     El límite  NO EXISTE.\n")

        return resultado, "\n".join(lineas)


    def _construir_inicio(self):
        frame = self.tab_inicio
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(2, weight=1)


        ctk.CTkLabel(
            frame,
            text="Analizador y Visualizador de Límites",
            font=("Arial", 30, "bold")
        ).grid(row=0, column=0, pady=(20, 4))

        ctk.CTkLabel(
            frame,
            text="MATE1133  —  Evaluación Integrada de Desempeño  |  Universidad Católica de Temuco",
            font=("Arial", 14),
            text_color="#8888aa"
        ).grid(row=1, column=0, pady=(0, 16))


        contenedor = ctk.CTkFrame(frame, fg_color="transparent")
        contenedor.grid(row=2, column=0, sticky="nsew", padx=30, pady=10)
        contenedor.grid_columnconfigure((0, 1), weight=1)
        contenedor.grid_rowconfigure(0, weight=1)


        tarjeta_izq = ctk.CTkFrame(contenedor, corner_radius=12)
        tarjeta_izq.grid(row=0, column=0, sticky="nsew", padx=(0, 8), pady=0)

        ctk.CTkLabel(tarjeta_izq, text="¿Qué hace esta app?",
                     font=("Arial", 17, "bold")).pack(pady=(20, 8), padx=20, anchor="w")

        descripcion = (
            "Esta herramienta calcula y visualiza límites de\n"
            "funciones matemáticas de forma analítica y gráfica.\n\n"
            "Combina SymPy (cálculo simbólico exacto) con\n"
            "Matplotlib (visualización) en una interfaz gráfica\n"
            "construida con CustomTkinter.\n\n"
            "El sistema detecta automáticamente:\n"
            "  • Sustitución directa exitosa\n"
            "  • Formas indeterminadas  (0/0, ∞/∞)\n"
            "  • Discontinuidades removibles\n"
            "  • Discontinuidades de salto\n"
            "  • Asíntotas horizontales\n"
            "  • Comportamiento en ±∞"
        )
        ctk.CTkLabel(tarjeta_izq, text=descripcion,
                     font=("Arial", 13), justify="left",
                     text_color="#cccccc").pack(padx=25, pady=(0, 20), anchor="w")


        tarjeta_der = ctk.CTkFrame(contenedor, corner_radius=12)
        tarjeta_der.grid(row=0, column=1, sticky="nsew", padx=(8, 0), pady=0)

        ctk.CTkLabel(tarjeta_der, text="Cómo ingresar funciones",
                     font=("Arial", 17, "bold")).pack(pady=(20, 8), padx=20, anchor="w")

        sintaxis = (
            "Usa  x  como variable y la siguiente sintaxis:\n\n"
            "  Potencia     →   x**2,  x**3\n"
            "  Multiplicar  →   3*x,   2*x**2\n"
            "  Fracción     →   (x**2 - 1) / (x - 1)\n"
            "  Raíz cuad.   →   sqrt(x + 3)\n"
            "  Seno/Coseno  →   sin(x),  cos(x),  tan(x)\n"
            "  Exponencial  →   exp(x)\n"
            "  Logaritmo    →   log(x)  (base e)\n"
            "  Valor abs.   →   Abs(x)\n"
            "  Arctan       →   atan(x)\n\n"
            "Para h, ingresa un número real.\n"
            "Ej:  0,  1,  -2,  0.5,  3/2"
        )
        ctk.CTkLabel(tarjeta_der, text=sintaxis,
                     font=("Consolas", 12), justify="left",
                     text_color="#aaddff").pack(padx=25, pady=(0, 20), anchor="w")


        ctk.CTkLabel(
            frame,
            text="Librerías: SymPy  ·  CustomTkinter  ·  Matplotlib   |   NumPy: PROHIBIDO ✗",
            font=("Arial", 11),
            text_color="#666688"
        ).grid(row=3, column=0, pady=(8, 16))


    def _construir_calculadora(self):
        frame = self.tab_calculadora
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        contenedor = ctk.CTkFrame(frame)
        contenedor.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        contenedor.grid_columnconfigure(1, weight=1)
        contenedor.grid_rowconfigure(0, weight=1)


        panel = ctk.CTkFrame(contenedor, width=370, corner_radius=10)
        panel.grid(row=0, column=0, sticky="nsew", padx=(8, 4), pady=8)
        panel.grid_propagate(False)

        ctk.CTkLabel(panel, text="Calculadora de Límites",
                     font=("Arial", 19, "bold")).pack(pady=(18, 2))
        ctk.CTkLabel(panel, text="lim f(x)   cuando   x → h",
                     font=("Arial", 12), text_color="#8888bb").pack(pady=(0, 14))


        ctk.CTkLabel(panel, text="Función  f(x) :",
                     font=("Arial", 13, "bold")).pack(anchor="w", padx=18)
        self._entry_fx_calc = ctk.CTkEntry(
            panel,
            placeholder_text="Ej:  (x**2 - 1) / (x - 1)",
            width=330, height=36, font=("Consolas", 12)
        )
        self._entry_fx_calc.pack(pady=(4, 10), padx=18)


        ctk.CTkLabel(panel, text="Valor  h  (hacia donde tiende x) :",
                     font=("Arial", 13, "bold")).pack(anchor="w", padx=18)
        self._entry_h_calc = ctk.CTkEntry(
            panel,
            placeholder_text="Ej:  1   (número real)",
            width=330, height=36, font=("Consolas", 12)
        )
        self._entry_h_calc.pack(pady=(4, 14), padx=18)


        ctk.CTkButton(
            panel,
            text="▶  Calcular Límite y Graficar",
            height=42,
            font=("Arial", 14, "bold"),
            fg_color="#3a6fbf",
            hover_color="#2d5a9e",
            command=self._accion_calcular_finito
        ).pack(pady=10, padx=18, fill="x")


        self._label_result_calc = ctk.CTkLabel(
            panel, text="",
            font=("Arial", 15, "bold"),
            text_color="#ffdd55",
            wraplength=330
        )
        self._label_result_calc.pack(pady=(2, 6), padx=18)


        ctk.CTkLabel(panel, text="Procedimiento paso a paso:",
                     font=("Arial", 12, "bold")).pack(anchor="w", padx=18)
        self._txt_proc_calc = ctk.CTkTextbox(
            panel, font=("Consolas", 10.5),
            text_color="#ccddff"
        )
        self._txt_proc_calc.pack(fill="both", expand=True, padx=18, pady=(4, 18))


        frame_graf = ctk.CTkFrame(contenedor, corner_radius=10)
        frame_graf.grid(row=0, column=1, sticky="nsew", padx=(4, 8), pady=8)

        self._fig_calc, self._ax_calc, self._canvas_calc = \
            self._crear_canvas_matplotlib(frame_graf)

    def _accion_calcular_finito(self):

        expr_str = self._entry_fx_calc.get().strip()
        h_str    = self._entry_h_calc.get().strip()


        if not expr_str or not h_str:
            self._label_result_calc.configure(text="")
            self._mostrar_texto(self._txt_proc_calc,
                "⚠ Debes completar ambos campos:\n  • Función f(x)\n  • Valor h")
            return

        try:
            h_val = sp.sympify(h_str)
            _ = float(h_val)   
        except Exception:
            self._label_result_calc.configure(text="")
            self._mostrar_texto(self._txt_proc_calc,
                f"✗ '{h_str}' no es un valor válido para h.\n"
                "Ingresa un número real, ej: 0, 1, -2, 0.5")
            return


        resultado, procedimiento = self._calcular_limite(expr_str, h_val)


        self._mostrar_texto(self._txt_proc_calc, procedimiento)

        if resultado is not None:
            self._label_result_calc.configure(
                text=f"lim  f(x)  =  {resultado}",
                text_color="#ffdd55"
            )
        else:
            self._label_result_calc.configure(
                text="El límite NO EXISTE",
                text_color="#ff6666"
            )


        self._graficar_finito(expr_str, h_val, resultado)

    def _graficar_finito(self, expr_str, h_val, resultado):
        x_sym = sp.Symbol('x')
        try:
            expr   = sp.sympify(expr_str, locals={"x": x_sym})
            h_f    = float(h_val)
            margen = max(6.0, abs(h_f) * 0.6 + 4.0)

            xs_brutos = self._generar_x(h_f - margen, h_f + margen, pasos=800)
            xs, ys    = self._evaluar_funcion(expr, xs_brutos)

            self._ax_calc.clear()
            self._aplicar_estilo_ejes(self._ax_calc)


            self._graficar_por_segmentos(
                self._ax_calc, xs, ys,
                color="#5599ff",
                label=f"f(x) = {expr_str}"
            )

            self._ax_calc.axvline(
                x=h_f, color="#ff7043",
                linestyle="--", linewidth=1.8, alpha=0.85,
                label=f"x = {h_val}"
            )


            if resultado is not None and resultado not in (sp.oo, -sp.oo):
                try:
                    lim_f = float(resultado)
                    self._ax_calc.scatter(
                        [h_f], [lim_f],
                        color="#ffeb3b", zorder=6, s=120,
                        label=f"Límite = {resultado}"
                    )


                    try:
                        f_en_h = float(sp.simplify(expr.subs(x_sym, h_val)))
                        if math.isfinite(f_en_h) and abs(f_en_h - lim_f) > 1e-9:
                            self._ax_calc.scatter(
                                [h_f], [f_en_h],
                                s=100, zorder=5,
                                facecolors="none",
                                edgecolors="#ffffff",
                                linewidths=2,
                                label=f"f({h_val}) = {round(f_en_h, 4)}"
                            )
                    except Exception:
                        pass
                except (TypeError, ValueError):
                    pass

            self._ajustar_ylim(self._ax_calc, ys)
            self._ax_calc.set_title(
                f"f(x) = {expr_str}    |    lim x→{h_val}  =  {resultado}",
                color="white", fontsize=10, pad=10
            )
            self._ax_calc.legend(
                facecolor="#1e1e2e", edgecolor="#444466",
                labelcolor="white", fontsize=9
            )
            self._fig_calc.tight_layout()
            self._canvas_calc.draw()

        except Exception as e:
            pass



    def _construir_infinito(self):
        frame = self.tab_infinito
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(0, weight=1)

        contenedor = ctk.CTkFrame(frame)
        contenedor.grid(row=0, column=0, sticky="nsew", padx=8, pady=8)
        contenedor.grid_columnconfigure(1, weight=1)
        contenedor.grid_rowconfigure(0, weight=1)


        panel = ctk.CTkFrame(contenedor, width=370, corner_radius=10)
        panel.grid(row=0, column=0, sticky="nsew", padx=(8, 4), pady=8)
        panel.grid_propagate(False)

        ctk.CTkLabel(panel, text="Límites al Infinito",
                     font=("Arial", 19, "bold")).pack(pady=(18, 2))
        ctk.CTkLabel(panel, text="lim f(x)   cuando   x → ±∞",
                     font=("Arial", 12), text_color="#8888bb").pack(pady=(0, 14))

        ctk.CTkLabel(panel, text="Función  f(x) :",
                     font=("Arial", 13, "bold")).pack(anchor="w", padx=18)
        self._entry_fx_inf = ctk.CTkEntry(
            panel,
            placeholder_text="Ej:  (3*x**2 + 2) / (x**2 - 5)",
            width=330, height=36, font=("Consolas", 12)
        )
        self._entry_fx_inf.pack(pady=(4, 10), padx=18)

        ctk.CTkLabel(panel, text="Dirección:",
                     font=("Arial", 13, "bold")).pack(anchor="w", padx=18)
        self._opt_dir = ctk.CTkOptionMenu(
            panel,
            values=["x → +∞", "x → -∞", "Ambas direcciones"],
            font=("Arial", 13),
            width=330
        )
        self._opt_dir.set("x → +∞")
        self._opt_dir.pack(pady=(4, 14), padx=18)

        ctk.CTkButton(
            panel,
            text="▶  Calcular Límite y Graficar",
            height=42,
            font=("Arial", 14, "bold"),
            fg_color="#3a6fbf",
            hover_color="#2d5a9e",
            command=self._accion_calcular_infinito
        ).pack(pady=10, padx=18, fill="x")

        self._label_result_inf = ctk.CTkLabel(
            panel, text="",
            font=("Arial", 14, "bold"),
            text_color="#ffdd55",
            wraplength=330
        )
        self._label_result_inf.pack(pady=(2, 6), padx=18)

        ctk.CTkLabel(panel, text="Procedimiento paso a paso:",
                     font=("Arial", 12, "bold")).pack(anchor="w", padx=18)
        self._txt_proc_inf = ctk.CTkTextbox(
            panel, font=("Consolas", 10.5),
            text_color="#ccddff"
        )
        self._txt_proc_inf.pack(fill="both", expand=True, padx=18, pady=(4, 18))


        frame_graf = ctk.CTkFrame(contenedor, corner_radius=10)
        frame_graf.grid(row=0, column=1, sticky="nsew", padx=(4, 8), pady=8)

        self._fig_inf, self._ax_inf, self._canvas_inf = \
            self._crear_canvas_matplotlib(frame_graf)

    def _accion_calcular_infinito(self):
        expr_str  = self._entry_fx_inf.get().strip()
        direccion = self._opt_dir.get()

        if not expr_str:
            self._mostrar_texto(self._txt_proc_inf,
                "Ingresa una función f(x).")
            return

        x_sym = sp.Symbol('x')
        try:
            sp.sympify(expr_str, locals={"x": x_sym})
        except Exception:
            self._mostrar_texto(self._txt_proc_inf,
                "✗ Función no válida. Revisa la sintaxis.")
            return

        texto_total = []
        res_pos, res_neg = None, None

        if direccion in ("x → +∞", "Ambas direcciones"):
            res_pos, proc = self._calcular_limite(expr_str, sp.oo)
            texto_total.append(proc)

        if direccion in ("x → -∞", "Ambas direcciones"):
            if texto_total:
                texto_total.append("\n" + "─" * 48 + "\n")
            res_neg, proc = self._calcular_limite(expr_str, -sp.oo)
            texto_total.append(proc)

        self._mostrar_texto(self._txt_proc_inf, "\n".join(texto_total))


        resumen = []
        if res_pos is not None and direccion in ("x → +∞", "Ambas direcciones"):
            resumen.append(f"lim(+∞) = {res_pos}")
        if res_neg is not None and direccion in ("x → -∞", "Ambas direcciones"):
            resumen.append(f"lim(-∞) = {res_neg}")
        self._label_result_inf.configure(
            text="  |  ".join(resumen) if resumen else ""
        )

        self._graficar_infinito(expr_str, direccion, res_pos, res_neg)

    def _graficar_infinito(self, expr_str, direccion, res_pos, res_neg):
        x_sym = sp.Symbol('x')
        try:
            expr = sp.sympify(expr_str, locals={"x": x_sym})

            xs_brutos = self._generar_x(-60, 60, pasos=1200)
            xs, ys    = self._evaluar_funcion(expr, xs_brutos)

            self._ax_inf.clear()
            self._aplicar_estilo_ejes(self._ax_inf)

            self._graficar_por_segmentos(
                self._ax_inf, xs, ys,
                color="#81c784",
                label=f"f(x) = {expr_str}"
            )


            if res_pos is not None and res_pos not in (sp.oo, -sp.oo):
                try:
                    yh = float(res_pos)
                    self._ax_inf.axhline(
                        y=yh, color="#ff7043", linestyle="--",
                        linewidth=1.8, alpha=0.8,
                        label=f"y = {res_pos}  (asíntota x→+∞)"
                    )
                except Exception:
                    pass

            if res_neg is not None and res_neg not in (sp.oo, -sp.oo):
                try:
                    yh = float(res_neg)
                    # Solo dibujar si es diferente al de +∞
                    if res_pos is None or float(res_pos) != yh:
                        self._ax_inf.axhline(
                            y=yh, color="#ce93d8", linestyle="--",
                            linewidth=1.8, alpha=0.8,
                            label=f"y = {res_neg}  (asíntota x→-∞)"
                        )
                except Exception:
                    pass

            self._ajustar_ylim(self._ax_inf, ys, limite_absoluto=200)
            self._ax_inf.set_title(
                f"f(x) = {expr_str}    |    comportamiento en ±∞",
                color="white", fontsize=10, pad=10
            )
            self._ax_inf.legend(
                facecolor="#1e1e2e", edgecolor="#444466",
                labelcolor="white", fontsize=9
            )
            self._fig_inf.tight_layout()
            self._canvas_inf.draw()

        except Exception:
            pass



    def _construir_ejemplos(self):
        frame = self.tab_ejemplos
        frame.grid_columnconfigure(0, weight=1)
        frame.grid_rowconfigure(1, weight=1)

        ctk.CTkLabel(frame, text="Ejemplos Predefinidos",
                     font=("Arial", 22, "bold")).grid(row=0, column=0, pady=(16, 6))

        contenedor = ctk.CTkFrame(frame)
        contenedor.grid(row=1, column=0, sticky="nsew", padx=12, pady=(0, 12))
        contenedor.grid_columnconfigure(1, weight=1)
        contenedor.grid_rowconfigure(0, weight=1)

        panel_scroll = ctk.CTkScrollableFrame(contenedor, width=370, corner_radius=10)
        panel_scroll.grid(row=0, column=0, sticky="nsew", padx=(8, 4), pady=8)


        frame_der = ctk.CTkFrame(contenedor, corner_radius=10)
        frame_der.grid(row=0, column=1, sticky="nsew", padx=(4, 8), pady=8)

        self._fig_ej, self._ax_ej, self._canvas_ej = \
            self._crear_canvas_matplotlib(frame_der)

        self._txt_proc_ej = ctk.CTkTextbox(
            frame_der, font=("Consolas", 10), height=180,
            text_color="#ccddff"
        )
        self._txt_proc_ej.pack(fill="x", padx=8, pady=(4, 8))

        ejemplos = [
            (
                "1 · Sustitución directa\n   lim (x² + 2x)  →  x = 3",
                "x**2 + 2*x", "3",
                "Caso más simple: f(3) existe y es el límite."
            ),
            (
                "2 · Forma indeterminada 0/0\n   lim (x²-1)/(x-1)  →  x = 1",
                "(x**2 - 1) / (x - 1)", "1",
                "Se factoriza: (x-1)(x+1)/(x-1) → x+1. Lím = 2."
            ),
            (
                "3 · Límite trigonométrico clásico\n   lim sin(x)/x  →  x = 0",
                "sin(x) / x", "0",
                "Resultado fundamental del cálculo: lím = 1."
            ),
            (
                "4 · Discontinuidad de salto\n   lim |x|/x  →  x = 0",
                "Abs(x) / x", "0",
                "Lateral izq = -1, lateral der = +1. No existe."
            ),
            (
                "5 · Discontinuidad removible\n   lim (x³-x)/(x²-1)  →  x = 1",
                "(x**3 - x) / (x**2 - 1)", "1",
                "Factorizando: x(x-1)(x+1)/((x-1)(x+1)) → x. Lím = 1."
            ),
            (
                "6 · Raíz con indeterminación\n   lim (√x - 1)/(x - 1)  →  x = 1",
                "(sqrt(x) - 1) / (x - 1)", "1",
                "Se racionaliza: (√x-1)(√x+1)/((x-1)(√x+1)) → 1/(√x+1). Lím = 1/2."
            ),
            (
                "7 · Polinomio racional\n   lim (2x²+3x-2)/(x+2)  →  x = -2",
                "(2*x**2 + 3*x - 2) / (x + 2)", "-2",
                "Se factoriza el numerador: (2x-1)(x+2)/(x+2)."
            ),

            (
                "8 · Asíntota horizontal\n   lim (3x²+2)/(x²-5)  →  +∞",
                "(3*x**2 + 2) / (x**2 - 5)", "+oo",
                "Mismo grado: cociente de coef. líderes = 3."
            ),
            (
                "9 · Exponencial al infinito\n   lim e^x  →  +∞",
                "exp(x)", "+oo",
                "Crece indefinidamente. Lím = +∞."
            ),
            (
                "10 · Arctan al infinito\n    lim atan(x)  →  +∞",
                "atan(x)", "+oo",
                "Converge a π/2. Asíntota horizontal y = π/2."
            ),
            (
                "11 · Límite -∞ de racional\n    lim (x+1)/(x-1)  →  -∞",
                "(x + 1) / (x - 1)", "-oo",
                "Mismo grado: coef. líderes iguales → lím = 1."
            ),
            (
                "12 · Forma ∞ - ∞\n    lim (√(x²+x) - x)  →  +∞",
                "sqrt(x**2 + x) - x", "+oo",
                "Racionalización: lím = 1/2."
            ),
        ]

        ctk.CTkLabel(panel_scroll,
                     text="Haz clic en un ejercicio:",
                     font=("Arial", 14, "bold")).pack(pady=(12, 6), padx=10)

        for titulo, fx, h_str, desc in ejemplos:
            frame_btn = ctk.CTkFrame(panel_scroll, corner_radius=8,
                                     fg_color="#1e1e2e")
            frame_btn.pack(fill="x", padx=8, pady=5)

            btn = ctk.CTkButton(
                frame_btn,
                text=titulo,
                anchor="w",
                font=("Consolas", 11),
                height=52,
                fg_color="#252540",
                hover_color="#353565",
                corner_radius=8,
                command=lambda f=fx, h=h_str, d=desc: self._ejecutar_ejemplo(f, h, d)
            )
            btn.pack(fill="x", padx=4, pady=4)

    def _ejecutar_ejemplo(self, fx: str, h_str: str, descripcion: str):
        if h_str in ("+oo", "oo"):
            h_val = sp.oo
        elif h_str == "-oo":
            h_val = -sp.oo
        else:
            h_val = sp.sympify(h_str)

        resultado, procedimiento = self._calcular_limite(fx, h_val)


        encabezado = f"  {descripcion}\n\n"
        self._mostrar_texto(self._txt_proc_ej, encabezado + procedimiento)


        x_sym = sp.Symbol('x')
        try:
            expr = sp.sympify(fx, locals={"x": x_sym})

            if h_val in (sp.oo, -sp.oo):
                x_ini, x_fin = -50, 50
            else:
                h_f    = float(h_val)
                margen = max(6.0, abs(h_f) * 0.6 + 4.0)
                x_ini  = h_f - margen
                x_fin  = h_f + margen

            xs_brutos = self._generar_x(x_ini, x_fin, pasos=800)
            xs, ys    = self._evaluar_funcion(expr, xs_brutos)

            self._ax_ej.clear()
            self._aplicar_estilo_ejes(self._ax_ej)

            self._graficar_por_segmentos(
                self._ax_ej, xs, ys,
                color="#80cbc4",
                label=f"f(x) = {fx}"
            )


            if h_val not in (sp.oo, -sp.oo):
                h_f = float(h_val)
                self._ax_ej.axvline(
                    x=h_f, color="#ff7043",
                    linestyle="--", linewidth=1.8, alpha=0.8,
                    label=f"x = {h_val}"
                )
                if resultado is not None and resultado not in (sp.oo, -sp.oo):
                    try:
                        lim_f = float(resultado)
                        self._ax_ej.scatter(
                            [h_f], [lim_f],
                            color="#ffeb3b", zorder=6, s=120,
                            label=f"Límite = {resultado}"
                        )
                    except Exception:
                        pass
            else:
                if resultado is not None and resultado not in (sp.oo, -sp.oo):
                    try:
                        yh = float(resultado)
                        self._ax_ej.axhline(
                            y=yh, color="#ff7043",
                            linestyle="--", linewidth=1.8, alpha=0.8,
                            label=f"y = {resultado} (asíntota)"
                        )
                    except Exception:
                        pass

            self._ajustar_ylim(self._ax_ej, ys)
            self._ax_ej.set_title(
                f"f(x) = {fx}    |    lim = {resultado}",
                color="white", fontsize=10, pad=10
            )
            self._ax_ej.legend(
                facecolor="#1e1e2e", edgecolor="#444466",
                labelcolor="white", fontsize=9
            )
            self._fig_ej.tight_layout()
            self._canvas_ej.draw()

        except Exception:
            pass


if __name__ == "__main__":
    app = App()
    app.mainloop()