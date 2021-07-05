def Caso1(n, M):
  print("Caso 1:")
  
  meio = n // 2
  M[0][meio] = 1
  numero = 2

  cima = n-1
  direita = meio+1
  aux_direita = direita
  aux_cima = cima
  M[cima][direita] = numero

  for i in range(2, n**2):
    numero += 1
    direita += 1
    cima -= 1

    if cima < 0:
      cima = n-1
    
    if direita >= n:
      direita = 0

    if M[cima][direita] == 0:
      M[cima][direita] = numero
      aux_cima = cima
      aux_direita = direita
    
    else:
      cima = aux_cima + 1
      direita = aux_direita
      M[cima][direita] = numero 
# =========================================

def Caso2(n, M):
  print("Caso 2:")

  numero = 1
  for i in range(n):
    for j in range(n):
      M[i][j] = numero
      numero += 1
  
  def aplicaFormula(M, n):
    M[i][j] = (n**2+1) - M[i][j]
  
  for i in range(n):
    for j in range(n):
      if i == j:
        aplicaFormula(M, n)
      elif i + j == n -1:
        aplicaFormula(M, n)


# =========================================

def Caso3(n, M):
  print("Caso 3:")

  # <CODIGO>

  # </CODIGO>

    
# =========================================


# == NÃO ALTERE ESTA FUNÇÃO ===============
def imprimeM(n, M):
  for i in range(n):
    for j in range(n):
      print(M[i][j], end="\t")
    print("")

		
# =========================================


# == NÃO ALTERE ESTA FUNÇÃO ===============
def main():
  # Leitura da entrada
  n = int(input())

  # Cria uma matriz quadrada de ordem n preenchida com 0's
  M = [[0] * n for i in range(n)]

  if n % 2 == 1:
    Caso1(n, M)
  elif n % 4 == 0:
    Caso2(n, M)
  else:
    Caso3(n, M)

  # Esta função não deve ser alterada.
  imprimeM(n, M)

main()
# =========================================