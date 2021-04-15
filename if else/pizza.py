tam, queijo, borda = input().split()
total = 0

if tam == "P":
  total = total + 15
elif tam == "M":
  total = total + 18.50
elif tam == "G":
  total = total + 23.00

if queijo == "S":
  if tam == "P":
    total = total + 2.50
  else:
    total = total + 4.0
elif queijo == "N":
  total = total

if borda == "S":
  total = total + 5.00
elif borda == "N":
  total = total

print(f"Total: R$ {total:.2f}")