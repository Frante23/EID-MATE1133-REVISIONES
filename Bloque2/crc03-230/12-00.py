# importaciones necesarias para la interfaz grafica el grafico y el calculo simbolico
import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sympy as sp
from tkinter import messagebox
# configuracion del tema de la ventana
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
# variables globales para el canvas y la figura del grafico
canvas_grafico = None
figura = None
def validar_entrada(funcion_texto, valor_texto):
    # verificamos que ninguno de los dos campos este vacio eliminando los espacios en blanco
    if funcion_texto.strip() == "" or valor_texto.strip() == "":
        return False, "Debes completar todos los campos."
    return True, ""
def es_indeterminado(valor):
    # retorna True si el valor no es un numero finito util como resultado de limite
    if valor is None:
        return True
    if valor in (sp.nan, sp.zoo):
        return True
    # is_finite retorna None cuando sympy no puede determinarlo
    # lo tratamos como indeterminado para ser conservadores
    if valor.is_finite is not True:
        return True
    return False
def calcular_limite(funcion_texto, valor_texto):
    # definimos la variable x como un simbolo matematico puro para el calculo algebraico
    x = sp.Symbol('x')
    try: #try para capturar cualquier error inesperado
        # convertimos los textos ingresados a expresiones simbolicas de sympy
        valor_h     = sp.sympify(valor_texto)
        funcion_sym = sp.sympify(funcion_texto)
        # PASO 1 sustitucion directa
        # reemplazamos x por el valor al que tiende usando subs de sympy
        # si f(a) existe y es finito entonces ese valor ES el limite
        # esto aplica cuando la funcion es continua en el punto
        if valor_h not in (sp.oo, -sp.oo): #si valor_h es infinito no tiene sentido hacer sustitucion directa
            sustitucion = funcion_sym.subs(x, valor_h) #reemplazamos x por el valor al que tiende usando subs de sympy
            resultado   = sp.simplify(sustitucion) #simplificamos el resultado para resolver casos como 0/1 o 1/0 que sympy no evalua directamente
            if not es_indeterminado(resultado): #si el resultado no es indeterminado entonces lo retornamos como limite
                return True, resultado, funcion_sym, valor_h #retornamos el resultado del limite junto con la funcion simbolica y el valor al que tiende para graficar despues
        # PASO 2 simplificacion algebraica para indeterminaciones del tipo 0/0
        # usamos cancel para cancelar factores comunes entre numerador y denominador
        # luego factorizamos y volvemos a intentar la sustitucion directa
        # este paso resuelve casos como (x^2 - 1)/(x - 1) cuando x tiende a 1
        funcion_cancelada   = sp.cancel(funcion_sym) #cancel elimina factores comunes entre el numerador y el denominador
        funcion_factorizada = sp.factor(funcion_cancelada)
        if valor_h not in (sp.oo, -sp.oo): #nuevamente solo tiene sentido hacer sustitucion directa si el valor al que tiende es finito
            sustitucion2 = funcion_factorizada.subs(x, valor_h) #reemplazamos x por el valor al que tiende usando subs de sympy
            resultado2   = sp.simplify(sustitucion2) #simplificamos el resultado para resolver casos como 0/1 o 1/0 que sympy no evalua directamente
            if not es_indeterminado(resultado2): #si el resultado no es indeterminado entonces lo retornamos como limite
                return True, resultado2, funcion_sym, valor_h #return para terminar la funcion y no seguir al paso 3 si ya se encontro un resultado
        # PASO 3 aproximacion numerica con ciclo de convergencia
        # si los pasos anteriores no resolvieron el limite usamos evaluacion numerica
        # la idea es acercarnos cada vez mas al punto y ver hacia donde converge f(x)
        if valor_h in (sp.oo, -sp.oo):
            # para limites en el infinito generamos una secuencia de puntos
            # cada vez mas grandes y verificamos que los valores de f converjan
            signo  = 1 if valor_h == sp.oo else -1 #definimos el signo de los puntos segun si el limite es positivo o negativo
            puntos = [signo * 10**k for k in range(4, 10)]  # 10000 hasta 1000000000
            valores_convergencia = [] #lista para almacenar los valores de f en cada punto de la secuencia y verificar convergencia
            for p in puntos: #para p en cada punto de la secuencia generada
                # ciclo que evalua f en cada punto de la secuencia
                try: 
                    val = float(funcion_sym.subs(x, p))
                    valores_convergencia.append(val)
                except Exception: #except para capturar cualquier error que pueda surgir al evaluar la funcion en puntos muy grandes o con indeterminaciones numericas, como overflow o division por cero, y asi evitar que la aplicacion se caiga,
                    # si no se puede evaluar en este punto simplemente lo saltamos
                    continue
            if len(valores_convergencia) < 2: #si no se pueden evaluar al menos dos puntos de la secuencia no podemos verificar la convergencia y por lo tanto no podemos determinar el limite
                return False, "No se pudo evaluar la funcion en el infinito", None, None #none para indicar que no se obtuvo un resultado valido del limite
            # verificamos convergencia comparando los ultimos valores del ciclo
            # si la diferencia entre dos evaluaciones consecutivas es muy pequeña convergio
            convergio = True #variable para indicar si la secuencia de valores converge o no, inicialmente asumimos que converge y luego verificamos
            for i in range(len(valores_convergencia) - 1): #para el rango de indices de la lista de valores de convergencia, menos uno porque vamos a comparar cada valor con el siguiente
                difference = abs(valores_convergencia[i + 1] - valores_convergencia[i]) #calculamos la diferencia absoluta entre el valor actual y el siguiente en la secuencia
                if difference > 1e-2: #si la diferencia es mayor a un umbral pequeño, por ejemplo 0.01, consideramos que no converge porque los valores no se estan acercando lo suficiente
                    convergio = False #por lo tanto, se actualiza la variable de convergencia a false para indicar que la secuencia no converge
                    break #sale del bucle
            if not convergio: #si la secuencia no converge, si los valores no se acercan a un valor suficiente, entonces no se puede determinar un limite en el infinito porque no se acerca a ningun valor especifico, por lo tanto retornamos un mensaje indicando que el limite no converge y posiblemente no exista
                return False, "El limite no converge posiblemente no existe", None, None
            resultado_num = valores_convergencia[-1] #el menos uno es para obtener el ultimo valor de la lista de valores de convergencia
        else: #else para limites finitos, si el valor al que tiende es un numero finito, entonces hacemos una aproximacion numerica acercandonos desde ambos lados del punto para verificar que los limites laterales coincidan y asi determinar el limite en ese punto
            # para limites finitos aproximamos desde ambos lados con un ciclo
            # reducimos h en cada iteracion para acercarnos mas al punto
            centro = float(valor_h) #float para convertir el valor que tiende a un numero float para hacer las operaciones de suma y resta con h, ya que valor_h es una expresion simbolica de sympy y necesitamos un numero flotante para hacer las aproximaciones numericas
            # ciclo de refinamiento: empezamos lejos y nos acercamos de a poco
            pasos_h      = [1e-3, 1e-4, 1e-5, 1e-6, 1e-7] #significa que se evaluara la funcion en puntos cada vez mas cercanos al valor que tiende
            val_izq_prev = None #el none significa que inicialmente no se ha podido evaluar la funcion en ningun punto, y se ira actualizando a medida que se puedan evaluar puntos mas cercanos al valor que tiende, para asi tener el valor mas cercano posible desde la izquierda y desde la derecha para verificar los limites laterales
            val_der_prev = None
            for h in pasos_h: #para la variable h en cada paso de refinamiento, que representa la distancia al valor que tiende, empezando por 0.001 y reduciendose hasta 0.0000001
                try:
                    val_izq = float(funcion_sym.subs(x, centro - h)) #evaluamos la funcion en el punto centro - h, que es un punto a la izquierda del valor que tiende, y convertimos el resultado a float para obtener un valor numerico aproximado, ya que funcion_sym.subs devuelve una expresion simbolica de sympy y necesitamos un numero flotante para comparar los limites laterales
                    val_der = float(funcion_sym.subs(x, centro + h)) #evaluamos la funcion en el punto centro + h, que es un punto a la derecha del valor que tiende, y convertimos el resultado a float para obtener un valor numerico aproximado, ya que funcion_sym.subs devuelve una expresion simbolica de sympy y necesitamos un numero flotante para comparar los limites laterales
                except Exception: #except para capturar cualquier error que pueda surgir al evaluar la funcion en puntos muy cercanos al valor que tiende, como indeterminaciones numericas, overflow o division por cero, y asi evitar que la aplicacion se caiga,
                    continue # si no se puede evaluar en este punto simplemente lo saltamos y seguimos con el siguiente valor de h para intentar evaluar en un punto un poco mas alejado, ya que a veces las funciones pueden tener indeterminaciones muy cercanas al valor que tiende pero se pueden evaluar un poco mas lejos
                # guardamos los valores de esta iteracion
                val_izq_prev = val_izq #actualizamos el valor previo desde la izquierda con el valor obtenido en esta iteracion, para asi tener el valor mas cercano posible desde la izquierda para verificar los limites laterales
                val_der_prev = val_der #actualizamos el valor previo desde la derecha con el valor obtenido en esta iteracion, para asi tener el valor mas cercano posible desde la derecha para verificar los limites laterales

            # si no se pudo evaluar en ninguna iteracion retornamos error
            if val_izq_prev is None or val_der_prev is None: #si despues de intentar evaluar en varios puntos cada vez mas cercanos al valor que tiende, no se pudo obtener un valor numerico valido ni desde la izquierda ni desde la derecha, entonces no se pudo determinar el limite por aproximacion numerica, por lo tanto retornamos un mensaje indicando que no se pudo evaluar numericamente la funcion
                return False, "No se pudo evaluar numericamente la funcion", None, None #none para indicar que no se obtuvo un resultado valido del limite

            # verificamos que los limites laterales coincidan
            # si la diferencia es grande el limite no existe desde ese punto
            if abs(val_der_prev - val_izq_prev) > 1e-4: #si la diferencia entre el valor obtenido desde la derecha y el valor obtenido desde la izquierda es mayor a un umbral pequeño, por ejemplo 0.0001, entonces consideramos que los limites laterales no coinciden lo suficiente como para determinar un limite en ese punto, por lo tanto retornamos un mensaje indicando que el limite no existe porque los limites laterales son distintos
                return False, "El limite no existe limites laterales distintos", None, None #none para indicar que no se obtuvo un resultado valido del limite

            # el resultado es el promedio de ambos lados
            resultado_num = (val_izq_prev + val_der_prev) / 2

        # convertimos el numero flotante a una expresion simbolica exacta
        # por ejemplo 0.5 se convierte en 1/2 y 1.4142 se convierte en sqrt(2)
        resultado = sp.nsimplify(resultado_num, rational=True, tolerance=1e-5)
        return True, resultado, funcion_sym, valor_h

    except Exception as error:
        return False, str(error), None, None


def limpiar_grafico():
    global canvas_grafico, figura
    # destruimos el widget del grafico anterior si existe para que no se superpongan en la interfaz
    if canvas_grafico is not None:
        canvas_grafico.get_tk_widget().destroy()
        canvas_grafico = None
    # cerramos la figura de matplotlib para liberar memoria ram del sistema
    if figura is not None:
        plt.close(figura)
        figura = None


def graficar_funcion(funcion_sym, valor_h, resultado_limite, frame_grafico):
    global canvas_grafico, figura
    limpiar_grafico()
    x = sp.Symbol('x')

    # definimos el rango del eje x segun si el limite es finito o infinito
    if valor_h in (sp.oo, -sp.oo):
        x_inicio, x_fin = (10, 200) if valor_h == sp.oo else (-200, -10)
    else:
        x_centro = float(valor_h)
        x_inicio = x_centro - 5
        x_fin    = x_centro + 5

    # recorremos el rango evaluando la funcion punto a punto
    puntos_x_validos = []
    puntos_y = []
    px   = x_inicio
    paso = 0.5 if valor_h in (sp.oo, -sp.oo) else 0.05

    while px <= x_fin:
        # saltamos la zona muy cercana al punto de tendencia para evitar discontinuidades
        cerca = valor_h not in (sp.oo, -sp.oo) and abs(px - float(valor_h)) <= 0.03
        if not cerca:
            try:
                valor_y = float(funcion_sym.subs(x, px))
                # descartamos valores demasiado grandes para no distorsionar el grafico
                if abs(valor_y) <= 1000:
                    puntos_x_validos.append(px)
                    puntos_y.append(valor_y)
            except:
                pass
        px += paso

    # creamos la figura con el tema de colores rosa oscuro adaptado a la estetica personalizada
    figura = plt.Figure(figsize=(6, 4), dpi=100)
    figura.patch.set_facecolor('#2d1b2e')
    ax = figura.add_subplot(111)
    ax.set_facecolor('#3a1f3c')
    ax.plot(puntos_x_validos, puntos_y,
            color='#ed93b1', linewidth=2,
            label=f'f(x) = {funcion_sym}')

    try:
        limite_float = float(resultado_limite)
        # marcamos el punto del limite si el valor es finito
        if valor_h not in (sp.oo, -sp.oo):
            ax.plot(float(valor_h), limite_float, 'o',
                    color='#ff6eb4', markersize=10,
                    markerfacecolor='#2d1b2e',
                    markeredgecolor='#ff6eb4',
                    markeredgewidth=2,
                    label=f'Limite = {resultado_limite}', zorder=5)
            ax.axvline(x=float(valor_h), color='#f4c0d1',
                       linestyle='--', alpha=0.4, linewidth=1)
        ax.axhline(y=limite_float, color='#f4c0d1',
                   linestyle='--', alpha=0.4, linewidth=1,
                   label=f'Limite = {resultado_limite}')
    except:
        pass

    # configuracion visual de ejes titulos y leyenda
    ax.set_title(f'f(x) = {funcion_sym}', color='#f4c0d1', fontsize=11, pad=10)
    ax.set_xlabel('x',    color='#c490c8')
    ax.set_ylabel('f(x)', color='#c490c8')
    ax.tick_params(colors='#c490c8')
    for spine in ax.spines.values():
        spine.set_color('#5c3060')
    ax.legend(facecolor='#4a1b4e', edgecolor='#993556',
              labelcolor='#f4c0d1', fontsize=9)
    ax.grid(True, alpha=0.2, color='#5c3060')
    figura.tight_layout()

    # incrustamos el grafico dentro del frame de la ventana
    canvas_grafico = FigureCanvasTkAgg(figura, master=frame_grafico)
    canvas_grafico.draw()
    canvas_grafico.get_tk_widget().pack(fill="both", expand=True, padx=5, pady=5)


def boton_calcular(entry_funcion, entry_valor, label_resultado, frame_grafico):
    texto_funcion = entry_funcion.get()
    texto_valor   = entry_valor.get()

    # validamos que los campos no esten vacios antes de procesar
    es_valido, mensaje_error = validar_entrada(texto_funcion, texto_valor)
    if not es_valido:
        messagebox.showerror("Error", mensaje_error)
        return

    # calculamos el limite con nuestra funcion principal
    exito, resultado, funcion_sym, valor_h = calcular_limite(texto_funcion, texto_valor)
    if not exito:
        messagebox.showerror("Error al calcular", f"No se pudo calcular el limite\n{resultado}")
        label_resultado.configure(text="Error al calcular", text_color="#ff6eb4")
        return

    # mostramos el resultado de la operacion en el label inferior
    label_resultado.configure(
        text=f"lim f(x) = {resultado}   (x -> {valor_h})",
        text_color="#ed93b1"
    )

    # graficamos la funcion evaluada
    try:
        graficar_funcion(funcion_sym, valor_h, resultado, frame_grafico)
    except Exception as e:
        messagebox.showwarning("Advertencia", f"Limite calculado pero error al graficar\n{e}")


def boton_limpiar(entry_funcion, entry_valor, label_resultado):
    # vaciamos los campos y restauramos el mensaje inicial por defecto
    entry_funcion.delete(0, "end")
    entry_valor.delete(0, "end")
    label_resultado.configure(
        text="Ingresa una funcion y presiona Calcular Limite",
        text_color="#9b6b9e"
    )
    limpiar_grafico()


def crear_ventana():
    # inicializamos el contenedor principal de la interfaz de customtkinter
    ventana = ctk.CTk()
    ventana.title("Calculadora de Limites")
    ventana.geometry("850x680")

    # titulo y subtitulo de la aplicacion
    ctk.CTkLabel(ventana, text="Calculadora de Limites",
                 font=ctk.CTkFont(size=20, weight="bold"),
                 text_color="#f4c0d1").pack(pady=(20, 3))
    ctk.CTkLabel(ventana, text="Calculo I - Ingenieria Civil Informatica",
                 font=ctk.CTkFont(size=12),
                 text_color="#9b6b9e").pack(pady=(0, 15))

    # frame con los campos de entrada de la funcion y el valor
    frame_entradas = ctk.CTkFrame(ventana, corner_radius=10,
                                  fg_color="#3a1f3c",
                                  border_color="#5c3060",
                                  border_width=1)
    frame_entradas.pack(padx=20, pady=5, fill="x")

    ctk.CTkLabel(frame_entradas, text="f(x):",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1").grid(row=0, column=0, padx=15, pady=12)
    entry_funcion = ctk.CTkEntry(frame_entradas, width=280,
                                 placeholder_text="Ej: (x**2 - 1)/(x - 1)",
                                 font=ctk.CTkFont(size=12),
                                 fg_color="#4a1b4e",
                                 border_color="#993556",
                                 text_color="#f4c0d1")
    entry_funcion.grid(row=0, column=1, padx=10, pady=12)

    ctk.CTkLabel(frame_entradas, text="x tiende a:",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1").grid(row=0, column=2, padx=15)
    entry_valor = ctk.CTkEntry(frame_entradas, width=120,
                               placeholder_text="Ej: 1, 0, oo",
                               font=ctk.CTkFont(size=12),
                               fg_color="#4a1b4e",
                               border_color="#993556",
                               text_color="#f4c0d1")
    entry_valor.grid(row=0, column=3, padx=10)

    # botones de calcular y limpiar posicionados horizontalmente
    frame_botones = ctk.CTkFrame(ventana, fg_color="transparent")
    frame_botones.pack(pady=10)

    ctk.CTkButton(frame_botones, text="Calcular Limite",
                  font=ctk.CTkFont(size=14, weight="bold"), height=40, width=200,
                  fg_color="#993556",
                  hover_color="#72243e",
                  corner_radius=8,
                  command=lambda: boton_calcular(entry_funcion, entry_valor,
                                                 label_resultado, frame_grafico)
                  ).grid(row=0, column=0, padx=15)

    ctk.CTkButton(frame_botones, text="Limpiar",
                  font=ctk.CTkFont(size=14), height=40, width=130,
                  fg_color="#5c3060",
                  hover_color="#4a1b4e",
                  corner_radius=8,
                  command=lambda: boton_limpiar(entry_funcion, entry_valor, label_resultado)
                  ).grid(row=0, column=1, padx=15)

    # label donde se muestra el resultado del limite procesado
    frame_resultado = ctk.CTkFrame(ventana, corner_radius=10, height=55,
                                   fg_color="#3a1f3c",
                                   border_color="#5c3060",
                                   border_width=1)
    frame_resultado.pack(padx=20, pady=5, fill="x")
    frame_resultado.pack_propagate(False)

    label_resultado = ctk.CTkLabel(frame_resultado,
                                   text="Ingresa una funcion y presiona Calcular Limite",
                                   font=ctk.CTkFont(size=14),
                                   text_color="#9b6b9e")
    label_resultado.pack(expand=True)

    # area donde se muestra el grafico de la funcion de forma dinamica
    ctk.CTkLabel(ventana, text="Grafica",
                 font=ctk.CTkFont(size=13, weight="bold"),
                 text_color="#f4c0d1",
                 anchor="w").pack(padx=25, pady=(5, 0), anchor="w")

    frame_grafico = ctk.CTkFrame(ventana, corner_radius=10,
                                 fg_color="#3a1f3c",
                                 border_color="#5c3060",
                                 border_width=1)
    frame_grafico.pack(padx=20, pady=(5, 10), fill="both", expand=True)

    # pie de pagina informativo con instrucciones de sintaxis de python
    ctk.CTkLabel(ventana, text="Usa ** para potencias   Ej: x**2   o   (x**3 - 8)/(x - 2)",
                 font=ctk.CTkFont(size=10),
                 text_color="#6b3d70").pack(pady=(0, 8))

    # ciclo infinito de escucha de eventos que mantiene activa la aplicacion
    ventana.mainloop()


if __name__ == "__main__":
    # ejecucion del metodo que levanta el entorno visual de usuario
    crear_ventana()