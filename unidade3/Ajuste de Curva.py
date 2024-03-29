# 1) Reta que melhor se ajuste aos pontos;
# 2) Curva de segundo grau que melhor se ajuste aos pontos;
# 3) Curva trigonométrica que melhor se ajuste aos pontos;
# 4) Apresentar graficamente os resultados.

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Definindo os pontos de dados
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y = np.array([3, 6, 9, 12, 15, 18, 21, 24, 27, 30])

# Definindo as funções para ajustar aos dados
def linear(x, a, b):
    return a * x + b

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

def sine(x, a, b, c):
    return a * np.sin(b * x) + c

# Ajustando os modelos aos dados
popt_linear, _ = curve_fit(linear, x, y)
popt_quadratic, _ = curve_fit(quadratic, x, y)
popt_sine, _ = curve_fit(sine, x, y)

# Gerando pontos para plotagem das curvas ajustadas
x_fit = np.linspace(0, 11, 100)

# Plotando os pontos de dados
plt.scatter(x, y, label='Pontos de dados')

# Plotando as curvas ajustadas
plt.plot(x_fit, linear(x_fit, *popt_linear), 'r--', label='Reta de ajuste')
plt.plot(x_fit, quadratic(x_fit, *popt_quadratic), 'g--', label='Curva de segundo grau de ajuste')
plt.plot(x_fit, sine(x_fit, *popt_sine), 'b--', label='Curva trigonométrica de ajuste')

# Adicionando legenda e título
plt.legend()
plt.title('Ajuste de modelos aos dados fornecidos manualmente')
plt.xlabel('X')
plt.ylabel('Y')

# Exibindo o gráfico
plt.grid(True)
plt.show()

# Link do código: https://replit.com/@JeilsonBarbalho/Ajuste-de-Curva
