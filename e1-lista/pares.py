a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

par = 0
impar = 0
positivo = 0 
negativo = 0

if a % 2 == 0:
  par = par + 1 
elif a % 2 != 0 and a != 0:
  impar = impar + 1
if a < 0:
  negativo = negativo + 1
elif a > 0 and a != 0:
  positivo = positivo + 1

if b % 2 == 0:
  par = par + 1 
elif b % 2 != 0 and b != 0:
  impar = impar + 1
if b < 0:
  negativo = negativo + 1
elif b > 0 and b != 0:
  positivo = positivo + 1

if c % 2 == 0:
  par = par + 1 
elif c % 2 != 0 and c != 0:
  impar = impar + 1
if c < 0:
  negativo = negativo + 1
elif c > 0 and c != 0:
  positivo = positivo + 1

if d % 2 == 0:
  par = par + 1 
elif d % 2 != 0 and d != 0:
  impar = impar + 1
if d < 0:
  negativo = negativo + 1
elif d > 0 and d != 0:
  positivo = positivo + 1

if e % 2 == 0:
  par = par + 1 
elif e % 2 != 0 and e != 0:
  impar = impar + 1
if e < 0:
  negativo = negativo + 1
elif e > 0 and e != 0:
  positivo = positivo + 1


print(str(par) + " valor(es) par(es)")
print(str(impar) + " valor(es) impar(es)")
print(str(positivo) + " valor(es) positivo(s)")
print(str(negativo) + " valor(es) negativo(s)")

  