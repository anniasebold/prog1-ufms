def calculaFormula(n):
    vetor_aux = []
    for i in range (n):
        valores = list(map(int, input().split()))
        vetor_aux.append(valores)
    val_menor = []
    for i in range (n):
        X = vetor_aux[i]
        valores = []
        for j in range (n):
            formula = ((X[0]-vetor_aux[j][0])**2+(X[1]-vetor_aux[j][1])**2+(X[2]-vetor_aux[j][2])**2)**0.5
            valores.append(formula)
def main():
    n = int(input())
    calculaFormula(n)
main()