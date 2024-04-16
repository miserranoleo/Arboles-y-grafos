import math

def biseccion(func, a, b, tolerancia=1e-6, max_iter=1000):
    iteraciones = 0
    while iteraciones < max_iter:
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tolerancia:
            return c, iteraciones
        iteraciones += 1
        if func(c) * func(a) > 0:
            a = c
        else:
            b = c
    return None, max_iter

def secante(func, x0, x1, tolerancia=1e-6, max_iter=1000):
    iteraciones = 0
    while iteraciones < max_iter:
        x2 = x1 - (func(x1) * (x1 - x0)) / (func(x1) - func(x0))
        if abs(x2 - x1) < tolerancia:
            return x2, iteraciones
        iteraciones += 1
        x0, x1 = x1, x2
    return None, max_iter

def newton_raphson(func, derivada, x0, tolerancia=1e-6, max_iter=1000):
    iteraciones = 0
    while iteraciones < max_iter:
        x1 = x0 - func(x0) / derivada(x0)
        if abs(x1 - x0) < tolerancia:
            return x1, iteraciones
        iteraciones += 1
        x0 = x1
    return None, max_iter

# Definir la ecuación y su derivada
def func(x):
    return x**3 - 2*x**2 + 4*x - 8

def derivada(x):
    return 3*x**2 - 4*x + 4

# Aplicar los métodos iterativos para encontrar la raíz
raiz_biseccion, iteraciones_biseccion = biseccion(func, 1, 3)
raiz_secante, iteraciones_secante = secante(func, 1, 3)
raiz_newton, iteraciones_newton = newton_raphson(func, derivada, 2)

# Imprimir los resultados
print("Raíz encontrada por el método de bisección:", raiz_biseccion)
print("Iteraciones necesarias para converger (bisección):", iteraciones_biseccion)
print("Raíz encontrada por el método de la secante:", raiz_secante)
print("Iteraciones necesarias para converger (secante):", iteraciones_secante)
print("Raíz encontrada por el método de Newton-Raphson:", raiz_newton)
print("Iteraciones necesarias para converger (Newton-Raphson):", iteraciones_newton)
