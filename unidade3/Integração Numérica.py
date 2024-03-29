# 1) Escolher uma função integrável não trivial (não quero função puramente polinomial)
# 2) apresentar o valor analítico de sua integral no intervalo a, b
# 3) Apresentar o valor da integração pelo método do retângulo, trapézio e Simpson
# 4) variar a quantidade de intervalos e comparar a eficiência dos métodos.

# A função f(x)=cos(x) como nossa função integrável não trivial.
# A integral de cos(x) no intervalo [a,b] é dada por:
# ∫
# a
# b

# cos(x)dx=sin(b)−sin(a)

# Código: 

import numpy as np

# Definindo a função
def f(x):
    return np.cos(x)

# Integral analítica
def integral_analitica(a, b):
    return np.sin(b) - np.sin(a)

# Método do Retângulo
def retangulo(f, a, b, n):
    dx = (b - a) / n
    integral = 0
    for i in range(n):
        x = a + i * dx
        integral += f(x)
    integral *= dx
    return integral

# Método do Trapézio
def trapezio(f, a, b, n):
    dx = (b - a) / n
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        x = a + i * dx
        integral += f(x)
    integral *= dx
    return integral

# Regra de Simpson
def simpson(f, a, b, n):
    dx = (b - a) / n
    integral = f(a) + f(b)
    for i in range(1, n, 2):
        x = a + i * dx
        integral += 4 * f(x)
    for i in range(2, n-1, 2):
        x = a + i * dx
        integral += 2 * f(x)
    integral *= dx / 3
    return integral

# Intervalo de integração
a = 0
b = np.pi/2

# Valor analítico da integral
integral_real = integral_analitica(a, b)
print("Valor analítico da integral:", integral_real)

# Testando os métodos de integração para diferentes números de intervalos
for n in [10, 50, 100, 500, 1000]:
    integral_retangulo = retangulo(f, a, b, n)
    integral_trapezio = trapezio(f, a, b, n)
    integral_simpson = simpson(f, a, b, n)
    
    print(f"\nNúmero de intervalos: {n}")
    print("Método do Retângulo:", integral_retangulo, "\nErro relativo:", abs((integral_real - integral_retangulo) / integral_real))
    print("\nMétodo do Trapézio:", integral_trapezio, "\nErro relativo:", abs((integral_real - integral_trapezio) / integral_real))
    print("\nRegra de Simpson:", integral_simpson, "\nErro relativo:", abs((integral_real - integral_simpson) / integral_real))

# Link do código: https://replit.com/@JeilsonBarbalho/Integracao-Numerica#main.py
