import sympy as sp
from sympy import symbols
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math

def calcular_limite_numerico(funcion_str, c_str):

    try:

        c_val = float(sp.sympify(c_str).evalf())
    except Exception:
        return "Error: Verifica el valor de x."


    h = 0.00001 
    

    lim_izq = evaluar_funcion(funcion_str, c_val - h)
    lim_der = evaluar_funcion(funcion_str, c_val + h)
    

    if lim_izq is None or lim_der is None:
        return "El límite diverge o es indefinido"
        

    if abs(lim_izq - lim_der) < 0.01:

        limite_final = (lim_izq + lim_der) / 2
        return round(limite_final, 4)
    else:

        return "No existe (límites laterales distintos)"


class App(ctk.CTk):
    def __init__(self):
        super().__init__()


        self.geometry("800x600")
        self.title("Analizador de limites")
        

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


        self.tab_inicio = self.tabs.add("Inicio")
        self.tab_limites_algebraicos = self.tabs.add("Límites algebraicos")
        self.tab_limites_trigonometricos = self.tabs.add("Límites trigonométricos")
        self.tab_limites_infinitos = self.tabs.add("Límites infinitos")


        self.crear_inicio()



        




    def crear_inicio(self):
        titulo = ctk.CTkLabel(
            self.tab_inicio,
            text = "Pestaña de inicio",
            font = ("Arial", 30, "bold")
            )
        titulo.pack(pady=25)

        texto = """Programa para representar límites y blablabla"""


        caja = ctk.CTkTextbox(self.tab_inicio, width=900, height=350, font=("Arial", 16))
        caja.pack(pady=20)
        caja.insert("1.0", texto)
        caja.configure(state="disabled")

    def crear_canvas(self, frame):
        figura = Figure(figsize=(6, 5), dpi=100)
        eje = figura.add_subplot(111)
        canvas = FigureCanvasTkAgg(figura, master=frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        return figura, eje, canvas
        




    def L_algebraicos(self):
        contenedor = ctk.CTkFrame(self.L_algebraicos) 
        contenedor.pack(fill="both", expand=True, padx=10, pady=10)

        panel = ctk.CTkFrame(contenedor, width=340)
        panel.pack(side="left", fill="y", padx=10, pady=10)

        grafico = ctk.CTkFrame(contenedor)
        grafico.pack(side="right", fill="both", expand=True, padx=10, pady=10)

        ctk.CTkLabel(panel, text="Límite algebraico", font=("Arial", 24, "bold")).pack(pady=15)

        ctk.CTkLabel(panel, text="Función: ").pack()
        entry_funcion = ctk.CTkEntry(app, placeholder_text="Ingrese f(x) ej: (x**2 - 1)/(x - 1)")
        entry_funcion.pack(pady=10)

        ctk.CTkLabel(panel, text="Valor al que tiende x: ").pack()
        entry_h = ctk.CTkEntry(app, placeholder_text="Valor de c (ej: 1 o oo)")
        entry_h.pack(pady=10)

        """#ctk.CTkButton(
            panel, 
            text="Calcular y graficar"
            command=self.graicar_limite
        ).pack(pady=20)"""
        
        self.resulttado_limite = ctk.CTkTextbox(panel, width=310, height=350)
        self.resultado_limite.pack(pady=10)





    def calcular_limite_trig(self):
        import math
        
        x = sp.Symbol('x')
        func_str = self.entry_trig_funcion.get()
        c_str = self.entry_trig_c.get()

        try:
            f = sp.sympify(func_str)
            c = sp.sympify(c_str)




            limite_texto = ""
            
            if c == sp.oo:
                valor = f.subs(x, 1000000).evalf()
                limite_texto = str(round(valor, 4))
            elif c == -sp.oo:
                valor = f.subs(x, -1000000).evalf()
                limite_texto = str(round(valor, 4))
            else:
                epsilon = 1e-6
                limite_izq = f.subs(x, c - epsilon).evalf()
                limite_der = f.subs(x, c + epsilon).evalf()
                
                if abs(limite_izq - limite_der) < 1e-3:
                    limite_promedio = (limite_izq + limite_der) / 2
                    limite_texto = str(round(limite_promedio, 4))
                else:
                    limite_texto = f"Diverge (Izq: {round(limite_izq, 4)}, Der: {round(limite_der, 4)})"

            self.resultado_trig.delete("1.0", "end")
            self.resultado_trig.insert("1.0", f"Función: {f}\nLímite aproximado (x -> {c}):\nResultado = {limite_texto}")




            self.ax_trig.clear()
            

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
            

            for val in x_vals:
                try:

                    y = f_numerica(val)
                    y_vals.append(y)
                except:


                    y_vals.append(float('nan'))


            self.ax_trig.plot(x_vals, y_vals, label="f(x)", color="cyan")
            

            if c != sp.oo and c != -sp.oo:
                self.ax_trig.axvline(x=c_val, color="red", linestyle="--", alpha=0.6, label=f"x = {c}")

            self.ax_trig.legend()
            self.ax_trig.grid(True, linestyle=":", alpha=0.7)
            self.canvas_trig.draw()

        except Exception as e:
            self.resultado_trig.delete("1.0", "end")
            self.resultado_trig.insert("1.0", f"Error en la expresión:\n{e}")






app = App()
app.mainloop()