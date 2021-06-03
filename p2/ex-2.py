n = list(map(int, input().split()))
somaMaior = 0
aux = 0

for i in range (0, len(n)):
  aux = 0
  if i == 0: 
    somaMaior += n[i]
  for j in range (i, len(n)):
    aux += n[j]
    if aux > somaMaior:
        somaMaior = aux
print(somaMaior)