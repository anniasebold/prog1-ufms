def troca(v):
  j = 19
  for i in range(10):
    temp = v[j]
    v[j] = v[i]
    v[i] = temp
    j = j -1

def imprime(v):
  for i in range(20):
    print(f"N[{i}] = {v[i]}")

def main():
  vet = []
  for i in range(20):
    num = int(input())
    vet.append(num)
    
  troca(vet)
  imprime(vet)

main()