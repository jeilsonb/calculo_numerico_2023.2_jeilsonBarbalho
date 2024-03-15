# A = [[1,2,8],[3,9,7],[6,6,4]] b = [1,8,1]

def calcular_determinante(matriz):
    # Calcula o determinante de uma matriz 3x3
    return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
            matriz[0][1] * matriz[1][2] * matriz[2][0] +
            matriz[0][2] * matriz[1][0] * matriz[2][1] -
            matriz[0][2] * matriz[1][1] * matriz[2][0] -
            matriz[0][1] * matriz[1][0] * matriz[2][2] -
            matriz[0][0] * matriz[1][2] * matriz[2][1])

def resolver_sistema(A, b):
    # Calcula o determinante principal Delta
    Delta = calcular_determinante(A)

    if Delta != 0:
        # Inicializa as soluções
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
    print("\nSolução do sistema:")
    print(f"x = {solucao[0]}")
    print(f"y = {solucao[1]}")
    print(f"z = {solucao[2]}" + "\n")
