# README - calculador_limites.py

## Descripción
Módulo de lógica matemática para calcular límites y devolver resultado junto con pasos explicativos.

## Alineacion con la pauta
Estas preguntas estan sujetas a la rubrica de MATE1133: desarrollo analitico, obtencion del resultado, justificacion, funcionalidad, UI/UX, visualizacion grafica, uso de librerias/restricciones y dominio del codigo fuente.

## Preguntas sobre funciones del código
1. (Obtencion del Resultado) ¿Qué hace `evaluar_limite`?
   Respuesta: Evalua una funcion para obtener un limite o una aproximacion inicial. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
2. (Dominio del Codigo Fuente) ¿Qué hace `evaluacion_directa`?
   Respuesta: Sustituye directamente el valor de tendencia en la funcion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
3. (Obtencion del Resultado) ¿Qué calcula `limites_laterales`?
   Respuesta: Calcula el comportamiento de la funcion por izquierda y por derecha. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
4. (Desarrollo Analitico) ¿Qué hace `comparar_laterales`?
   Respuesta: Compara los laterales para decidir si el limite existe. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
5. (Desarrollo Analitico) ¿Qué intenta resolver `intentar_factorizar`?
   Respuesta: Busca simplificar una expresion factorizando numerador y denominador. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
6. (Obtencion del Resultado) ¿Qué hace `limite_al_infinito`?
   Respuesta: Resuelve limites cuando x tiende a infinito positivo o negativo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
7. (Obtencion del Resultado) ¿Qué reconoce `limite_trigonometrico`?
   Respuesta: Reconoce identidades trigonometricas conocidas para resolver limites. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
8. (Desarrollo Analitico) ¿Qué hace `multiplicar_conjugado`?
   Respuesta: Usa el conjugado para simplificar expresiones con raices. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
9. (Obtencion del Resultado) ¿Qué coordina `calcular_limite`?
   Respuesta: Coordina el calculo del limite y devuelve el resultado principal junto con la informacion necesaria. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.
10. (Desarrollo Analitico) ¿Qué hace la función interna `tiene_raiz_term`?
   Respuesta: Detecta si un termino contiene una raiz cuadrada. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
11. (Dominio del Codigo Fuente) ¿Qué función agrega pasos de sustitución directa?
   Respuesta: La funcion `evaluacion_directa` agrega los pasos donde se reemplaza h directamente en la funcion. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
12. (Desarrollo Analitico) ¿Qué función decide si el límite existe por laterales?
   Respuesta: La funcion `comparar_laterales` decide si el limite existe comparando los valores por izquierda y derecha. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
13. (Dominio del Codigo Fuente) ¿Qué función trabaja con numerador y denominador?
   Respuesta: La funcion de factorizacion trabaja con numerador y denominador para simplificar expresiones racionales. Criterio pauta: Debe poder ubicarse y explicarse con precision en el codigo durante la defensa.
14. (Desarrollo Analitico) ¿Qué función se usa cuando `h` es infinito?
   Respuesta: La funcion `limite_al_infinito` se usa cuando la tendencia es infinito positivo o negativo. Criterio pauta: Debe relacionarse con un paso matematico valido del calculo de limites.
15. (Obtencion del Resultado) ¿Qué función devuelve el diccionario final de resultado?
   Respuesta: El resultado se actualiza en la etiqueta o panel destinado a mostrar la salida del calculo. Criterio pauta: Debe ayudar a que el resultado del software coincida con el resultado exacto resuelto a mano.

## Preguntas sobre librerías
16. (Obtencion del Resultado) ¿Para qué se usa `sympy` en este módulo?
   Respuesta: Se usa para trabajar con expresiones matematicas simbolicas y calcular limites. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
17. (Obtencion del Resultado) ¿Qué representa `sp.Symbol("x")`?
   Respuesta: Crea una variable simbolica, por ejemplo x. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
18. (Obtencion del Resultado) ¿Qué hace `sp.sympify`?
   Respuesta: Convierte texto en una expresion matematica de SymPy. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
19. (Justificacion y Analisis) ¿Qué hace `sp.simplify`?
   Respuesta: Intenta reducir una expresion a una forma mas simple. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
20. (Obtencion del Resultado) ¿Qué hace `sp.limit`?
   Respuesta: Calcula simbolicamente el limite de una expresion. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
21. (Justificacion y Analisis) ¿Qué hace `sp.factor`?
   Respuesta: Factoriza una expresion algebraica. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
22. (Justificacion y Analisis) ¿Qué hace `sp.cancel`?
   Respuesta: Cancela factores comunes en expresiones racionales. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
23. (Obtencion del Resultado) ¿Qué hace `as_numer_denom` en una expresión SymPy?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
24. (Justificacion y Analisis) ¿Qué representa `sp.oo`?
   Respuesta: Representa infinito positivo en SymPy. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
25. (Justificacion y Analisis) ¿Qué representa `sp.nan`?
   Respuesta: Representa un resultado no definido numericamente. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
26. (Justificacion y Analisis) ¿Qué representa `sp.zoo`?
   Respuesta: Representa infinito complejo, comun en divisiones por cero. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
27. (Justificacion y Analisis) ¿Para qué sirve `sp.degree`?
   Respuesta: Obtiene el grado de un polinomio. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
28. (Justificacion y Analisis) ¿Para qué sirve `sp.Poly`?
   Respuesta: Convierte una expresion en polinomio para analizar grados y coeficientes. Criterio pauta: Debe justificar por que la libreria es necesaria segun la pauta y no solo por comodidad.
29. (Obtencion del Resultado) ¿Qué ventaja tiene usar SymPy en vez de solo aproximaciones decimales?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
30. (Obtencion del Resultado) ¿Qué limitación puede tener SymPy con expresiones escritas por el usuario?
   Respuesta: Permite interpretar funciones, simplificar expresiones y resolver limites de forma simbolica. Criterio pauta: Debe explicar como la libreria ayuda a calcular o validar el resultado matematico.
