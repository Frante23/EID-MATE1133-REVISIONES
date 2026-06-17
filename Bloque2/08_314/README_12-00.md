# README - 12-00.py

## Descripción
Aplicación de cálculo de límites con interfaz gráfica donde la función `calcular` centraliza procesamiento y visualización.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace la función `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (UI/UX) ¿Qué datos lee `calcular` desde la interfaz?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
3. (UI/UX) ¿Dónde se valida la entrada del usuario?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
4. (Dominio del Codigo Fuente) ¿Dónde se convierte el texto a expresión matemática?
   Respuesta: El texto se transforma a expresion matematica usando SymPy antes de calcular. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
5. (Obtencion del Resultado) ¿Dónde se calcula el límite?
   Respuesta: El limite se calcula en la seccion que transforma la entrada con SymPy y llama a la funcion de calculo correspondiente. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
6. (Obtencion del Resultado) ¿Dónde se actualiza el resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (Dominio del Codigo Fuente) ¿Dónde se prepara la gráfica?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
8. (Dominio del Codigo Fuente) ¿Dónde se dibuja la función?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
9. (Funcionalidad de la Aplicacion) ¿Dónde se manejan errores?
   Respuesta: Captura excepciones o condiciones invalidas y muestra un mensaje comprensible. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
10. (UI/UX) ¿Qué parte crea la ventana principal?
   Respuesta: Instancia la ventana principal donde se colocan todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
11. (UI/UX) ¿Qué parte crea los campos de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (Dominio del Codigo Fuente) ¿Qué parte crea el botón de cálculo?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Obtencion del Resultado) ¿Qué parte crea el área de resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
14. (Dominio del Codigo Fuente) ¿Qué parte inicia la aplicación?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Obtencion del Resultado) ¿Qué responsabilidades mezcla `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
18. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
20. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
22. (Uso de Librerias y Restricciones) ¿Qué librería interpreta funciones matemáticas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
23. (Uso de Librerias y Restricciones) ¿Qué librería genera la gráfica?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
24. (Uso de Librerias y Restricciones) ¿Qué librería crea los componentes visuales?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Obtencion del Resultado) ¿Qué errores puede producir SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
26. (Visualizacion Grafica) ¿Qué errores puede mostrar Matplotlib si hay datos inválidos?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
27. (UI/UX) ¿Qué ventaja tiene CustomTkinter para una app educativa?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
28. (Obtencion del Resultado) ¿Qué ventaja tiene SymPy frente a una aproximación manual?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
29. (Visualizacion Grafica) ¿Qué ventaja tiene Matplotlib para explicar límites?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
30. (Justificacion y Analisis) ¿Qué dependencia revisarías si falla el cálculo simbólico?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
