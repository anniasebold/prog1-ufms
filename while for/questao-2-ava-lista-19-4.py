x = float(input())
n = int(input())

val = 0 
soma = True

for i in range(0, n+1):
  fat = 1

  for j in range(1, i+1):
    fat = fat * j
    if soma:
      val = fat + x ** i / j
      soma = False
    else:
      soma = True
      val = fat - x ** i / j

print(f"{val:.4f}")