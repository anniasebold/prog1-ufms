def calculaProduto():
  u = list(map(float, input().split()))
  v = list(map(float, input().split()))
  total = 0

  for i in range(0, len(u)):
    total += u[i] * v[i]

  print(f"{total:.4f}")

calculaProduto()