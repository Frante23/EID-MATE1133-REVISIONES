import customtkinter as ctk
import sympy as sp
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from calculador_limites import calcular_limite

NORD_DEEP        = "#2E3440"
NORD_DARK        = "#3B4252"
NORD_LIGHT       = "#E5E9F0"
NORD_FROST       = "#88C0D0"
NORD_FROST_HOVER = "#81A1C1"

ctk.set_appearance_mode("dark")

class MathLimites(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Math Limites")
        self.configure(fg_color=NORD_DEEP)
        self.sidebar_expanded = False


        self.sidebar = ctk.CTkFrame(self, fg_color=NORD_DARK, width=50)
        self.sidebar.pack(side="left", fill="y")
        self.sidebar.pack_propagate(False)


        self.btn_toggle = ctk.CTkButton(
            self.sidebar,
            text="☰",
            command=self.abrir_sidebar,
            fg_color="transparent",
            hover_color=NORD_FROST_HOVER,
            text_color=NORD_FROST,
            font=("JetBrains Mono", 20),
            width=40,
            height=40,
        )
        self.btn_toggle.pack(pady=(15, 0), padx=5)


        self.sidebar_content = ctk.CTkFrame(self.sidebar, fg_color="transparent")

        ctk.CTkLabel(
            self.sidebar_content,
            text="Math\nLímites",
            font=("JetBrains Mono", 18, "bold"),
            text_color=NORD_FROST
        ).pack(pady=(15, 30))

        opciones = [("  Límites",                 "Limites")]

        for texto, key in opciones:
            ctk.CTkButton(
                self.sidebar_content,
                text=texto,
                command=lambda k=key: self.seleccionar(k),
                fg_color="transparent",
                hover_color=NORD_FROST_HOVER,
                text_color=NORD_LIGHT,
                font=("JetBrains Mono", 13),
                width=190,
                anchor="w"
            ).pack(padx=10, pady=4)


        self.container = ctk.CTkFrame(self, fg_color=NORD_DEEP)
        self.container.pack(side="right", expand=True, fill="both")
        self.container.bind("<Button-1>", self.cerrar_sidebar)


        self.panel_input = ctk.CTkFrame(self.container, fg_color=NORD_DARK)
        self.panel_input.place(relx=0.805, y=0, relwidth=0.195, relheight=1)

        ctk.CTkLabel(self.panel_input,
            text="Ingrese el límite:",
            font=("JetBrains Mono", 14, "bold"),
            text_color=NORD_FROST
        ).pack(pady=(25, 20))

        ctk.CTkLabel(self.panel_input,
            text="lim(x) =",
            font=("JetBrains Mono", 12),
            text_color=NORD_LIGHT
        ).pack(anchor="w", padx=20)

        self.entry_funcion = ctk.CTkEntry(self.panel_input,
            placeholder_text="ej: (x**2 - 1)/(x - 1)",
            font=("JetBrains Mono", 12),
            width=210
        )
        self.entry_funcion.pack(padx=20, pady=(5, 15))

        ctk.CTkLabel(self.panel_input,
            text="h =",
            font=("JetBrains Mono", 12),
            text_color=NORD_LIGHT
        ).pack(anchor="w", padx=20)

        self.entry_h = ctk.CTkEntry(self.panel_input,
            placeholder_text="ej: 1  o  oo (infinito)",
            font=("JetBrains Mono", 12),
            width=210
        )
        self.entry_h.pack(padx=20, pady=(5, 20))

        ctk.CTkButton(self.panel_input,
            text="Calcular",
            command=self.calcular,
            font=("JetBrains Mono", 13, "bold"),
            fg_color=NORD_FROST,
            hover_color=NORD_FROST_HOVER,
            text_color=NORD_DEEP,
            width=210
        ).pack(padx=20)

        ctk.CTkLabel(self.panel_input,
            text="Resultado:",
            font=("JetBrains Mono", 12, "bold"),
            text_color=NORD_FROST
        ).pack(anchor="w", padx=20, pady=(25, 5))

        self.txt_resultado = ctk.CTkTextbox(self.panel_input,
            font=("JetBrains Mono", 12),
            text_color=NORD_LIGHT,
            width=210,
            height=300,
            state="disabled"
        )
        self.txt_resultado.pack(padx=20, pady=(0, 20))


        self.frames = {}
        for nombre in ["Limites"]:
            frame = ctk.CTkFrame(self.container, fg_color=NORD_DEEP)
            frame.place(x=0, y=0, relwidth=0.805, relheight=1)
            self.frames[nombre] = frame
            frame.bind("<Button-1>", self.cerrar_sidebar)

        for nombre, frame in self.frames.items():
            if nombre == "Limites":
                self.setup_grafica(frame)
            else:
                ctk.CTkLabel(
                    frame,
                    text=nombre,
                    font=("JetBrains Mono", 24, "bold"),
                    text_color=NORD_FROST
                ).place(relx=0.5, rely=0.5, anchor="center")

        self.frames["Limites"].lift()

    def setup_grafica(self, frame):
        fig = Figure(figsize=(5, 4), facecolor="#2E3440")
        self.ax = fig.add_subplot(111)
        self.ax.set_facecolor("#3B4252")
        self.ax.tick_params(colors="#E5E9F0")
        self.ax.spines["bottom"].set_color("#E5E9F0")
        self.ax.spines["left"].set_color("#E5E9F0")
        self.ax.spines["top"].set_color("#3B4252")
        self.ax.spines["right"].set_color("#3B4252")
        self.ax.set_title("Ingrese una función y presione Calcular",
            color="#88C0D0", fontsize=10)

        self.canvas = FigureCanvasTkAgg(fig, master=frame)
        self.canvas.get_tk_widget().place(
            relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)
        self.canvas.draw()

    def abrir_sidebar(self):
        self.sidebar.configure(width=220)
        self.btn_toggle.pack_forget()
        self.sidebar_content.pack(fill="both", expand=True, padx=5)
        self.sidebar_expanded = True

    def cerrar_sidebar(self, event=None):
        if self.sidebar_expanded:
            self.sidebar_content.pack_forget()
            self.sidebar.configure(width=50)
            self.btn_toggle.pack(pady=(15, 0), padx=5)
            self.sidebar_expanded = False

    def seleccionar(self, seccion: str):
        self.frames[seccion].lift()
        self.cerrar_sidebar()

    def calcular(self):
        funcion_str = self.entry_funcion.get().strip()
        h_str = self.entry_h.get().strip()


        if not funcion_str or not h_str:
            self.mostrar_resultado("⚠ Error: Complete ambos campos antes de calcular.")
            return


        try:
            x = sp.Symbol('x')
            sp.sympify(funcion_str)
        except Exception:
            self.mostrar_resultado(
                "⚠ Error: La función ingresada no es válida.\n\n"
                "Ejemplos válidos:\n"
                "  (x**2 - 1)/(x - 1)\n"
                "  sin(x)/x\n"
                "  (x**3 - 8)/(x - 2)"
            )
            return


        valores_infinito = ["oo", "inf", "∞", "-oo", "-inf", "-∞"]
        if h_str not in valores_infinito:
            try:
                float(h_str)
            except ValueError:
                self.mostrar_resultado(
                    "⚠ Error: El valor de h no es válido.\n\n"
                    "Ejemplos válidos:\n"
                    "  1\n"
                    "  0\n"
                    "  -2\n"
                    "  oo  (para infinito)\n"
                    "  -oo (para menos infinito)"
                )
                return


        resultado = calcular_limite(funcion_str, h_str)
        pasos = resultado["pasos"]
        valor = resultado["resultado"]

        texto = "\n".join(pasos)
        texto += f"\n\n{'═'*31}\n  LÍMITE = {valor}\n{'═'*31}"

        self.mostrar_resultado(texto)
        self.graficar(funcion_str, h_str, valor)
        self.frames["Limites"].lift()

    def graficar(self, funcion_str: str, h_str: str, limite: str):
        x = sp.Symbol('x')

        try:
            funcion = sp.sympify(funcion_str)

            if h_str.strip() in ["oo", "inf"]:
                x_vals = [1 + i * 0.5 for i in range(200)]
            elif h_str.strip() in ["-oo", "-inf"]:
                x_vals = [-1 - i * 0.5 for i in range(200)]
            else:
                h = float(h_str)
                paso = 0.01
                x_vals = [h - 2 + i * paso for i in range(401)]

            y_vals = []
            for val in x_vals:
                try:
                    y = float(funcion.subs(x, val))
                    if abs(y) > 1e6:
                        y_vals.append(None)
                    else:
                        y_vals.append(y)
                except:
                    y_vals.append(None)

            self.ax.clear()
            self.ax.set_facecolor("#3B4252")
            self.ax.tick_params(colors="#E5E9F0")
            self.ax.spines["bottom"].set_color("#E5E9F0")
            self.ax.spines["left"].set_color("#E5E9F0")
            self.ax.spines["top"].set_color("#3B4252")
            self.ax.spines["right"].set_color("#3B4252")

            segmento_x = []
            segmento_y = []
            for xv, yv in zip(x_vals, y_vals):
                if yv is None:
                    if segmento_x:
                        self.ax.plot(segmento_x, segmento_y,
                            color="#88C0D0", linewidth=2)
                        segmento_x, segmento_y = [], []
                else:
                    segmento_x.append(xv)
                    segmento_y.append(yv)
            if segmento_x:
                self.ax.plot(segmento_x, segmento_y,
                    color="#88C0D0", linewidth=2)

            if h_str.strip() not in ["oo", "inf", "-oo", "-inf"]:
                h = float(h_str)
                if limite not in ["None", "Error", "∞", "En desarrollo"]:
                    lim_val = float(limite)
                    self.ax.axvline(x=h, color="#BF616A",
                        linestyle="--", linewidth=1, alpha=0.7)
                    self.ax.plot(h, lim_val, "o",
                        color="#BF616A", markersize=8,
                        label=f"lim = {round(lim_val, 4)}")
                    self.ax.legend(facecolor="#3B4252",
                        labelcolor="#E5E9F0", fontsize=9)

            self.ax.set_title(f"f(x) = {funcion_str}",
                color="#88C0D0", fontsize=10)
            self.ax.grid(True, color="#4C566A", alpha=0.5)
            self.canvas.draw()

        except Exception as e:
            self.ax.set_title(f"Error al graficar: {e}",
                color="#BF616A", fontsize=10)
            self.canvas.draw()

    def mostrar_resultado(self, texto: str):
        self.txt_resultado.configure(state="normal")
        self.txt_resultado.delete("1.0", "end")
        self.txt_resultado.insert("1.0", texto)
        self.txt_resultado.configure(state="disabled")

app = MathLimites()
app.mainloop()