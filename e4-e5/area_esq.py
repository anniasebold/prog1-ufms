def areaEsquerda(M, O):
	soma = 0.0
	cont = 0
	n = len(M)

	for i in range(1, n - 1):
		colf = i if i <= 5 else n - i -1
		for j in range(0, colf):
			soma += M[i][j]
			cont += 1

	return soma if O == "S" else soma / cont


def main():
	O = input()

	n = 12

	M = [[0] * n for i in range(n)] # cria uma matriz n x n
	for i in range(n):
		for j in range(n):
			num = float(input())
			M[i][j] = num

	#print(M)

	valor = areaEsquerda(M, O)
	print(f"{valor:.1f}")

main()