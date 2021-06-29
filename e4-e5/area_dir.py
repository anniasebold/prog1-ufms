def areaDireita(M, O):
  soma = 0.0
  cont = 0
  n = len(M)

  for i in range(1, n - 1):
    coli = n - i if i <= 5 else i + 1
    for j in range(coli, n):
      soma += M[i][j]
      cont += 1

  return soma if O == "S" else soma / cont


def main():
  O = input()

  n = 4

  M = [[0] * n for i in range(n)] # cria uma matriz n x n
  for i in range(n):
    for j in range(n):
      M[i][j] = num

  #print(M)

  valor = areaDireita(M, O)
  print(f"{valor:.1f}")

main()