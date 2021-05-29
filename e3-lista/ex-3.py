def leN():
  n = int(input())

  return n

def inverteTexto():
  t = list(input())
  metadeTexto = 0
  tInvertido = []
  dentro = []
  fora = []
  foraInvertido = []

  tamanhoTexto = len(t)
  metadeTexto = len(t) // 2

  while tamanhoTexto:
    tamanhoTexto -= 1
    tInvertido.append(t[tamanhoTexto])

  for i in range(0, metadeTexto):
    dentro.append(tInvertido[i])
    fora.append(t[i])
  
  while metadeTexto:
    metadeTexto -= 1
    foraInvertido.append(fora[metadeTexto])
  
  return foraInvertido, dentro


def main():

  n = leN()

  for i in range(0, n):

    textoFinal = []
    foraInvertido, dentro = inverteTexto()

    textoFinal = foraInvertido + dentro
    textoFinal = "".join(textoFinal)

    print(textoFinal)

main()