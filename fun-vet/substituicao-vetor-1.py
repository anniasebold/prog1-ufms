def lerValores():
  x = []
  for i in range(0, 10):
    x.append(int(input()))
  return x

def subValores():
  y = lerValores()
  for i in range(0, len(y)):
    if y[i] <= 0:
      y[i] = 1
  
  for i in range(0, len(y)):
    print(f"X[{i}] = {y[i]}")

subValores()