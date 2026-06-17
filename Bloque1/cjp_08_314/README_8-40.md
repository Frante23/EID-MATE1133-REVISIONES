# README - 8-40.py

## Descripción
Programa gráfico para ingresar una función, calcular un límite y mostrar su gráfica.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Visualizacion Grafica) ¿Qué hace la función `crear_grafico`?
   Respuesta: Prepara la figura, los ejes y el contenedor donde se mostrara la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
2. (Visualizacion Grafica) ¿Qué objetos devuelve o configura `crear_grafico`?
   Respuesta: Prepara la figura, los ejes y el contenedor donde se mostrara la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
3. (Funcionalidad de la Aplicacion) ¿Qué hace la función `ejecutar_analsis`?
   Respuesta: Ejecuta el flujo principal de analisis: leer datos, calcular y mostrar resultados. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
4. (Funcionalidad de la Aplicacion) ¿Cómo obtiene `ejecutar_analsis` la función ingresada?
   Respuesta: Ejecuta el flujo principal de analisis: leer datos, calcular y mostrar resultados. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
5. (Funcionalidad de la Aplicacion) ¿Cómo obtiene `ejecutar_analsis` el valor de tendencia?
   Respuesta: La funcion de analisis lee h desde su campo de entrada para evaluar el limite en ese punto. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
6. (Funcionalidad de la Aplicacion) ¿Qué validaciones realiza antes de calcular?
   Respuesta: Debe comprobar que f(x) y h existan y puedan interpretarse antes de calcular. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
7. (Obtencion del Resultado) ¿Dónde se calcula el límite?
   Respuesta: El limite se calcula en la seccion que transforma la entrada con SymPy y llama a la funcion de calculo correspondiente. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Obtencion del Resultado) ¿Dónde se actualiza el texto del resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (Dominio del Codigo Fuente) ¿Dónde se actualiza la gráfica?
   Respuesta: Redibuja la grafica con la funcion y el resultado actual. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
10. (UI/UX) ¿Qué parte del código crea la ventana principal?
   Respuesta: Instancia la ventana principal donde se colocan todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
11. (UI/UX) ¿Qué parte del código crea los campos de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (Dominio del Codigo Fuente) ¿Qué parte del código crea el botón de cálculo?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (UI/UX) ¿Qué ocurre si la entrada no es válida?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
14. (UI/UX) ¿Cómo se limpia o reemplaza una gráfica anterior?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
15. (Dominio del Codigo Fuente) ¿Qué función concentra más responsabilidades?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué diferencia hay entre `CTk`, `CTkEntry`, `CTkButton` y `CTkLabel`?
   Respuesta: Es la ventana principal de una aplicacion hecha con CustomTkinter. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
19. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Visualizacion Grafica) ¿Por qué se importa Matplotlib dentro de una app de escritorio?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
22. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Obtencion del Resultado) ¿Qué errores puede lanzar SymPy con una expresión inválida?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
25. (Obtencion del Resultado) ¿Cómo se relaciona SymPy con la variable `x`?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
26. (Uso de Librerias y Restricciones) ¿Qué librería calcula el límite?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (Uso de Librerias y Restricciones) ¿Qué librería dibuja la curva?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Uso de Librerias y Restricciones) ¿Qué librería construye la interfaz?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
29. (Visualizacion Grafica) ¿Qué ventaja tiene usar Matplotlib en vez de dibujar manualmente?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
30. (UI/UX) ¿Qué dependencia habría que instalar si el programa no abre la interfaz?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
