v = list(map(int, input().split()))
menor = v[0]

for i in range(0, len(v)):
  if v[i] < menor:
    menor = v[i]
    print(ordenado)
  

print(menor)
print(v)