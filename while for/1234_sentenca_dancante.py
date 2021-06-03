def dancante(s):
  stringFinal = []
  vez = True

  for i in range(0, len(s)):
    if s[i] == " ":
      stringFinal.append(" ")
    if vez == True and s[i] != " ":
      stringFinal.append(s[i].upper())
      vez = False
    elif vez == False and s[i] != " ":
      stringFinal.append(s[i].lower())
      vez = True

  stringFinal = "".join(stringFinal)
  print(stringFinal)

def main():
	while True:
		try:
			s = input()
			d = dancante(s)

		except EOFError:
			break

main()