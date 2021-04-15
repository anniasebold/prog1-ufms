a, b = input().split()
a = float(a)
b = float(b)

if a > b:
  if a % b == 0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")
elif a < b:
  if b % a == 0:
    print("Sao Multiplos")
  else:
    print("Nao sao Multiplos")