import customtkinter as ctk
import sympy as sp
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math




def calcular_limite():
    x = sp.Symbol('x')

    func_str = entry_funcion.get()
    c_str = entry_c.get()

    try:

        f = sp.sympify(func_str)
        c = sp.sympify(c_str)


        limite_exacto = ""

        evaluacion_directa = f.subs(x, c)


        if evaluacion_directa.has(sp.nan) or evaluacion_directa.has(sp.zoo):

            f_simplificada = sp.cancel(f)
            limite_exacto = f_simplificada.subs(x,c)


            if limite_exacto.has(sp.nan) or limite_exacto.has(sp.zoo):
                limite_exacto = "No existe (Diverge)"
        else:

            limite_exacto = evaluacion_directa


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
        resultado_txt.insert("1.0", f"Función: {f}\nLímite cuando x -> {c}\n\nLímite exacto:\n{limite_exacto}\n\nAproximación:\n{limite_aprox}")
        resultado_txt.configure(state="disabled")
