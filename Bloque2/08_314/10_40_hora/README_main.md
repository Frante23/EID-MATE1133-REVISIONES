# README - main.py

## Descripción
Archivo principal de la aplicación modular. Crea la ventana, configura apariencia y coordina navegación entre inicio y graficadora.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Visualizacion Grafica) ¿Qué hace `ir_a_graficadora`?
   Respuesta: Cambia la vista desde inicio hacia la graficadora. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
2. (Dominio del Codigo Fuente) ¿Qué hace `regresar_a_inicio`?
   Respuesta: Vuelve desde la graficadora a la pantalla inicial. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Dominio del Codigo Fuente) ¿Qué función muestra la pantalla inicial?
   Respuesta: Llama al constructor de la pantalla de inicio para mostrar la portada. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
4. (Visualizacion Grafica) ¿Qué función muestra la graficadora?
   Respuesta: Esa parte prepara o actualiza la representacion visual de la funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
5. (Dominio del Codigo Fuente) ¿Qué función elimina o reemplaza contenido anterior?
   Respuesta: Limpia el contenedor principal antes de cargar una nueva pantalla. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
6. (Dominio del Codigo Fuente) ¿Qué función actúa como callback de navegación?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
7. (UI/UX) ¿Qué parte del archivo crea la ventana principal?
   Respuesta: Instancia la ventana principal donde se colocan todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
8. (UI/UX) ¿Qué parte configura el tamaño de ventana?
   Respuesta: La ventana principal se crea al inicializar la aplicacion grafica y contiene todos los widgets. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
9. (Dominio del Codigo Fuente) ¿Qué parte configura el modo visual?
   Respuesta: Configura tema, apariencia o colores globales de la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
10. (Dominio del Codigo Fuente) ¿Qué parte inicia la primera pantalla?
   Respuesta: Carga la pantalla de inicio cuando se abre la aplicacion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
11. (Dominio del Codigo Fuente) ¿Qué parte inicia el `mainloop`?
   Respuesta: Inicia el bucle de eventos para que la ventana permanezca activa. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Dominio del Codigo Fuente) ¿Qué función depende de `crear_pantalla_inicio`?
   Respuesta: Construye la portada o pantalla inicial. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (Visualizacion Grafica) ¿Qué función depende de `crear_pantalla_graficadora`?
   Respuesta: Construye la pantalla donde se ingresan datos y se muestra la grafica. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
14. (Dominio del Codigo Fuente) ¿Qué función debería mantenerse simple?
   Respuesta: La funcion de navegacion principal debe mantenerse simple para no mezclar responsabilidades. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Dominio del Codigo Fuente) ¿Qué responsabilidad principal tiene este archivo?
   Respuesta: Coordina el flujo principal del archivo sin encargarse de detalles que pertenecen a otros modulos. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.

## Preguntas sobre librerías
16. (UI/UX) ¿Para qué se usa `customtkinter`?
   Respuesta: Se usa para construir una interfaz grafica moderna con ventanas, botones, entradas y paneles. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
17. (UI/UX) ¿Qué hace `ctk.CTk`?
   Respuesta: Es la ventana principal de una aplicacion hecha con CustomTkinter. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
18. (UI/UX) ¿Qué hace `ctk.set_appearance_mode`?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
19. (UI/UX) ¿Qué hace `ctk.set_default_color_theme`?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
20. (Justificacion y Analisis) ¿Qué se importa desde `inicio.py`?
   Respuesta: Permite manejar datos en memoria como si fueran archivos. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
21. (Visualizacion Grafica) ¿Qué se importa desde `graficadora.py`?
   Respuesta: Prepara o actualiza la representacion visual de la funcion. Criterio pauta: Debe explicar como la libreria permite graficar o validar visualmente el limite.
22. (Justificacion y Analisis) ¿Por qué se importan funciones de otros módulos?
   Respuesta: Permite manejar datos en memoria como si fueran archivos. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
23. (Uso de Librerias y Restricciones) ¿Qué librería crea la ventana principal?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
24. (Justificacion y Analisis) ¿Qué módulo crea la pantalla inicial?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
25. (Justificacion y Analisis) ¿Qué módulo crea la pantalla de cálculo?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
26. (Justificacion y Analisis) ¿Qué dependencia se encarga de la navegación visual?
   Respuesta: La libreria mencionada aporta una capacidad externa necesaria para interfaz, calculo o graficacion. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
27. (Justificacion y Analisis) ¿Qué problema puede ocurrir si falla un import local?
   Respuesta: La aplicacion no podra iniciar la pantalla que depende de ese modulo. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
28. (Justificacion y Analisis) ¿Qué ventaja tiene dividir la app en módulos?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
29. (Justificacion y Analisis) ¿Qué dependencia revisarías si la ventana no abre?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
30. (Justificacion y Analisis) ¿Qué módulo debería contener la lógica matemática en esta estructura?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
