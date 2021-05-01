binario = int(input())

decimal = 0
exp = 0
while binario != 0:
  divisao = binario // 10
  resto = binario % 10
  decimal = decimal + resto * (2 ** exp)
  exp = exp + 1
  binario = divisao
print(decimal)