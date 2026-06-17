# README - 11-20.py

## Descripción
Aplicación avanzada de análisis de límites con interfaz completa, detección trigonométrica, racionalización, análisis lateral, cálculo al infinito y navegación gráfica.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Dominio del Codigo Fuente) ¿Qué hace `linspace`?
   Respuesta: Genera valores igualmente espaciados para graficar. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
2. (Dominio del Codigo Fuente) ¿Qué hace `isinf`?
   Respuesta: Determina si un valor representa infinito. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Obtencion del Resultado) ¿Qué configura `AppLimites.__init__`?
   Respuesta: Configura el estado inicial de la clase o de la aplicacion. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
4. (Funcionalidad de la Aplicacion) ¿Qué hace `ejecutar_analisis`?
   Respuesta: Ejecuta el analisis completo del limite desde la interfaz. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
5. (Obtencion del Resultado) ¿Qué hace `detectar_limite_trigonometrico`?
   Respuesta: Reconoce identidades trigonometricas conocidas para resolver limites. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
6. (Dominio del Codigo Fuente) ¿Qué hace `racionalizar_correctamente`?
   Respuesta: Aplica racionalizacion para simplificar expresiones con raices. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
7. (Obtencion del Resultado) ¿Qué hace `analizar_limites_laterales_correctamente`?
   Respuesta: Calcula el comportamiento de la funcion por izquierda y por derecha. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Obtencion del Resultado) ¿Qué hace `calcular_infinito_correcto`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
9. (Visualizacion Grafica) ¿Qué hace `graficar`?
   Respuesta: Dibuja la funcion y sus elementos relevantes en la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
10. (Obtencion del Resultado) ¿Qué hace `calcular_limite_completo`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
11. (UI/UX) ¿Qué hace `mover_izquierda`?
   Respuesta: Desplaza la vista de la grafica hacia la izquierda. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (Dominio del Codigo Fuente) ¿Qué hace `mover_derecha`?
   Respuesta: Desplaza la vista de la grafica hacia la derecha. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Dominio del Codigo Fuente) ¿Qué hace `mover_arriba`?
   Respuesta: Desplaza la vista de la grafica hacia arriba. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Dominio del Codigo Fuente) ¿Qué hace `mover_abajo`?
   Respuesta: Desplaza la vista de la grafica hacia abajo. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Visualizacion Grafica) ¿Qué hace `actualizar_grafico`?
   Respuesta: Redibuja la grafica usando el estado actual de visualizacion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
18. (Justificacion y Analisis) ¿Para qué se usa `NavigationToolbar2Tk`?
   Respuesta: Agrega herramientas para mover, ampliar o guardar la grafica. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
19. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
21. (Justificacion y Analisis) ¿Para qué se usa `re`?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
22. (Justificacion y Analisis) ¿Para qué se usa `PIL.Image`?
   Respuesta: Permite crear o manipular imagenes. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
23. (Justificacion y Analisis) ¿Para qué se usa `ImageDraw`?
   Respuesta: Permite dibujar sobre imagenes creadas con PIL. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
24. (Justificacion y Analisis) ¿Para qué se usa `io`?
   Respuesta: Permite manejar datos en memoria como si fueran archivos. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
25. (Justificacion y Analisis) ¿Para qué se usa `math`?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
26. (Justificacion y Analisis) ¿Para qué se usa `traceback`?
   Respuesta: Ayuda a mostrar detalles tecnicos cuando ocurre un error. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
27. (Uso de Librerias y Restricciones) ¿Qué librería maneja el cálculo simbólico?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Uso de Librerias y Restricciones) ¿Qué librería maneja la interfaz visual?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
29. (Uso de Librerias y Restricciones) ¿Qué librería permite dibujar y navegar la gráfica?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
30. (Uso de Librerias y Restricciones) ¿Qué librería ayuda a diagnosticar errores internos?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
