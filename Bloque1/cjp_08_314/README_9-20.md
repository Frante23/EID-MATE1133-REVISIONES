# README - 9-20.py

## Descripción
Calculadora de límites con portada, botones de inserción, cálculo simbólico, análisis de asíntotas y gráfica.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace la clase `CalculadoraLimites`?
   Respuesta: Agrupa la interfaz y la logica principal de la calculadora de limites. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (Dominio del Codigo Fuente) ¿Qué configura `__init__`?
   Respuesta: Configura el estado inicial de la clase o de la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Dominio del Codigo Fuente) ¿Qué crea `crear_portada`?
   Respuesta: Construye la pantalla inicial o de presentacion del programa. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
4. (Visualizacion Grafica) ¿Qué hace `crear_canvas`?
   Respuesta: Crea el lienzo donde se integra la grafica de Matplotlib. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
5. (Dominio del Codigo Fuente) ¿Qué hace `insertar_en_funcion`?
   Respuesta: Inserta texto o simbolos en el campo de la funcion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
6. (Dominio del Codigo Fuente) ¿Qué hace `insertar_en_h`?
   Respuesta: Inserta texto o simbolos en el campo de la tendencia. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
7. (Obtencion del Resultado) ¿Qué hace `crear_calculadora_limites`?
   Respuesta: Construye la seccion de la interfaz dedicada al calculo de limites. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (UI/UX) ¿Qué hace `limpiar_y_escribir`?
   Respuesta: Limpia un campo o panel y luego escribe nuevo contenido. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
9. (Funcionalidad de la Aplicacion) ¿Qué ocurre en `ejecutar_calculo`?
   Respuesta: Inicia el calculo usando los datos actuales de la interfaz. Criterio pauta: Debe aportar a que la app permita ingresar f(x), ingresar h y calcular mediante boton sin errores criticos.
10. (Obtencion del Resultado) ¿Qué calcula `calcular_limites_logica`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
11. (Dominio del Codigo Fuente) ¿Qué analiza `analizar_asintotas`?
   Respuesta: Busca comportamientos de la funcion asociados a asintotas o discontinuidades. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Visualizacion Grafica) ¿Qué hace `graficar`?
   Respuesta: Dibuja la funcion y sus elementos relevantes en la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
13. (UI/UX) ¿Qué método conecta la interfaz con la lógica?
   Respuesta: Esa parte administra elementos visuales que el usuario ve o usa dentro de la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
14. (UI/UX) ¿Qué método modifica directamente los campos de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
15. (UI/UX) ¿Qué método debería probarse sin abrir la ventana?
   Respuesta: Debe probarse con entradas conocidas para confirmar que devuelve resultados correctos. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué widgets de CustomTkinter aparecen en esta calculadora?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Visualizacion Grafica) ¿Para qué sirve `Figure` de Matplotlib?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
19. (Visualizacion Grafica) ¿Para qué sirve `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Visualizacion Grafica) ¿Cómo se incrusta una figura de Matplotlib en la ventana?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
22. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Justificacion y Analisis) ¿Para qué se usa `re`?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
25. (Justificacion y Analisis) ¿Qué tipo de validaciones puede facilitar `re`?
   Respuesta: Debe comprobar que f(x) y h existan y puedan interpretarse antes de calcular. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
26. (Uso de Librerias y Restricciones) ¿Qué librería se encarga de las expresiones simbólicas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
27. (Uso de Librerias y Restricciones) ¿Qué librería se encarga del render gráfico?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
28. (Uso de Librerias y Restricciones) ¿Qué librería se encarga de la interfaz?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
29. (Obtencion del Resultado) ¿Qué problema puede ocurrir si `sympify` recibe texto mal escrito?
   Respuesta: Convierte cadenas de texto en expresiones matematicas manipulables por SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
30. (Visualizacion Grafica) ¿Qué ventaja tiene Matplotlib para visualizar límites?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
