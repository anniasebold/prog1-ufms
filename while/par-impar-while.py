n = int(input())

par = 0
impar = 0
i = 1
while i <= n:
  var = int(input())
  if var % 2 == 0:
    par += var
  else:
    impar += var

  i += 1

print(f"Pares: {par}")
print(f"Impares: {impar}")