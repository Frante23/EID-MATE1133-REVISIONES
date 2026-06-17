# README - 11-40.py

## Descripción
Calculadora de límites con funciones separadas para cálculo y generación de gráfico.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (UI/UX) ¿Qué entradas recibe `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
3. (Obtencion del Resultado) ¿Qué devuelve `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
4. (Visualizacion Grafica) ¿Qué hace `generar_grafico`?
   Respuesta: Construye o actualiza la visualizacion grafica de la funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
5. (Visualizacion Grafica) ¿Qué datos necesita `generar_grafico`?
   Respuesta: Construye o actualiza la visualizacion grafica de la funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
6. (Dominio del Codigo Fuente) ¿Dónde se transforma el texto en expresión matemática?
   Respuesta: El texto se transforma a expresion matematica usando SymPy antes de calcular. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
7. (Dominio del Codigo Fuente) ¿Dónde se interpreta la tendencia?
   Respuesta: Convierte el valor escrito para h en numero, infinito o expresion valida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
8. (Obtencion del Resultado) ¿Dónde se actualiza el resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (UI/UX) ¿Dónde se limpia o crea la figura?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
10. (Visualizacion Grafica) ¿Dónde se dibuja la curva?
   Respuesta: Traza la curva de la funcion sobre los ejes de Matplotlib. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
11. (UI/UX) ¿Qué parte del archivo crea la ventana?
   Respuesta: Instancia la ventana principal donde se colocan todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (Dominio del Codigo Fuente) ¿Qué parte del archivo crea los inputs?
   Respuesta: Crea las cajas donde el usuario escribe funcion y tendencia. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Dominio del Codigo Fuente) ¿Qué parte del archivo conecta botón y cálculo?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Dominio del Codigo Fuente) ¿Qué función contiene la lógica matemática principal?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Dominio del Codigo Fuente) ¿Qué función contiene la lógica de visualización principal?
   Respuesta: Contiene la preparacion y actualizacion de los elementos graficos de la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
18. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
20. (Obtencion del Resultado) ¿Qué representa la variable simbólica de SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
21. (Visualizacion Grafica) ¿Para qué se usa `Figure`?
   Respuesta: Representa la figura donde se dibujan los ejes y la grafica. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
22. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
23. (Uso de Librerias y Restricciones) ¿Qué librería crea los widgets?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
24. (Uso de Librerias y Restricciones) ¿Qué librería calcula el límite?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Uso de Librerias y Restricciones) ¿Qué librería genera la gráfica?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
26. (Justificacion y Analisis) ¿Qué error puede ocurrir con una expresión inválida?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
27. (Justificacion y Analisis) ¿Qué error puede ocurrir con una tendencia inválida?
   Respuesta: Si la entrada no es valida, el programa debe evitar errores criticos y mostrar un mensaje entendible. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
28. (UI/UX) ¿Qué ventaja tiene separar SymPy de la interfaz?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
29. (Visualizacion Grafica) ¿Qué ventaja tiene usar Matplotlib en lugar de texto solamente?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
30. (Justificacion y Analisis) ¿Qué dependencia se debe revisar si la gráfica no se muestra?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
