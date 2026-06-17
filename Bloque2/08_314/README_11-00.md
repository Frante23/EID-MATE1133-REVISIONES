# README - 11-00.py

## Descripción
Calculadora de límites en un solo archivo. La función `calcular` reúne lectura de datos, cálculo y graficación.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace la función `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (UI/UX) ¿Qué entradas lee `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
3. (Funcionalidad de la Aplicacion) ¿Qué validaciones realiza `calcular`?
   Respuesta: Debe comprobar que f(x) y h existan y puedan interpretarse antes de calcular. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
4. (Dominio del Codigo Fuente) ¿Dónde se transforma el texto en expresión matemática?
   Respuesta: El texto se transforma a expresion matematica usando SymPy antes de calcular. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
5. (Obtencion del Resultado) ¿Dónde se calcula el límite?
   Respuesta: El limite se calcula en la seccion que transforma la entrada con SymPy y llama a la funcion de calculo correspondiente. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
6. (Obtencion del Resultado) ¿Dónde se actualiza la etiqueta de resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (UI/UX) ¿Dónde se limpia la gráfica anterior?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
8. (Visualizacion Grafica) ¿Dónde se generan los puntos para graficar?
   Respuesta: Dibuja la funcion y sus elementos relevantes en la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
9. (Dominio del Codigo Fuente) ¿Dónde se dibuja la función?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
10. (Dominio del Codigo Fuente) ¿Dónde se marca el punto del límite?
   Respuesta: Dibuja una referencia visual en el punto o valor asociado al limite. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
11. (UI/UX) ¿Qué parte del archivo crea la ventana?
   Respuesta: Instancia la ventana principal donde se colocan todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (UI/UX) ¿Qué parte del archivo crea los campos de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
13. (Dominio del Codigo Fuente) ¿Qué parte del archivo crea el botón principal?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Dominio del Codigo Fuente) ¿Qué parte del archivo inicia el ciclo de la app?
   Respuesta: Inicia el bucle de eventos para que la ventana permanezca activa. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Obtencion del Resultado) ¿Qué responsabilidad debería separarse de `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué widgets de CustomTkinter aparecen?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Obtencion del Resultado) ¿Qué implica usar `from sympy import *`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
20. (Obtencion del Resultado) ¿Qué riesgo tiene importar todo desde SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
21. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
22. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
23. (Uso de Librerias y Restricciones) ¿Qué librería calcula expresiones simbólicas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
24. (Uso de Librerias y Restricciones) ¿Qué librería permite graficar puntos?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Uso de Librerias y Restricciones) ¿Qué librería construye la ventana?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
26. (Obtencion del Resultado) ¿Qué hace `limit` en SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
27. (Obtencion del Resultado) ¿Qué hace `sympify` en SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
28. (Visualizacion Grafica) ¿Qué problema puede ocurrir con valores no definidos en Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
29. (Visualizacion Grafica) ¿Qué dependencia conecta Matplotlib con Tkinter?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
30. (Uso de Librerias y Restricciones) ¿Qué librería usarías para mejorar validaciones matemáticas?
   Respuesta: Debe comprobar que f(x) y h existan y puedan interpretarse antes de calcular. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
