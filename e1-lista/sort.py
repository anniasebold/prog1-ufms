a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

maior = 0
meio = 0
menor = 0

if a > b and a > c:
  maior = a
  if b < c: 
    meio = c
    menor = b
  elif c < b:
    meio = b
    menor = c
elif b > a and b > c:
  maior = b
  if a < c:
    meio = c
    menor = a
  elif c < a:
    meio = a
    menor = c
elif c > a and c > b:
  maior = c
  if b < a:
    meio = a
    menor = b
  elif a < b:
    meio = b
    menor = a

print(menor)
print(meio)
print(maior)
print()
print(a)
print(b)
print(c)