import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp


class App(ctk.CTk):

    def __init__(self):
        super().__init__()


        self.title("Calculo de Limites")
        self.geometry("1200x720")


        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)


        self.tabs = ctk.CTkTabview(self)
        self.tabs.grid(row=0, column=0, padx=20, pady=20, sticky="nsew")


        self.tab_inicio = self.tabs.add("Inicio")
        self.tab_limite = self.tabs.add("Limite")


        self.crear_inicio()
        self.crear_limite()





    def crear_inicio(self):
        titulo = ctk.CTkLabel(
            self.tab_inicio,
            text="Projecto Limites",
            font=("Arial", 50, "bold")
        )
        titulo.pack(pady=60, padx=30)

        texto = """
            Esta aplicación fue desarrollada con:\n
            • customtkinter  → interfaz gráfica moderna\n
            • sympy          → cálculo simbólico de límites\n
            • matplotlib     → visualización de funciones\n\n
            Funcionalidades:\n
            ✔ Ingresar una función f(x)\n
            ✔ Calcular el límite en un punto\n
            ✔ Graficar la función\n
            ✔ Mostrar el resultado"""

        caja = ctk.CTkTextbox(self.tab_inicio, width=900, height=600, font=("Arial", 16))
        caja.pack(pady=20)
        caja.insert("1.0", texto)
        caja.configure(state="disabled")










    def crea_grafico(self, frame):
        figura = Figure(figsize=(6, 5), dpi=100)
        figura.patch.set_facecolor('#242424')
        eje = figura.add_subplot(111)
        eje.set_facecolor('#1a1a1a')          
        eje.tick_params(colors='white')
        
        canvas = FigureCanvasTkAgg(figura, master=frame)
        canvas.get_tk_widget().pack(fill="both", expand=True)
        return figura, eje, canvas





    def crear_limite(self):

        self.tab_limite.grid_columnconfigure(0, weight=4)
        self.tab_limite.grid_columnconfigure(1, weight=1)
        self.tab_limite.grid_rowconfigure(0, weight=1)


        contenedor_datos = ctk.CTkFrame(self.tab_limite)
        contenedor_datos.grid(row=0, column=1, padx=0, pady=15, sticky="nsew")

        titulo = ctk.CTkLabel(contenedor_datos, text="Menu de Datos", font=("Arial", 22, "bold"))
        titulo.pack(pady=15)


        titulo_fx = ctk.CTkLabel(contenedor_datos, text="Ingrese la función:  Ej: (x**2 - 4)/(x - 2) o sin(x)/x)", font=("Arial", 14))
        titulo_fx.pack(pady=(10, 2))
        self.entrada_fx = ctk.CTkEntry(contenedor_datos, width=250, placeholder_text="f(x)")
        self.entrada_fx.pack(pady=5)

        titulo_h = ctk.CTkLabel(contenedor_datos, text="Ingrese el valor al que tiene x:", font=("Arial", 14))
        titulo_h.pack(pady=(10, 2))
        self.entrada_h = ctk.CTkEntry(contenedor_datos, width=250, placeholder_text="h")
        self.entrada_h.pack(pady=5)


        self.btn_calcular = ctk.CTkButton(contenedor_datos, text="Calcular y Graficar", command=self.procesar_limite, font=("Arial", 14, "bold"))
        self.btn_calcular.pack(pady=25)


        titulo_resultado = ctk.CTkLabel(contenedor_datos, text="Desarrollo:", font=("Arial", 15, "bold"))
        titulo_resultado.pack(pady=(10, 2))

        self.txt_resultado = ctk.CTkTextbox(contenedor_datos, width=350, height=220, font=("Consolas", 12))
        self.txt_resultado.pack(padx=0, pady=5)
        

        self.resultado_final = ctk.CTkLabel(contenedor_datos, text="Límite L = ", font=("Arial", 18, "bold"), text_color="#1f538d")
        self.resultado_final.pack(pady=15)


        self.grafico = ctk.CTkFrame(self.tab_limite)
        self.grafico.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")
        

        self.figura, self.eje, self.canvas = self.crea_grafico(self.grafico)





    def procesar_limite(self):

        self.txt_resultado.configure(state="normal")
        self.txt_resultado.delete("1.0", "end")

        try:

            str_fx = self.entrada_fx.get()
            str_h = self.entrada_h.get()

            if not str_fx or not str_h:
                self.resultado_final.configure(text="Error: Rellene todos los campos", text_color="red")
                return


            x = sp.symbols('x')
            

            expresion = sp.sympify(str_fx)
            

            es_infinito_pos = (str_h.strip() == "oo")
            es_infinito_neg = (str_h.strip() == "-oo")
            es_infinito = es_infinito_pos or es_infinito_neg

            if es_infinito:

                pasos_infinitos = [10, 100, 1000, 10000, 100000]
                h_imprimible = "+oo" if es_infinito_pos else "-oo"
                self.txt_resultado.insert("end", f"Evaluando tendencia hacia h = {h_imprimible}\n")
                self.txt_resultado.insert("end", f"{'Dirección':<12} | {'x':<12} | {'f(x)':<15}\n")
                self.txt_resultado.insert("end", "-" * 48 + "\n")
                
                limite_final = None
                for paso in pasos_infinitos:

                    x_eval = paso if es_infinito_pos else -paso
                    y_eval = expresion.subs(x, x_eval).evalf()
                    limite_final = float(y_eval)
                    
                    dir_texto = "Tendencia (+)" if es_infinito_pos else "Tendencia (-)"
                    self.txt_resultado.insert("end", f"{dir_texto:<12} | {x_eval:<12} | {limite_final:<15.6f}\n")
                

                L = round(limite_final, 4)
                self.resultado_final.configure(text=f"Límite L = {L}", text_color="#22c55e")
            else:
                h = float(sp.sympify(str_h).evalf())


                self.txt_resultado.insert("end", f"Evaluando entorno alrededor de h = {h}\n")
                self.txt_resultado.insert("end", f"{'Dirección':<12} | {'x':<12} | {'f(x)':<15}\n")
                self.txt_resultado.insert("end", "-" * 48 + "\n")


                distancias = [0.1, 0.01, 0.001, 0.0001, 0.00001]
                
                limite_izq = None
                limite_der = None


                for d in distancias:
                    x_eval = h - d

                    y_eval = expresion.subs(x, x_eval).evalf()
                    limite_izq = float(y_eval)
                    self.txt_resultado.insert("end", f"Izquierda (-) | {x_eval:<12.5f} | {limite_izq:<15.6f}\n")

                self.txt_resultado.insert("end", "-" * 48 + "\n")


                for d in distancias:
                    x_eval = h + d
                    y_eval = expresion.subs(x, x_eval).evalf()
                    limite_der = float(y_eval)
                    self.txt_resultado.insert("end", f"Derecha   (+) | {x_eval:<12.5f} | {limite_der:<15.6f}\n")



                if abs(limite_izq - limite_der) < 1e-4:

                    L = round(limite_izq, 4)
                    self.resultado_final.configure(text=f"Límite L = {L}", text_color="#22c55e")
                else:
                    self.resultado_final.configure(text="El límite No Existe (L. Laterales distintos)", text_color="orange")


            self.eje.clear()
            self.eje.set_facecolor('#1a1a1a')


            puntos_x = []
            puntos_y = []
            pasos = 200

            if es_infinito:
                if es_infinito_pos:
                    inicio_rango = 0
                    fin_rango = 100
                else:
                    inicio_rango = -100
                    fin_rango = 0
            else:
                inicio_rango = h - 10
                fin_rango = h + 10

            ancho_paso = (fin_rango - inicio_rango) / pasos


            for i in range(pasos + 1):
                cur_x = inicio_rango + (i * ancho_paso)

                if not es_infinito and abs(cur_x - h) < 1e-6:
                    continue
                try:
                    cur_y = float(expresion.subs(x, cur_x).evalf())

                    if abs(cur_y) < 1000:
                        puntos_x.append(cur_x)
                        puntos_y.append(cur_y)
                except Exception:
                    pass


            self.eje.plot(puntos_x, puntos_y, color='#1f77b4', linewidth=2.5, label=f"f(x) = {str_fx}")

            if es_infinito:

                self.eje.axhline(y=0, color='red', linestyle='--', alpha=0.6, label=f"Asín. Horiz. y = {L}")
            else:

                self.eje.axvline(x=h, color='red', linestyle='--', alpha=0.6, label=f"x = {h}")
            

            self.eje.grid(True, color='#444444', linestyle=':')
            self.eje.tick_params(colors='white')
            self.eje.legend(loc="upper right")
            

            self.canvas.draw()

        except Exception as err:

            self.resultado_final.configure(text="error de cálculo", text_color="red")
            self.txt_resultado.insert("end", f"\n[ERROR]: {str(err)}\nRevise que ingreso datos correctos (ej: 2*x en vez de 2x).")
        

        self.txt_resultado.configure(state="disabled")





    def mostrar_texto(self, caja, texto):
        caja.configure(state="normal")
        caja.delete("1.0", "end")
        caja.insert("1.0", texto)
        caja.configure(state="disabled")

if __name__ == "__main__":
    app = App()
    app.mainloop()


