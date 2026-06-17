# README - mathlimites.py

## Descripción
Interfaz gráfica de Math Límites. Usa `calculador_limites.py` para la lógica y Matplotlib para la visualización.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué configura `MathLimites.__init__`?
   Respuesta: Configura el estado inicial de la clase o de la aplicacion. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (Visualizacion Grafica) ¿Qué hace `setup_grafica`?
   Respuesta: Configura la figura y los ejes iniciales de la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
3. (Dominio del Codigo Fuente) ¿Qué hace `abrir_sidebar`?
   Respuesta: Muestra o expande el menu lateral. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
4. (Dominio del Codigo Fuente) ¿Qué hace `cerrar_sidebar`?
   Respuesta: Oculta o contrae el menu lateral. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
5. (Dominio del Codigo Fuente) ¿Qué hace `seleccionar`?
   Respuesta: Cambia la opcion o seccion seleccionada en la interfaz. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
6. (Obtencion del Resultado) ¿Qué ocurre en `calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (Visualizacion Grafica) ¿Qué hace `graficar`?
   Respuesta: Dibuja la funcion y sus elementos relevantes en la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
8. (Obtencion del Resultado) ¿Qué hace `mostrar_resultado`?
   Respuesta: Presenta el resultado y los pasos al usuario. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (UI/UX) ¿Qué método obtiene los valores escritos por el usuario?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
10. (Obtencion del Resultado) ¿Qué método llama a `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
11. (Obtencion del Resultado) ¿Qué método actualiza el panel de resultados?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
12. (Dominio del Codigo Fuente) ¿Qué método modifica el estado visual del sidebar?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Visualizacion Grafica) ¿Qué método prepara los ejes de la gráfica?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
14. (Dominio del Codigo Fuente) ¿Qué método responde al cálculo principal?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (UI/UX) ¿Qué método debería manejar errores de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué widgets de CustomTkinter forman la interfaz?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Obtencion del Resultado) ¿Para qué se usa `sympy` en este archivo?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Visualizacion Grafica) ¿Para qué sirve `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Visualizacion Grafica) ¿Para qué sirve `Figure` de Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
22. (Obtencion del Resultado) ¿Qué función se importa desde `calculador_limites`?
   Respuesta: Debe mostrarse el bloque donde se transforma la entrada y se obtiene el resultado del limite. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Justificacion y Analisis) ¿Por qué conviene importar la lógica desde otro archivo?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
24. (Uso de Librerias y Restricciones) ¿Qué librería dibuja la curva?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Uso de Librerias y Restricciones) ¿Qué librería crea la ventana?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
26. (Uso de Librerias y Restricciones) ¿Qué librería interpreta funciones matemáticas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (UI/UX) ¿Qué ventaja tiene separar CustomTkinter de SymPy?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
28. (Visualizacion Grafica) ¿Qué problema puede ocurrir si Matplotlib recibe valores no reales?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
29. (Obtencion del Resultado) ¿Qué problema puede ocurrir si SymPy no interpreta la función?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
30. (Visualizacion Grafica) ¿Qué dependencia conecta Matplotlib con Tkinter?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
