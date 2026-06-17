# Archivos que usan limit de SymPy

Este listado incluye llamadas reales detectadas con el parser de Python:

- `sp.limit(...)` cuando SymPy se importa como `import sympy as sp`.
- `limit(...)` cuando el archivo usa `from sympy import *` o `from sympy import limit`.

No cuenta comentarios ni texto dentro de strings.

Total de archivos con limit de SymPy: 13
Total de llamadas detectadas: 23

## Bloque1/cjp_08_317/8-20.py
- Linea 207 (limit importado desde sympy): `lim_izq = limit(expr, x, h_val, "-")`
- Linea 208 (limit importado desde sympy): `lim_der = limit(expr, x, h_val, "+")`

## Bloque1/cjp_08_317/8_40_hora/pruebas.py
- Linea 40 (limit importado desde sympy): `limite = limit(sin(x)/x, x, escribir_limite)`

## Bloque1/cjp_08_317/9-00.py
- Linea 66 (sp.limit): `limite_calculado = sp.limit(expresion, x, valor_h)`

## Bloque2/07_234/11_00.py
- Linea 114 (sp.limit): `resultado_limite =sp .limit (funcion_sympy ,x ,valor_h )`

## Bloque2/07_234/12_00.py
- Linea 84 (sp.limit): `limite =sp .limit (funcion_expr ,x ,valor )`

## Bloque2/08_314/10_40_hora/graficadora.py
- Linea 76 (sp.limit): `lim_izq_sym = sp.limit(funcion, x, h_val, '-')`
- Linea 82 (sp.limit): `lim_der_sym = sp.limit(funcion, x, h_val, '+')`

## Bloque2/08_314/10_40_hora/logica.py
- Linea 26 (sp.limit): `limite_resultado = sp.limit(funcion, x, h_val)`

## Bloque2/08_314/11-00.py
- Linea 176 (limit importado desde sympy): `resultado_final = limit(funcion, x, h)`
- Linea 188 (limit importado desde sympy): `limite_result = limit(funcion, x, h)`
- Linea 190 (limit importado desde sympy): `pasos += f"Límite por la izquierda = {limit(funcion, x, h, '-')}\n"`
- Linea 191 (limit importado desde sympy): `pasos += f"Límite por la derecha  = {limit(funcion, x, h, '+')}\n\n"`

## Bloque2/08_314/11-20.py
- Linea 267 (sp.limit): `lim_test = sp.limit(f, x_sym, 0)`

## Bloque2/08_314/11-40.py
- Linea 49 (sp.limit): `limite = sp.limit(funcion, x, h, dir="+")`
- Linea 59 (sp.limit): `limite = sp.limit(funcion, x, h, dir="-")`
- Linea 68 (sp.limit): `limite_derecha = sp.limit(funcion, x, h, dir="+")`
- Linea 69 (sp.limit): `limite_izquierda = sp.limit(funcion, x, h, dir="-")`

## Bloque2/08_314/12-00.py
- Linea 144 (sp.limit): `limite = sp.limit(funcion, x, h)`

## Bloque2/crc03-230/10-40.py
- Linea 110 (sp.limit): `return sp.limit(f, x, h, dir=dir_sym), pasos`
- Linea 150 (sp.limit): `return sp.limit(f, x, h, dir=dir_sym), pasos`

## Bloque2/crc03-230/11-00.py
- Linea 119 (sp.limit): `resultado_limite_sympy = sp.limit(f, x, h)`
- Linea 144 (sp.limit): `resultado_limite_sympy = sp.limit(f, x, h)`

## Archivos no analizados por error de sintaxis

- `Bloque1/cjp_08_317/8_40_hora/calculo.py`: expected 'except' or 'finally' block (<unknown>, line 63)
