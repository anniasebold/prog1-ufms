def leitura():
  a = list(map(int, input().split()))
  b = list(map(int, input().split()))

  return a, b

def main():
  a, b = leitura()
  nsoma = 0
  n = 0
  resto = 0
  soma = []
  tamanhoVetor = len(a)
  somaFinal = []

  for i in range(tamanhoVetor-1, -1, -1):
    nsoma = (a[i]+b[i]+resto)%10
    resto = (a[i]+b[i]+resto)//10
    soma.append(nsoma)

  if 0 < resto:
    soma.append(resto) 

  for i in range(len(soma)-1, -1,-1):
    somaFinal.append(soma[i])

  for i in range(0, len(soma)):
    print(somaFinal[i], end = " ")

main()