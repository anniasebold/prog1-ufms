n = int(input())
aux = 1

for n in range(n+1):
  while n > 0 and aux <= n:
    print(f"{n} {n * n} {(n*n) * n}")
    print(f"{n} {n * n + 1} {((n*n) * n + 1)}")
    aux += 1