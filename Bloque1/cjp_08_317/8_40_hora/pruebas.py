import sympy as sp
from sympy import symbols
from sympy import expand, factor
from sympy import *




init_printing(use_unicode=True)


t, o = symbols('t o')
func= 5*t + 3**o
print("Funcion: ", func)

x, y = symbols('x y')
expr = x*(x + 2*y)
print("Ejercicio: ", expr)




print("\nhola: ", Eq(x + 1, 4))


expresion_expandida = expand(expr)
expresion_factorizada = factor(expr)
print("\nFuncion expandida: ", expresion_expandida)
print("\nFuncion factorizada: ", expresion_factorizada)


ocho = sp.sqrt(8)
print("\nRaiz cuadrada de 8: ", ocho)

nueve = sp.sqrt(9)
print("\nRaiz cuadrada de 9: ", nueve)


escribir_limite = int(input("Ingrese a qué número tiende x: "))
limite = limit(sin(x)/x, x, escribir_limite)
print("\nLimite es: ", limite)


print("\n valores de x para que se cumpla la operacion: ", solve(x**2 - 2, x))


a = cos(x)**2 - sin(x)**2
b = cos(2*x)
print("\n Es a igual a b?: ", a.equals(b))




print("\n División de enteros con sympy usando integer: ", Integer(1)/Integer(3))
print("División de enteros en python: ", 1/3)

print("\nUsando rational: ", Rational(1, 3))


a = (x + 1)**2
b = x**2 + 2*x + 1
c = x**2 - 2*x + 1
print("\n A menos B: ", simplify(a - b))
print("\n A menos C: ", simplify(a - c))

print("\n\nTrigonometria")



acos(x)

asin(x)


print("\n Sen al cuadrado + Cos al cuadrado: ", trigsimp(sin(x)**2 + cos(x)**2))





g, h = symbols('g h')
print("\nLOL: ", powsimp(x**g*x**h))



x = symbols('x')
funcion = sp.sin()
valor_x = int(input("Ingrese valor de x: "))
funcion_nueva = 0