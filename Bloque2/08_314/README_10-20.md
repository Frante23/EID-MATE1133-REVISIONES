# README - 10-20.py

## Descripción
Aplicación con pestañas de inicio y cálculo de límites usando CustomTkinter, SymPy y Matplotlib.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Dominio del Codigo Fuente) ¿Qué configura `App.__init__`?
   Respuesta: Configura el estado inicial de la clase o de la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
2. (Dominio del Codigo Fuente) ¿Qué crea `crear_inicio`?
   Respuesta: Construye la pantalla o pestana de inicio. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Visualizacion Grafica) ¿Qué hace `crea_grafico`?
   Respuesta: Prepara los elementos graficos necesarios para mostrar una funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
4. (Obtencion del Resultado) ¿Qué crea `crear_limite`?
   Respuesta: Construye la seccion donde se ingresa y calcula el limite. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
5. (Obtencion del Resultado) ¿Qué hace `procesar_limite`?
   Respuesta: Procesa la funcion y la tendencia para entregar resultado y pasos. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
6. (Dominio del Codigo Fuente) ¿Qué hace `mostrar_texto`?
   Respuesta: Muestra mensajes, resultados o pasos en un area de texto. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
7. (Dominio del Codigo Fuente) ¿Qué función obtiene la función ingresada?
   Respuesta: Lee el campo de texto donde el usuario escribio la funcion matematica. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
8. (Obtencion del Resultado) ¿Qué función obtiene el valor de tendencia?
   Respuesta: La funcion de analisis lee h desde su campo de entrada para evaluar el limite en ese punto. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (Obtencion del Resultado) ¿Qué función actualiza el resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
10. (Dominio del Codigo Fuente) ¿Qué función actualiza la gráfica?
   Respuesta: Redibuja la grafica con la funcion y el resultado actual. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
11. (Dominio del Codigo Fuente) ¿Qué función arma la pestaña de inicio?
   Respuesta: Construye los widgets y textos que forman esa pestana de la interfaz. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Dominio del Codigo Fuente) ¿Qué función arma la pestaña de límite?
   Respuesta: Construye los widgets y textos que forman esa pestana de la interfaz. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Dominio del Codigo Fuente) ¿Qué función concentra la lógica matemática?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Dominio del Codigo Fuente) ¿Qué función concentra la lógica visual?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Dominio del Codigo Fuente) ¿Qué función debería dividirse si el código creciera?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué aporta `CTkTabview` a la interfaz?
   Respuesta: Es la ventana principal de una aplicacion hecha con CustomTkinter. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Visualizacion Grafica) ¿Para qué se usa `Figure` de Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
19. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (UI/UX) ¿Cómo se incrusta una gráfica en CustomTkinter?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
21. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
22. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Obtencion del Resultado) ¿Qué representa `sp.Symbol`?
   Respuesta: Crea una variable simbolica, por ejemplo x. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
25. (Uso de Librerias y Restricciones) ¿Qué librería calcula el límite?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
26. (Uso de Librerias y Restricciones) ¿Qué librería muestra la interfaz?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (Uso de Librerias y Restricciones) ¿Qué librería dibuja la gráfica?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Obtencion del Resultado) ¿Qué error puede producir SymPy con texto inválido?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
29. (Visualizacion Grafica) ¿Qué ventaja tiene Matplotlib para este proyecto?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
30. (Justificacion y Analisis) ¿Qué dependencia habría que revisar si no aparece la ventana?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
