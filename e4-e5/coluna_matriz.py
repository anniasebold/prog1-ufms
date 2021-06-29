def calculaSM(M, C, T):
	soma = 0.0
	n = len(M)
	for i in range(n):
		soma += M[i][C]

	if T == "S":
		return soma
	else:
		return soma / n


def main():
	C = int(input())
	T = input()

	n = 12

	M = [[0] * n for i in range(n)] # cria uma matriz n x n
	for i in range(n):
		for j in range(n):
			num = float(input())
			M[i][j] = num

	#print(M)

	valor = calculaSM(M, C, T)

	print(f"{valor:.1f}")

main()