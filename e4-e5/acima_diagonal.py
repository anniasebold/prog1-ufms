def acimaDiagonal(M, O):
  soma = 0.0
  cont = 0
  n = len(M)

  for i in range(n-1):
    for j in range(i + 1, n):
      soma += M[i][j]
      cont += 1

  if O == "S":
    return soma
  else:
    return soma / cont

def main():
  O = input()

  n = 2

  M = [[0] * n for i in range(n)] # cria uma matriz n x n
  for i in range(n):
    for j in range(n):
      num = float(input())
      M[i][j] = num

  #print(M)

  valor = acimaDiagonal(M, O)

  print(f"{valor:.1f}")

main()
