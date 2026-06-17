# README - logica.py

## Descripción
Módulo de lógica matemática para procesar límites y entregar datos a la interfaz.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace `procesar_limite`?
   Respuesta: Procesa la funcion y la tendencia para entregar resultado y pasos. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (UI/UX) ¿Qué entradas recibe `procesar_limite`?
   Respuesta: Procesa la funcion y la tendencia para entregar resultado y pasos. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
3. (Obtencion del Resultado) ¿Qué devuelve `procesar_limite`?
   Respuesta: Procesa la funcion y la tendencia para entregar resultado y pasos. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
4. (Obtencion del Resultado) ¿Qué hace `calcular_limite_manual`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
5. (UI/UX) ¿Qué entradas recibe `calcular_limite_manual`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
6. (Obtencion del Resultado) ¿Qué pasos genera `calcular_limite_manual`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (UI/UX) ¿Qué función interpreta la expresión del usuario?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
8. (Dominio del Codigo Fuente) ¿Qué función interpreta la tendencia?
   Respuesta: Convierte el valor escrito para h en numero, infinito o expresion valida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
9. (UI/UX) ¿Qué función detecta errores de entrada?
   Respuesta: Los campos de entrada permiten escribir f(x) y h, que son requisitos explicitos de la pauta. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
10. (Visualizacion Grafica) ¿Qué función arma el resultado para la graficadora?
   Respuesta: Esa parte prepara o actualiza la representacion visual de la funcion. Criterio pauta: Debe aportar a mostrar claramente el comportamiento de la funcion cerca de h.
11. (Dominio del Codigo Fuente) ¿Qué función debería probarse con casos unitarios?
   Respuesta: Debe probarse con entradas conocidas para confirmar que devuelve resultados correctos. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Dominio del Codigo Fuente) ¿Qué función contiene más lógica matemática?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
13. (UI/UX) ¿Qué función separa la interfaz del cálculo?
   Respuesta: Esa parte administra elementos visuales que el usuario ve o usa dentro de la aplicacion. Criterio pauta: Debe contribuir a una interfaz ordenada, clara y facil de usar.
14. (Dominio del Codigo Fuente) ¿Qué función podría ampliarse para más casos?
   Respuesta: Debe se?alarse la seccion exacta del archivo y explicar su papel dentro del flujo entrada-calculo-salida. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
15. (Dominio del Codigo Fuente) ¿Qué función debería documentarse con ejemplos?
   Respuesta: La funcion principal deberia incluir ejemplos de entrada y salida esperada. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.

## Preguntas sobre librerías
16. (Obtencion del Resultado) ¿Para qué se usa `sympy`?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
17. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
18. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Justificacion y Analisis) ¿Qué representa `sp.oo`?
   Respuesta: Representa infinito positivo en SymPy. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
20. (Justificacion y Analisis) ¿Qué hace `sp.simplify`?
   Respuesta: Intenta reducir una expresion a una forma mas simple. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
21. (Justificacion y Analisis) ¿Para qué se usa `math`?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
22. (Obtencion del Resultado) ¿Qué diferencia hay entre cálculos de `math` y de SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
23. (Uso de Librerias y Restricciones) ¿Qué librería maneja expresiones simbólicas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
24. (Uso de Librerias y Restricciones) ¿Qué librería maneja operaciones numéricas básicas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
25. (Obtencion del Resultado) ¿Qué error puede producir SymPy con texto inválido?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
26. (Obtencion del Resultado) ¿Qué ventaja tiene SymPy para límites?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
27. (Obtencion del Resultado) ¿Qué limitación tiene `math` con expresiones simbólicas?
   Respuesta: Se usa para operaciones numericas comunes de Python. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
28. (Justificacion y Analisis) ¿Qué dependencia permite trabajar con infinito matemático?
   Respuesta: La libreria mencionada aporta una capacidad externa necesaria para interfaz, calculo o graficacion. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
29. (UI/UX) ¿Qué dependencia debería mantenerse fuera de la interfaz?
   Respuesta: La libreria mencionada aporta una capacidad externa necesaria para interfaz, calculo o graficacion. Criterio pauta: Debe explicar como la libreria ayuda a ordenar o controlar la interfaz.
30. (Uso de Librerias y Restricciones) ¿Qué librería usarías para agregar pruebas automáticas?
   Respuesta: Permite buscar patrones en texto mediante expresiones regulares. Criterio pauta: Debe justificar el uso de SymPy, CustomTkinter o Matplotlib cuando corresponda, respetando la prohibicion de NumPy.
