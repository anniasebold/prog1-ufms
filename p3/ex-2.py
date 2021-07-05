def calculaMatriz(n, M):
  l_aux = 0
  c_aux = 0
  aux = 1
  nlimite = 0 #Verifica se chegou ao numero de n para 
  entra = True #Verifica se varia entre linha ou coluna
  inverte = True 
  nInverte = 1 #Verifica se inverte
  for i in range (1, n**2+1):
    if entra:
      M[c_aux][l_aux] = i
      l_aux += nInverte
      nlimite += 1
      if nlimite == n:
        aux += 1
        entra = False
        nlimite = 0
        c_aux += nInverte
        l_aux -= nInverte
        n -= 1
    else:
      M[c_aux][l_aux] = i
      c_aux += nInverte
      nlimite += 1
      if nlimite == n:
        aux += 1
        entra = True
        nlimite = 0
        if inverte == True:
            nInverte = -1
            inverte = False
        else:
            nInverte = 1
            inverte = True
        l_aux += nInverte
        c_aux += nInverte
			
def imprimeM(n, M):
	n = len(M)
	T = len(str(n ** 2))
	for i in range(n):
		for j in range(n):
			fim = " " if j != n - 1 else ""
			print(f"{M[i][j]:>{T}}", end=fim)
		print("") # pula uma linha após imprimir uma linha inteira da matriz

	print("")

def main():
  n = int(input())
  M = [[0] * n for i in range(n)]
  calculaMatriz(n, M)
  imprimeM(n, M)

main()