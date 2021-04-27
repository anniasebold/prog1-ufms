i = 1
valida = 0 
valor = 0

while i > 0:
  n = float(input())
  if n >= 0 and n <= 10:
    valida += 1
    valor += n
  else: 
    print("nota invalida")
  if valida == 2:
    media = valor / 2
    print(f"media = {media}")
    break
  i += 1  