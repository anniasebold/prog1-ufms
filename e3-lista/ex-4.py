def leTexto():
  t = list(input())

  return t

def main():
  while True:
    try:
      t = leTexto()
      aux = 0
      aux1 = 0
      for i in range(len(t)):
        if t[i] == '_' and aux == 1:
          aux = 0
          t[i] = '</i>'
        if t[i] == '_':
          aux += 1
          t[i] = '<i>'
        if t[i] == '*' and aux1 == 1:
          aux1 = 0
          t[i] = '</b>'
        if t[i] == '*':
          aux1 += 1
          t[i] = '<b>'
      t = "".join(t)
      print(t)
    except EOFError:
      break

main()