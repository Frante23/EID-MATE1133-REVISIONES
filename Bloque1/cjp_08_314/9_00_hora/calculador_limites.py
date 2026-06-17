import sympy as sp

x = sp.symbols('x')

def evaluar_limite(funcion_str: str, valor: float):
    try:
        funcion = sp.sympify(funcion_str)
        resultado = funcion.subs(x, valor)
        resultado = float(resultado)
        return resultado
    except:
        return None
    
def evaluacion_directa(funcion_str: str, h: float):
    #     Intenta evaluar f(h) directamente.
    #   Retorna (resultado, pasos) donde:
    #   resultado es el valor numérico o None si es indeterminado
    #   pasos es una lista de strings con el proceso

    pasos = []
    pasos.append(f"Paso 1: Sustitucion Directa -> f({h})")

    resultado = evaluar_limite(funcion_str, h)

    if resultado is None:
        pasos.append(f"  f({h}) = Error al evaluar, forma indetermianda")
        return None, pasos
    
    funcion = sp.sympify(funcion_str)
    valor_simbolico = funcion.subs(x, h)

    if str(valor_simbolico) in ["nan", "zoo", "oo", "-oo"]:
        pasos.append(f"  f({h}) = {valor_simbolico} -> Forma Indeterminada")
        return None, pasos
    
    pasos.append(f"   f({h}) = {round(resultado, 6)}")
    pasos.append(f"   Sustitucion Directa Exitosa")
    return resultado, pasos

EPSILON = 1e-7

def limites_laterales(funcion_str: str, h: float):

    pasos = []
    pasos.append(f"Paso 4: Cálculo de límites laterales")
    pasos.append(f"   ¿Qué es ε? Es un número muy pequeño (ε = {EPSILON})")
    pasos.append(f"   Nos permite acercarnos a h sin llegar exactamente a h")
    pasos.append(f"")

    derecho  = evaluar_limite(funcion_str, h + EPSILON)
    izquierdo = evaluar_limite(funcion_str, h - EPSILON)

    pasos.append(f"   Límite por la derecha (x → {h}⁺):")
    pasos.append(f"   → Evaluamos f({h} + ε) = f({round(h + EPSILON, 10)})")
    if derecho is None:
        pasos.append(f"   → Resultado: No se puede evaluar")
    else:
        pasos.append(f"   → Resultado: f({round(h + EPSILON, 10)}) ≈ {round(derecho, 6)}")

    pasos.append(f"")
    pasos.append(f"   Límite por la izquierda (x → {h}⁻):")
    pasos.append(f"   → Evaluamos f({h} - ε) = f({round(h - EPSILON, 10)})")
    if izquierdo is None:
        pasos.append(f"   → Resultado: No se puede evaluar")
    else:
        pasos.append(f"   → Resultado: f({round(h - EPSILON, 10)}) ≈ {round(izquierdo, 6)}")

    return derecho, izquierdo, pasos

TOLERANCIA = 1e-4

def comparar_laterales(derecho, izquierdo, pasos):

    pasos.append(f"Paso 5: Comparación de límites laterales")

    if derecho is None or izquierdo is None:
        pasos.append(f"   → Uno o ambos laterales no existen")
        pasos.append(f"   → ∴ El límite NO EXISTE")
        return None, pasos

    diferencia = abs(derecho - izquierdo)
    pasos.append(f"   → lim⁺ = {round(derecho, 6)}")
    pasos.append(f"   → lim⁻ = {round(izquierdo, 6)}")
    pasos.append(f"   → Diferencia entre laterales: |{round(derecho,6)} - {round(izquierdo,6)}| = {round(diferencia, 10)}")
    pasos.append(f"")

    if diferencia < TOLERANCIA:
        resultado = round((derecho + izquierdo) / 2, 6)
        pasos.append(f"   → La diferencia es menor a la tolerancia ({TOLERANCIA})")
        pasos.append(f"   → lim⁺ ≈ lim⁻  →  El límite EXISTE")
        pasos.append(f"   → Resultado = ({round(derecho,6)} + {round(izquierdo,6)}) / 2 = {resultado}")
        return resultado, pasos
    else:
        pasos.append(f"   → La diferencia es mayor a la tolerancia ({TOLERANCIA})")
        pasos.append(f"   → lim⁺ ≠ lim⁻  →  El límite NO EXISTE")
        return None, pasos

# Intenta factorizar y simplificar la expresión para resolver la indeterminación.    
def intentar_factorizar(funcion_str: str, h: float):

    pasos = []
    pasos.append(f"Paso 3: Forma indeterminada → intentando factorizar")

    try:
        funcion = sp.sympify(funcion_str)
        numerador = sp.numer(funcion)
        denominador = sp.denom(funcion)

        pasos.append(f"   Expresión original:")
        pasos.append(f"   Numerador:    {numerador}")
        pasos.append(f"   Denominador:  {denominador}")

        # Analizar el numerador
        pasos.append(f"")
        pasos.append(f"   Analizando el numerador: {numerador}")
        num_factorizado = sp.factor(numerador)

        # Detectar tipo de factorización del numerador
        grado_num = sp.degree(numerador, x)
        if num_factorizado != numerador:
            if grado_num == 2:
                # Verificar si es diferencia de cuadrados: a² - b²
                coeficientes = sp.Poly(numerador, x).all_coeffs()
                if len(coeficientes) == 3 and coeficientes[1] == 0:
                    b = sp.sqrt(abs(coeficientes[2]))
                    pasos.append(f"   → Detectado: Diferencia de cuadrados")
                    pasos.append(f"   → Fórmula: a² - b² = (a - b)(a + b)")
                    pasos.append(f"   → Donde: a = x, b = {b}")
                else:
                    pasos.append(f"   → Detectado: Trinomio factorizable")
                    pasos.append(f"   → Buscando factores del trinomio...")
            else:
                pasos.append(f"   → Detectado: Expresión factorizable")
            pasos.append(f"   → Resultado: {num_factorizado}")
        else:
            pasos.append(f"   → El numerador no requiere factorización")

        # Analizar el denominador
        pasos.append(f"")
        pasos.append(f"   Analizando el denominador: {denominador}")
        den_factorizado = sp.factor(denominador)

        if den_factorizado != denominador:
            pasos.append(f"   → Detectado: Expresión factorizable")
            pasos.append(f"   → Resultado: {den_factorizado}")
        else:
            pasos.append(f"   → El denominador es lineal, no requiere factorización")

        # Cancelar factores comunes
        funcion_cancelada = sp.cancel(funcion)

        pasos.append(f"")
        pasos.append(f"   Cancelando factores comunes:")

        if funcion_cancelada == funcion:
            pasos.append(f"   → No se encontraron factores comunes para cancelar")
            return None, pasos

        # Detectar qué factor se canceló
        factores_num = sp.Mul.make_args(num_factorizado)
        factores_den = sp.Mul.make_args(den_factorizado)
        cancelados = [str(f) for f in factores_num if f in factores_den]

        if cancelados:
            for factor_cancelado in cancelados:
                pasos.append(f"   → El factor ({factor_cancelado}) aparece en numerador y denominador")
                pasos.append(f"   → Se cancela porque x ≠ {h} (tendemos a {h}, no somos {h})")

        pasos.append(f"")
        pasos.append(f"   → Expresión antes:      {num_factorizado} / {den_factorizado}")
        pasos.append(f"   → Expresión simplificada: {funcion_cancelada}")

        # Sustitución directa con expresión simplificada
        resultado_simplificado = float(funcion_cancelada.subs(x, h))
        pasos.append(f"")
        pasos.append(f"   Sustitución directa en expresión simplificada:")
        pasos.append(f"   → f({h}) = {funcion_cancelada} con x = {h}")
        pasos.append(f"   → f({h}) = {round(resultado_simplificado, 6)}")

        return str(funcion_cancelada), pasos

    except Exception as e:
        pasos.append(f"   No se pudo factorizar: {e}")
        return None, pasos

# Calcula el límite cuando x tiende a infinito o menos infinito
def limite_al_infinito(funcion_str: str, h: float):

    pasos = []
    signo = "∞" if h > 0 else "-∞"
    pasos.append(f"Paso 1: h = {signo} → Análisis al infinito")

    try:
        funcion = sp.sympify(funcion_str)
        numerador = sp.numer(funcion)
        denominador = sp.denom(funcion)

        pasos.append(f"   Expresión original:")
        pasos.append(f"   Numerador:   {numerador}")
        pasos.append(f"   Denominador: {denominador}")

        # Encontrar grados
        grado_num = sp.degree(numerador, x)
        grado_den = sp.degree(denominador, x)
        grado_max = max(grado_num, grado_den)

        pasos.append(f"")
        pasos.append(f"   Identificando grados:")
        pasos.append(f"   → Grado del numerador:   {grado_num}")
        pasos.append(f"   → Grado del denominador: {grado_den}")
        pasos.append(f"   → Potencia mayor: x^{grado_max}")

        # Dividir por la potencia mayor
        potencia_mayor = x ** grado_max
        num_dividido = sp.expand(numerador / potencia_mayor)
        den_dividido = sp.expand(denominador / potencia_mayor)

        pasos.append(f"")
        pasos.append(f"   Estrategia: dividir cada término por x^{grado_max}")
        pasos.append(f"   → Numerador término a término:")

        for term in sp.Add.make_args(sp.expand(numerador)):
            term_div = sp.simplify(term / potencia_mayor)
            pasos.append(f"      {term} / x^{grado_max} = {term_div}")

        pasos.append(f"   → Denominador término a término:")
        for term in sp.Add.make_args(sp.expand(denominador)):
            term_div = sp.simplify(term / potencia_mayor)
            pasos.append(f"      {term} / x^{grado_max} = {term_div}")

        pasos.append(f"")
        pasos.append(f"   Expresión después de dividir:")
        pasos.append(f"   → Numerador:   {num_dividido}")
        pasos.append(f"   → Denominador: {den_dividido}")

        # Evaluar cuando x → ∞
        pasos.append(f"")
        pasos.append(f"   Cuando x → {signo}, los términos con x en denominador → 0:")

        for term in sp.Add.make_args(num_dividido):
            if term.has(x):
                pasos.append(f"      {term} → 0")
        for term in sp.Add.make_args(den_dividido):
            if term.has(x):
                pasos.append(f"      {term} → 0")

        num_limite = num_dividido.subs(x, sp.oo if h > 0 else -sp.oo)
        den_limite = den_dividido.subs(x, sp.oo if h > 0 else -sp.oo)

        pasos.append(f"")
        pasos.append(f"   Sustituyendo x → {signo}:")
        pasos.append(f"   → Numerador   → {num_limite}")
        pasos.append(f"   → Denominador → {den_limite}")

        # Resultado final
        if den_limite == 0:
            pasos.append(f"   → Denominador → 0 → El límite es ∞")
            return "∞", pasos

        resultado = float(num_limite / den_limite)
        pasos.append(f"")
        pasos.append(f"   Resultado final:")
        pasos.append(f"   → {num_limite} / {den_limite} = {round(resultado, 6)}")

        return str(round(resultado, 6)), pasos

    except Exception as e:
        pasos.append(f"   No se pudo calcular: {e}")
        return "Error", pasos
    
# Detecta y resuelve límites trigonométricos conocidos.
def limite_trigonometrico(funcion_str: str, h: float):
    
    pasos = []
    pasos.append(f"Paso 2: Detectando identidades trigonométricas...")

    funcion = sp.sympify(funcion_str)
    funcion_str_lower = funcion_str.replace(" ", "").lower()

    # Aplica solo cuando h = 0
    if h != 0:
        pasos.append(f"   Las identidades trigonométricas aplican solo cuando x → 0")
        return None, [], False
    
    # Identidad 1: lim sen(x)/x = 1
    identidad1 = sp.sympify("sin(x)/x")
    if sp.sympify(funcion - identidad1) == 0 or funcion_str_lower == "sin(x)/x":
        pasos.append(f"   Identidad detectada: lim sen(x)/x cuando x → 0")
        pasos.append(f"   Aplicando identidad fundamental:")
        pasos.append(f"   lim sen(x)/x = 1  (identidad trigonométrica fundamental)")
        return "1", pasos, True
    
    # Identidad 2: lim (1-cos(x))/x = 0
    indentidad2 = sp.sympify("(1 - cos(x))/x")
    if sp.sympify(funcion - indentidad2) == 0 or funcion_str_lower == "(1 - cos(x))/x":
        pasos.append(f"   Identidad detectada: lim (1-cos(x))/x cuando x → 0")
        pasos.append(f"   Aplicando identidad:")
        pasos.append(f"   lim (1-cos(x))/x = 0  (identidad trigonométrica)")
        return "0", pasos, True
    
    # Identidad 3: lim tan(x)/x = 1
    identidad3 = sp.sympify("tan(x)/x")
    if sp.sympify(funcion - identidad3) == 0 or funcion_str_lower == "tan(x)/x":
        pasos.append(f"   Identidad detectada: lim tan(x)/x cuando x → 0")
        pasos.append(f"   Aplicando identidad:")
        pasos.append(f"   lim tan(x)/x = 1  (identidad trigonométrica)")
        return "1", pasos, True
    
    pasos.append(f"   No se reconoció ninguna identidad trigonométrica estándar")
    return None, pasos, False

def multiplicar_conjugado(funcion_str: str, h: float):

    pasos = []
    pasos.append(f"Paso 3: Raíz detectada → multiplicando por el conjugado")

    try:
        funcion = sp.sympify(funcion_str)
        numerador = sp.numer(funcion)
        denominador = sp.denom(funcion)

        pasos.append(f"   Expresión original:")
        pasos.append(f"   Numerador:   {numerador}")
        pasos.append(f"   Denominador: {denominador}")

        # Detectar si hay sqrt
        def tiene_raiz_term(term):
            return any(
                arg.is_Pow and arg.exp == sp.Rational(1, 2)
                for arg in sp.preorder_traversal(term)
            )

        tiene_raiz_num = any(
            arg.is_Pow and arg.exp == sp.Rational(1, 2)
            for arg in sp.preorder_traversal(numerador)
        )
        tiene_raiz_den = any(
            arg.is_Pow and arg.exp == sp.Rational(1, 2)
            for arg in sp.preorder_traversal(denominador)
        )

        if not tiene_raiz_num and not tiene_raiz_den:
            pasos.append(f"   No se encontraron raíces en la expresión")
            return None, pasos

        # Construir conjugado
        if tiene_raiz_num:
            base = sp.expand(numerador)
            conjugado = sp.nsimplify(-base + 2 * sum(
                term for term in sp.Add.make_args(base)
                if tiene_raiz_term(term)
            ))
        else:
            base = sp.expand(denominador)
            conjugado = sp.nsimplify(-base + 2 * sum(
                term for term in sp.Add.make_args(base)
                if tiene_raiz_term(term)
            ))

        pasos.append(f"")
        pasos.append(f"   Estrategia: multiplicar por el conjugado")
        pasos.append(f"   → El conjugado de ({numerador}) es ({conjugado})")
        pasos.append(f"   → Esto elimina la raíz usando: (a - b)(a + b) = a² - b²")

        # Mostrar la multiplicación
        pasos.append(f"")
        pasos.append(f"   Multiplicando numerador y denominador por ({conjugado}):")
        pasos.append(f"   → Numerador:   ({numerador}) × ({conjugado})")

        nuevo_num = sp.expand(numerador * conjugado)
        pasos.append(f"                = {nuevo_num}")

        pasos.append(f"   → Denominador: ({denominador}) × ({conjugado})")
        nuevo_den = sp.expand(denominador * conjugado)
        pasos.append(f"                = {nuevo_den}")

        # Simplificar
        nueva_funcion = sp.cancel(nuevo_num / nuevo_den)
        pasos.append(f"")
        pasos.append(f"   Simplificando la expresión resultante:")
        pasos.append(f"   → {nuevo_num} / {nuevo_den}")
        pasos.append(f"   → Cancelando factores comunes...")
        pasos.append(f"   → Expresión simplificada: {nueva_funcion}")

        # Sustitución directa
        resultado = float(nueva_funcion.subs(x, h))
        pasos.append(f"")
        pasos.append(f"   Sustitución directa en expresión simplificada:")
        pasos.append(f"   → f({h}) = {nueva_funcion} con x = {h}")
        pasos.append(f"   → f({h}) = {round(resultado, 6)}")

        return str(nueva_funcion), pasos

    except Exception as e:
        pasos.append(f"   No se pudo aplicar el conjugado: {e}")
        return None, pasos

# Función principal que coordina todo el cálculo.
def calcular_limite(funcion_str: str, h_str: str) -> dict:
    pasos = []
    pasos.append(f"═══════════════════════════════")
    pasos.append(f"  Calculando: lim f(x) cuando x → {h_str}")
    pasos.append(f"  f(x) = {funcion_str}")
    pasos.append(f"═══════════════════════════════")

    # Convertir h a número
    try:
        if h_str.strip() in ["oo", "inf", "∞"]:
            h = float('inf')
        elif h_str.strip() in ["-oo", "-inf", "-∞"]:
            h = float('-inf')
        else:
            h = float(h_str)
    except:
        return {
            "resultado": "Error",
            "pasos": ["Error: El valor de h no es válido"]
        }

    # Caso infinito → se maneja aparte
    # Caso infinito
    if h == float('inf') or h == float('-inf'):
        resultado, pasos_infinito = limite_al_infinito(funcion_str, h)
        pasos.extend(pasos_infinito)
        return {"resultado": resultado, "pasos": pasos}

    # Paso 1: sustitución directa
    resultado, pasos_sustitucion = evaluacion_directa(funcion_str, h)
    pasos.extend(pasos_sustitucion)

    if resultado is None:
        # Forma indeterminada → primero revisar trigonométricas
        pasos.append("→ Forma indeterminada detectada, analizando...")
        resultado_trig, pasos_trig, fue_resuelto = limite_trigonometrico(funcion_str, h)
        pasos.extend(pasos_trig)

        if fue_resuelto:
            return {"resultado": resultado_trig, "pasos": pasos}
        
        # Si no era trigonométrico → detectar raíces primero
        funcion_temp = sp.sympify(funcion_str)
        tiene_raiz = any(
            arg.is_Pow and arg.exp == sp.Rational(1, 2)
            for arg in sp.preorder_traversal(funcion_temp)
        )
        if tiene_raiz:
            expresion_simplificada, pasos_conjugado = multiplicar_conjugado(funcion_str, h)
            pasos.extend(pasos_conjugado)
            if expresion_simplificada is not None:
                funcion_str = expresion_simplificada
        else:
            # Sin raíces → intentar factorizar
            expresion_simplificada, pasos_factor = intentar_factorizar(funcion_str, h)
            pasos.extend(pasos_factor)
            if expresion_simplificada is not None:
                funcion_str = expresion_simplificada

    # Límites laterales
    derecho, izquierdo, pasos_laterales = limites_laterales(funcion_str, h)
    pasos.extend(pasos_laterales)

    # Comparar laterales
    pasos_comparacion = []
    resultado_final, pasos_comparacion = comparar_laterales(derecho, izquierdo, pasos_comparacion)
    pasos.extend(pasos_comparacion)

    return {"resultado": str(resultado_final), "pasos": pasos}

if __name__ == "__main__":
    print("\n--- Test conjugado ---")
    test = calcular_limite("(x**2 - 1)/(x - 1)", "1")
    for paso in test["pasos"]:
        print(paso)
    print("Resultado:", test["resultado"])