def calculamatriz(n, M):
  M_sec = []
  linha = [0]
  s_sub = "L"
  i = 0
  aux = 0
  aux2 = 0 
  while i < (((n-2)//4*2+1)):
    linha = [s_sub] * (((n-2)//4*2+1))
    M_sec.append(linha)
    if i == (n-2)//4:
        s_sub = "U"
        aux = i+1
    elif i == (n-2)//4+1:
        s_sub = "X"
    i += 1
  M_sec[aux-1][((n-2)//4*2+1)//2] = "U"
  M_sec[aux][((n-2)//4*2+1)//2] = "L"
  aux2 = 1
  linha = ((n-2)//4*2+1)//2
  coluna = 0
  for i in range (((n-2)//4*2+1)**2):
    if M_sec[coluna][linha] == "L":
      M[coluna*2][linha*2+1] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2+1] = aux2
      aux2 += 1
      M[coluna*2][linha*2] = aux2
      aux2 += 1
    elif M_sec[coluna][linha] == "U":
      M[coluna*2][linha*2] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2+1] = aux2
      aux2 += 1
      M[coluna*2][linha*2+1] = aux2
      aux2 += 1
    elif M_sec[coluna][linha] == "X":
      M[coluna*2][linha*2] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2+1] = aux2
      aux2 += 1
      M[coluna*2+1][linha*2] = aux2
      aux2 += 1
      M[coluna*2][linha*2+1] = aux2
      aux2 += 1
    linha_aux = linha
    coluna_aux = coluna
    linha += 1
    coluna -= 1
    if coluna < 0:
        coluna = ((n-2)//4*2+1) - 1
    if linha >= ((n-2)//4*2+1):
        linha = 0
    if M[coluna*2][linha*2] != 0:
        linha = linha_aux
        coluna = coluna_aux
        coluna += 1   
def imprimeM(n, M):
  for i in range(n):
    for j in range(n):
      print(M[i][j], end="\t")
    print("")

def main():
  n = int(input())
  M = [[0] * n for i in range(n)]
  calculamatriz(n, M)
  imprimeM(n, M)

main()