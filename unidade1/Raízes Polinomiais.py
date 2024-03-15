# q(x) = 25x5 + 12x4 - 9x3 + 5x2 + x - 1

def q(x):
    return 25*x**5 + 12*x**4 - 9*x**3 + 5*x**2 + x - 1

def bissecao(a, b, tol=1e-6, max_iter=100):
    if q(a) * q(b) > 0:
        raise ValueError("A função não muda de sinal no intervalo [a, b].")
    iter_count = 0
    while (b - a) / 2 > tol and iter_count < max_iter:
        c = (a + b) / 2
        if q(c) == 0:
            return c  # Encontrou a raiz exata
        elif q(c) * q(a) < 0:
            b = c
        else:
            a = c
        iter_count += 1
    # Retornar o ponto médio do intervalo como uma aproximação da raiz
    return (a + b) / 2

# Exemplo de uso:
a = -1
b = 1
raiz_aproximada = bissecao(a, b)
print(f"\nAproximação da raiz: {raiz_aproximada}")
def q(x):
  return 25*x**5 + 12*x**4 - 9*x**3 + 5*x**2 + x - 1

def secante(x0, x1, tol=1e-6, max_iter=100):
  iter_count = 0

  while abs(q(x1)) > tol and iter_count < max_iter:
      # Aproximação da derivada pela diferença finita
      derivative_approx = (q(x1) - q(x0)) / (x1 - x0)

      # Atualização da próxima estimativa da raiz usando a fórmula da secante
      x2 = x1 - q(x1) / derivative_approx

      x0, x1 = x1, x2  # Atualizar valores para a próxima iteração
      iter_count += 1
  return x1

# Exemplo de uso:
x0 = -1
x1 = 1
raiz_aproximada = secante(x0, x1)
print(f"Aproximação da raiz: {raiz_aproximada}")

# Neste exemplo, a função q(x) representa o polinômio e a função secante(x0, x1) implementa o método da secante.
def q(x):
  return 25*x**5 + 12*x**4 - 9*x**3 + 5*x**2 + x - 1

def derivada_q(x):
  return 125*x**4 + 48*x**3 - 27*x**2 + 10*x + 1

def newton_raphson(x0, tol=1e-6, max_iter=100):
  iter_count = 0

  while abs(q(x0)) > tol and iter_count < max_iter:
      # Atualização da próxima estimativa da raiz usando a fórmula de Newton-Raphson
      x1 = x0 - q(x0) / derivada_q(x0)

      x0 = x1  # Atualizar valor para a próxima iteração
      iter_count += 1

  return x0

# Exemplo de uso:
x0 = 1  # Estimativa inicial
raiz_aproximada = newton_raphson(x0)
print(f"Aproximação da raiz: {raiz_aproximada}" + "\n")

# Neste exemplo, a função q(x) representa o polinômio e a função derivada q(x) calcula a derivada de q(x). 
# A função newton_raphson(x0) implementa o método de Newton-Raphson
