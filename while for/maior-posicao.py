i = 1
maior = 0
posicao = 0

while i <= 100:
  n = int(input())
  if n > maior:
    maior = n
    posicao = i
  i += 1

print(maior)
print(posicao)