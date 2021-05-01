n = int(input())

count1 = 1
count2 = 1

for i in range(1, n+1):
  numero = int(input())

  if i == 1:
    ultimo = numero
    if  ultimo > numero:
        count1 += 1
    if count1 > count2:
      count2 = count1

  ultimo = numero

print(count1)
print(count2)