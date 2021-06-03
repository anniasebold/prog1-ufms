string = list(input())
palavra = list(input())
hasEqual = False
tamanhoVetor = len(string) - len(palavra)

for i in range(0, tamanhoVetor + 1):
  trecho = []
  for j in range(0, len(palavra)):
    trecho.append(string[i+j])
  
  if trecho == palavra:
    hasEqual = True
    print(i)
  
if hasEqual == False:
  print("NOT FOUND!")