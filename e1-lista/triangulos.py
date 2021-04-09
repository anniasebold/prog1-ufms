a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)
meio = 0

if a > b:
  if b > c:
    a = a
    b = b
    c = c
  elif a > c:
    a = a
    meio = b
    b = c
    c = meio
  else:
    meio = a
    a = c 
    c = b
    b = meio 
elif b > c:
  if a > c:
    meio = a
    a = b
    b = meio
  else:
    meio = a
    a = b
    b = c
    c = meio
else:
  meio = a
  a = c
  c = meio

if a >= b + c:
  print("NAO FORMA TRIANGULO")
elif a**2 == (b ** 2) + (c ** 2):
  print("TRIANGULO RETANGULO")
else: 
  if a**2 > (b ** 2) + (c ** 2):
    print("TRIANGULO OBTUSANGULO")
  elif a**2 < (b ** 2) + (c ** 2):
    print("TRIANGULO ACUTANGULO")

  if a**2 == (b ** 2) + (c ** 2):
    print("TRIANGULO RETANGULO")
  elif a == b == c:
    print("TRIANGULO EQUILATERO")
  elif a == b or b == c or a == c:
    print("TRIANGULO ISOSCELES")
