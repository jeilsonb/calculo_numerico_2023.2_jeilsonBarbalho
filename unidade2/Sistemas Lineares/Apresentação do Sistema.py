import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def calcular_determinante(matriz):
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
            matriz[0][1] * matriz[1][2] * matriz[2][0] +
            matriz[0][2] * matriz[1][0] * matriz[2][1] -
            matriz[0][2] * matriz[1][1] * matriz[2][0] -
            matriz[0][1] * matriz[1][0] * matriz[2][2] -
            matriz[0][0] * matriz[1][2] * matriz[2][1])

def resolver_sistema(A, b):
    Delta = calcular_determinante(A)

    if Delta != 0:
        x = calcular_determinante([[b[0], A[0][1], A[0][2]],
                                   [b[1], A[1][1], A[1][2]],
                                   [b[2], A[2][1], A[2][2]]]) / Delta

        y = calcular_determinante([[A[0][0], b[0], A[0][2]],
                                   [A[1][0], b[1], A[1][2]],
                                   [A[2][0], b[2], A[2][2]]]) / Delta

        z = calcular_determinante([[A[0][0], A[0][1], b[0]],
                                   [A[1][0], A[1][1], b[1]],
                                   [A[2][0], A[2][1], b[2]]]) / Delta
        return x, y, z
    else:
        print("O sistema pode não ter uma solução única (Delta = 0).")
        return None

# Definindo a matriz A e o vetor b
A = [[1, 2, 8], [3, 9, 7], [6, 6, 4]]
b = [1, 8, 1]

# Resolvendo o sistema
solucao = resolver_sistema(A, b)

# Exibindo as soluções
if solucao is not None:
    print("Solução do sistema:")
    print(f"x = {solucao[0]}")
    print(f"y = {solucao[1]}")
    print(f"z = {solucao[2]}")

    # Criando um gráfico 3D
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Adicionando o ponto da solução ao gráfico
    ax.scatter(solucao[0], solucao[1], solucao[2], color='red', marker='o', s=100, label='Solução')

    # Adicionando o plano definido pelas equações do sistema
    x = np.linspace(-2, 2, 10)
    y = np.linspace(-2, 2, 10)
    X, Y = np.meshgrid(x, y)
    Z = (1 - X - 2*Y) / 8
    ax.plot_surface(X, Y, Z, alpha=0.5, rstride=100, cstride=100, color='gray', label='Plano do Sistema')

    # Configurando rótulos
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Solução do Sistema Linear')

    # Adicionando uma legenda
    ax.legend()

    # Exibindo o gráfico
    plt.show()
