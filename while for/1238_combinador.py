def leitura():
  n = int(input())

  return n

def combinaStrings():
  n = leitura()

  for i in range(0, n):
    string = list(input().split())
    string1 = []
    stringFinal = []
    
    string1 = string[1] 
    string = string[0]

    string1 = list(string1)
    string = list(string)

    if len(string1) > len(string):
      maiorString = string1
      menorString = string
    else:
      maiorString = string
      menorString = string1

    tamanhoMenorString = len(menorString)

    for i in range(0, len(maiorString)):
      if tamanhoMenorString != 0:
        stringFinal.append(string[i])
        stringFinal.append(string1[i])
        tamanhoMenorString -= 1
      else:
        stringFinal.append(maiorString[i])
  
    stringFinal = "".join(stringFinal)
    print(stringFinal)

def main():
  combinaStrings()

main()
