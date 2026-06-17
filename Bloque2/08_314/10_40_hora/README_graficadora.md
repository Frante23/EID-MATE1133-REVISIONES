# README - graficadora.py

## Descripción
Pantalla de graficadora modular que muestra entradas, pasos, guía, gráfica y llama a la lógica matemática.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Visualizacion Grafica) ¿Qué hace `crear_pantalla_graficadora`?
   Respuesta: Construye la pantalla donde se ingresan datos y se muestra la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
2. (Visualizacion Grafica) ¿Qué widgets crea `crear_pantalla_graficadora`?
   Respuesta: Construye la pantalla donde se ingresan datos y se muestra la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
3. (Dominio del Codigo Fuente) ¿Qué hace `mostrar_pasos`?
   Respuesta: Muestra en pantalla el procedimiento del calculo. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
4. (Dominio del Codigo Fuente) ¿Qué datos recibe `mostrar_pasos`?
   Respuesta: Muestra en pantalla el procedimiento del calculo. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
5. (UI/UX) ¿Qué hace `abrir_guia`?
   Respuesta: Abre o muestra ayuda para usar la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
6. (UI/UX) ¿Qué hace `accion_limpiar`?
   Respuesta: Limpia entradas, resultados y grafica. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
7. (Obtencion del Resultado) ¿Qué hace `accion_calcular`?
   Respuesta: Lee entradas, calcula el limite y actualiza resultado y grafica. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Dominio del Codigo Fuente) ¿Qué función obtiene la función ingresada?
   Respuesta: Lee el campo de texto donde el usuario escribio la funcion matematica. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
9. (Dominio del Codigo Fuente) ¿Qué función obtiene la tendencia ingresada?
   Respuesta: La funcion de analisis lee h desde su campo de entrada para evaluar el limite en ese punto. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
10. (Obtencion del Resultado) ¿Qué función llama a `procesar_limite`?
   Respuesta: Procesa la funcion y la tendencia para entregar resultado y pasos. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
11. (Dominio del Codigo Fuente) ¿Qué función actualiza el cuadro de pasos?
   Respuesta: Escribe el procedimiento del calculo en el panel destinado a los pasos. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Dominio del Codigo Fuente) ¿Qué función actualiza la gráfica?
   Respuesta: Redibuja la grafica con la funcion y el resultado actual. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (UI/UX) ¿Qué función limpia la interfaz?
   Respuesta: Esa parte administra elementos visuales que el usuario ve o usa dentro de la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
14. (Dominio del Codigo Fuente) ¿Qué función abre información de ayuda?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Funcionalidad de la Aplicacion) ¿Qué función debería manejar mejor los errores?
   Respuesta: Si la entrada no es valida, el programa debe evitar errores criticos y mostrar un mensaje entendible. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
18. (Justificacion y Analisis) ¿Para qué se usa `math`?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
19. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
20. (Visualizacion Grafica) ¿Para qué se usa `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Justificacion y Analisis) ¿Para qué se usa `NavigationToolbar2Tk`?
   Respuesta: Agrega herramientas para mover, ampliar o guardar la grafica. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
22. (Justificacion y Analisis) ¿Qué función se importa desde `logica.py`?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
23. (Obtencion del Resultado) ¿Por qué conviene separar `procesar_limite` en otro archivo?
   Respuesta: Debe mostrarse el bloque donde se transforma la entrada y se obtiene el resultado del limite. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Uso de Librerias y Restricciones) ¿Qué librería crea los controles de la pantalla?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Uso de Librerias y Restricciones) ¿Qué librería dibuja la curva?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
26. (Uso de Librerias y Restricciones) ¿Qué librería permite manipular expresiones matemáticas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (Uso de Librerias y Restricciones) ¿Qué librería conecta Matplotlib con Tkinter?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Visualizacion Grafica) ¿Qué ventaja tiene la barra de navegación de Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
29. (Obtencion del Resultado) ¿Qué error puede ocurrir si `procesar_limite` devuelve datos inválidos?
   Respuesta: Devuelve el resultado procesado para que otra parte del programa lo muestre o use. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
30. (Justificacion y Analisis) ¿Qué dependencia revisarías si la gráfica no aparece?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
