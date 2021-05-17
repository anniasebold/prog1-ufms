def calculaPolinomio():
  coef = list(map(float, input().split()))

  k = int(input())
  for i in range(0, k):
    x = float(input())
    p = 0
    for i in range(len(coef)):
      p += coef[i] * (x**i)
    print(f"{p:.4f}")

calculaPolinomio() 