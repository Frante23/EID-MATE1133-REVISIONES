# README - 9-40.py

## Descripción
Aplicación con pantalla inicial y calculadora de límites con métodos numéricos, factorización, cálculo al infinito y gráfica.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Dominio del Codigo Fuente) ¿Qué hace `np_is_nan`?
   Respuesta: Verifica si un valor debe tratarse como no numerico. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
2. (Dominio del Codigo Fuente) ¿Qué configura `App.__init__`?
   Respuesta: Configura el estado inicial de la clase o de la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (UI/UX) ¿Qué crea `crear_interfaz_inicio`?
   Respuesta: Construye la pantalla inicial de la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
4. (Obtencion del Resultado) ¿Qué hace `mostrar_calculadora`?
   Respuesta: Cambia desde la pantalla inicial hacia la calculadora. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
5. (UI/UX) ¿Qué crea `crear_interfaz_calculadora`?
   Respuesta: Construye los campos, botones y paneles de la calculadora. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
6. (Desarrollo Analitico) ¿Qué intenta resolver `intentar_factorizacion`?
   Respuesta: Intenta simplificar la expresion mediante factorizacion para resolver indeterminaciones. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
7. (Obtencion del Resultado) ¿Qué calcula `calcular_limite_numerico`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Obtencion del Resultado) ¿Qué calcula `calcular_limite_infinito`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (Visualizacion Grafica) ¿Qué hace `calcular_y_graficar_limite`?
   Respuesta: Dibuja o actualiza la grafica usando los datos calculados. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
10. (Visualizacion Grafica) ¿Qué hace `crear_canvas`?
   Respuesta: Crea el lienzo donde se integra la grafica de Matplotlib. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
11. (Dominio del Codigo Fuente) ¿Qué hace `mostrar_texto`?
   Respuesta: Muestra mensajes, resultados o pasos en un area de texto. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Dominio del Codigo Fuente) ¿Qué hace `al_configurar_interior`?
   Respuesta: Ajusta el comportamiento o tamano de un contenedor interno. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Dominio del Codigo Fuente) ¿Qué función decide qué estrategia de cálculo usar?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Dominio del Codigo Fuente) ¿Qué función actualiza la gráfica?
   Respuesta: Redibuja la grafica con la funcion y el resultado actual. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (UI/UX) ¿Qué función muestra los resultados al usuario?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué widgets de CustomTkinter se usan para organizar la interfaz?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
19. (Visualizacion Grafica) ¿Para qué se usa `Figure` de Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Justificacion y Analisis) ¿Para qué se usa `math`?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
22. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Obtencion del Resultado) ¿Qué hace `sp.limit` o sus funciones relacionadas?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
25. (Justificacion y Analisis) ¿Para qué se importa `tkinter`?
   Respuesta: Es la base grafica sobre la que se apoya CustomTkinter. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
26. (Uso de Librerias y Restricciones) ¿Qué librería permite cálculos simbólicos?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (Uso de Librerias y Restricciones) ¿Qué librería permite cálculos numéricos simples?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Uso de Librerias y Restricciones) ¿Qué librería permite crear la ventana visual?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
29. (Uso de Librerias y Restricciones) ¿Qué librería permite incrustar gráficos?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
30. (Obtencion del Resultado) ¿Qué limitación tiene depender de aproximaciones numéricas con `math`?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
