n = int(input())
numero = n
inverso = 0

while numero > 0:
  resto = numero % 10 
  inverso = (inverso*10) + resto
  numero = numero // 10

if n == 0:
  print("SIM")
elif n / inverso == 1:
  print("SIM")
else:
  print("NAO")