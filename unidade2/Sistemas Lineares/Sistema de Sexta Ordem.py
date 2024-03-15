import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, x0, omega=1.0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()
    x_antigo = x0.copy()
    iteracao = 0
    historico_jacobi = [x.copy()]

    while iteracao < max_iter:
        for i in range(n):
            soma = np.dot(A[i, :], x_antigo) - A[i, i] * x_antigo[i]
            x[i] = x_antigo[i] + omega * (b[i] - soma) / A[i, i]

        historico_jacobi.append(x.copy())

        if np.linalg.norm(x - x_antigo, ord=np.inf) < tol:
            return x, iteracao + 1, np.array(historico_jacobi)

        x_antigo = x.copy()
        iteracao += 1

    return x, iteracao, np.array(historico_jacobi)

def gauss_seidel(A, b, x0, omega=1.0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = x0.copy()
    iteracao = 0
    historico_gs = [x.copy()]

    while iteracao < max_iter:
        for i in range(n):
            soma1 = np.dot(A[i, :i], x[:i])
            soma2 = np.dot(A[i, i+1:], x[i+1:])
            x[i] = x[i] + omega * (b[i] - soma1 - soma2) / A[i, i]

        historico_gs.append(x.copy())

        if np.linalg.norm(x - x0, ord=np.inf) < tol:
            return x, iteracao + 1, np.array(historico_gs)

        x0 = x.copy()
        iteracao += 1

    return x, iteracao, np.array(historico_gs)

# Definindo o sistema de sexta ordem
A = np.array([[2, 1, -1, 3, 2, 1],
              [3, -2, 2, 4, 1, -3],
              [1, 3, -4, 1, 2, -1],
              [4, 2, 1, -5, -2, 4],
              [1, 2, 3, -1, 3, -2],
              [-2, 1, -4, 2, -1, 3]])

b = np.array([10, 5, 15, 20, 7, 3])

# Chute inicial para as soluções
x0 = np.zeros_like(b)

# Resolvendo com o método de Jacobi
solucao_jacobi, iteracoes_jacobi, historico_jacobi = jacobi(A, b, x0, omega=0.1)

# Resolvendo com o método de Gauss-Seidel
solucao_gs, iteracoes_gs, historico_gs = gauss_seidel(A, b, x0, omega=0.1)

# Plotando o gráfico de convergência
plt.figure(figsize=(10, 6))

# Gráfico para Jacobi
for i in range(len(historico_jacobi[0])):
    plt.plot(historico_jacobi[:, i], label=f'Jacobi - x{i + 1}')

# Gráfico para Gauss-Seidel
for i in range(len(historico_gs[0])):
    plt.plot(historico_gs[:, i], label=f'Gauss-Seidel - x{i + 1}', linestyle='--')

plt.title('Convergência de Jacobi e Gauss-Seidel')
plt.xlabel('Iteração')
plt.ylabel('Solução')
plt.legend()
plt.grid(True)
plt.show()

# Exibindo os resultados finais
print("Solução pelo método de Jacobi:")
print(solucao_jacobi)
print("Número de iterações:", iteracoes_jacobi)

print("\nSolução pelo método de Gauss-Seidel:")
print(solucao_gs)
print("Número de iterações:", iteracoes_gs)
