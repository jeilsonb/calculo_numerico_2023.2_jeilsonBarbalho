# Escolher uma EDO de 1z ordem e resolver usando os métodos:
# 1) Método de Euler (3,0)
# 2) Método de Runge-kuta 4 ordem (5,0)
# 3) Comparar com a resposta exata da Equação Diferencial (1,0)
# 4) Imprimir os resultados em um gráfico (1,0)

# Código:

# 1) Método de Euler
import numpy as np
import matplotlib.pyplot as plt

def metodo_de_euler(f, x0, y0, h, n):
    y = y0
    x = x0
    xs = [x0]
    ys = [y0]
    for i in range(1, n+1):
        y = y + h * f(x, y)
        x = x + h
        xs.append(x)
        ys.append(y)
    return xs, ys

# Definição da função f(x, y)
def f(x, y):
    return -2 * x + 1

# Condição inicial
x0 = 0
y0 = 0

# Tamanho do passo
h = 0.1

# Número total de passos
n = 10

# Resolvendo a EDO usando o Método de Euler
xs, ys = metodo_de_euler(f, x0, y0, h, n)

# Plotando o gráfico
plt.plot(xs, ys, label='Solução aproximada')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução aproximada da EDO usando o Método de Euler')
plt.legend()
plt.grid(True)
plt.show()

# 2) Método de Runge-kuta 4 ordem
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, x0, y0, h, n):
    y = y0
    x = x0
    xs = [x0]
    ys = [y0]
    for i in range(1, n+1):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        xs.append(x)
        ys.append(y)
    return xs, ys

# Definição da função f(x, y)
def f(x, y):
    return -2 * x + 1

# Condição inicial
x0 = 0
y0 = 0

# Tamanho do passo
h = 0.1

# Número total de passos
n = 10

# Resolvendo a EDO usando o Método de Runge-Kutta de quarta ordem
xs, ys = runge_kutta_4(f, x0, y0, h, n)

# Plotando o gráfico
plt.plot(xs, ys, label='Solução aproximada')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Solução aproximada da EDO usando o Método de Runge-Kutta de quarta ordem')
plt.legend()
plt.grid(True)
plt.show()

# 3) Comparar com a resposta exata da Equação Diferencial
import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_4(f, x0, y0, h, n):
    y = y0
    x = x0
    xs = [x0]
    ys = [y0]
    for i in range(1, n+1):
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)
        y = y + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h
        xs.append(x)
        ys.append(y)
    return xs, ys

# Definição da função f(x, y)
def f(x, y):
    return -2 * x + 1

# Solução exata da EDO
def solucao_exata(x):
    return -x**2 + x

# Condição inicial
x0 = 0
y0 = 0

# Tamanho do passo
h = 0.1

# Número total de passos
n = 10

# Resolvendo a EDO usando o Método de Runge-Kutta de quarta ordem
xs, ys_aprox = runge_kutta_4(f, x0, y0, h, n)

# Calculando a solução exata nos mesmos pontos
ys_exata = [solucao_exata(x) for x in xs]

# Plotando o gráfico
plt.plot(xs, ys_exata, label='Solução exata', color='blue')
plt.plot(xs, ys_aprox, label='Solução aproximada (Runge-Kutta 4)', linestyle='--', color='red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparação entre a solução exata e a solução aproximada da EDO')
plt.legend()
plt.grid(True)
plt.show()
