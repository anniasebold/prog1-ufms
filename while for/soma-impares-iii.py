n = int(input())

for t in range(n):
  x,y = input().split()
  x = int(x)
  y = int(y)
  soma = 0

  if x % 2 == 0:
    x += 1

  for i in range(y):
    soma += x
    x += 2

  print(soma)