def Caso1(n, M):
  print("Caso 1:")
  
  meio = n // 2
  M[0][meio] = 1

  direita = 1
  cima = 0
  aux_direita = 1
  aux_cima = 0
  numero = 1

  for i in range(1, n**2):
    numero += 1
    if i == 1:
      cima = n-1
      direita = meio+1
      M[cima][direita] = numero

      aux_cima = cima
      aux_direita = direita
    else:
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

  # <CODIGO>
  print("entrou caso 2")

	# </CODIGO>


# =========================================


def Caso3(n, M):
  print("Caso 3:")

  # <CODIGO>
  print("entrou caso 3")

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