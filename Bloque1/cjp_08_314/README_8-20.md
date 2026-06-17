# README - 8-20.py

## Descripción
Aplicación de cálculo y visualización de límites con CustomTkinter, SymPy y Matplotlib.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Dominio del Codigo Fuente) ¿Qué hace la función `parsear_funcion`?
   Respuesta: Convierte el texto ingresado por el usuario en una expresion matematica que el programa puede evaluar. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
2. (Dominio del Codigo Fuente) ¿Qué hace la función `parsear_h`?
   Respuesta: Convierte el valor de tendencia escrito por el usuario en un numero o en infinito cuando corresponde. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Obtencion del Resultado) ¿Qué hace `_formatear_resultado`?
   Respuesta: Prepara el resultado para mostrarlo de forma clara en la interfaz. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
4. (Dominio del Codigo Fuente) ¿Qué hace `_normalizar_numero`?
   Respuesta: Ajusta valores numericos para evitar formatos innecesarios o resultados poco legibles. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
5. (Obtencion del Resultado) ¿Qué calcula `_aproximacion_lateral`?
   Respuesta: Evalua la funcion cerca del punto por un lado para estimar el limite lateral. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
6. (Obtencion del Resultado) ¿Qué hace `_limite_por_aproximacion`?
   Respuesta: Compara aproximaciones laterales para estimar si el limite existe y cual es su valor. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (Obtencion del Resultado) ¿Qué devuelve `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Dominio del Codigo Fuente) ¿Qué hace `generar_puntos`?
   Respuesta: Crea listas de valores de x e y para dibujar la funcion en la grafica. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
9. (Visualizacion Grafica) ¿Qué construye `ventana_grafico`?
   Respuesta: Construye una ventana o area destinada a mostrar la grafica de la funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
10. (Obtencion del Resultado) ¿Qué inicializa `LimiteApp.__init__`?
   Respuesta: Inicializa la aplicacion, sus variables principales y la configuracion base de la ventana. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
11. (UI/UX) ¿Qué arma `_construir_layout`?
   Respuesta: Organiza la estructura visual principal de la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
12. (UI/UX) ¿Qué crea `_panel_izquierdo`?
   Respuesta: Crea el panel donde normalmente van entradas, botones y resultados. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
13. (Visualizacion Grafica) ¿Qué crea `_panel_grafico`?
   Respuesta: Crea el sector donde se muestra la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
14. (Obtencion del Resultado) ¿Qué hace `_accion_calcular`?
   Respuesta: Lee los datos del usuario, ejecuta el calculo y actualiza la interfaz. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
15. (Visualizacion Grafica) ¿Qué hace `_graficar`?
   Respuesta: Dibuja o actualiza la grafica usando los datos calculados. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter` en este archivo?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué widgets de CustomTkinter aparecen en la interfaz?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (Visualizacion Grafica) ¿Para qué se usa `matplotlib.pyplot`?
   Respuesta: Se usa para crear y configurar graficas de funciones. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
19. (Visualizacion Grafica) ¿Qué permite hacer `FigureCanvasTkAgg`?
   Respuesta: Conecta una figura de Matplotlib con una ventana basada en Tkinter o CustomTkinter. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
20. (Visualizacion Grafica) ¿Por qué Matplotlib necesita integrarse con Tkinter?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
21. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
22. (Obtencion del Resultado) ¿Qué representa `Symbol("x")` en SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Obtencion del Resultado) ¿Para qué sirve `sympify`?
   Respuesta: Convierte cadenas de texto en expresiones matematicas manipulables por SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Obtencion del Resultado) ¿Qué significan `zoo` y `nan` en SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
25. (Obtencion del Resultado) ¿Cómo ayuda SymPy a evaluar funciones matemáticas?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
26. (UI/UX) ¿Qué ventaja tiene CustomTkinter frente a Tkinter básico?
   Respuesta: Permite crear los controles visuales de la aplicacion con un estilo mas moderno que Tkinter clasico. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
27. (UI/UX) ¿Qué limitación tiene Matplotlib al graficar discontinuidades?
   Respuesta: Permite dibujar curvas, puntos, ejes y otros elementos graficos. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
28. (Obtencion del Resultado) ¿Qué riesgo tiene usar `sympify` con texto del usuario?
   Respuesta: Convierte cadenas de texto en expresiones matematicas manipulables por SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
29. (Justificacion y Analisis) ¿Qué dependencia se encarga del cálculo simbólico?
   Respuesta: La libreria mencionada aporta una capacidad externa necesaria para interfaz, calculo o graficacion. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
30. (Justificacion y Analisis) ¿Qué dependencia se encarga de mostrar la gráfica dentro de la ventana?
   Respuesta: La libreria mencionada aporta una capacidad externa necesaria para interfaz, calculo o graficacion. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
