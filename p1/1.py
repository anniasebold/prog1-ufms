n = int(input())

if n == 0:
  print(0)
elif n == 1 or n == 2:
  print(1)
else:
  maior = 1
  maior2 = 1
  for i in range(3, n+1):
    f = maior + maior2
    maior2 = maior
    maior = f
    i += 1
  print(f)