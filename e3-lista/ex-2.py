def leNumeros():
  n = int(input())
  m = list(map(int, input().split()))

  return n, m

def main(): 
  menor = 0
  posicao = 0
  temp = 0  

  n,m= leNumeros()

  for i in range(0, n):
    if i == 0:
      menor = m[i]
    if m[i] <= menor:
      menor = m[i]
      posicao = i

  print(f"Menor valor: {menor}")
  print(f"Posicao: {posicao}")

main()