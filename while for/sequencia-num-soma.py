m,n= input().split()
m = int(m)
n = int(n)
while m > 0 or n > 0:
  if m <= 0 or n <= 0:
    break
  if n < m:
    print(f"{n} ", end="")
    soma = n
    aux = n
    while aux < m:
      aux += 1
      soma += aux
      print(f"{aux} ", end="")
    print(f"Sum={soma}")
  else:
    print(f"{m} ", end="")
    soma = m
    aux = m
    while aux < n:
      aux += 1
      soma += aux
      print(f"{aux} ", end="")
    print(f"Sum={soma}")
  m,n= input().split()
  m = int(m)
  n = int(n)