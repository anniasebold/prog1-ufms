def calculaDerivada():
  coef = list(map(float, input().split()))

  for i in range(len(coef)):
    der = coef[i] * i
    if i != 0:
      print(f"{der:.4f}")

calculaDerivada()