def leVetor():
  a = []
  for i in range(0, 100):
    a.append(float(input()))
  return a

def mostraVetor():
  a = leVetor()
  for i in range(0, len(a)):
    if a[i] <= 10:
      print(f"A[{i}] = {a[i]:.1f}")

mostraVetor()