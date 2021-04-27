t = int(input())
for t in range(t):
  pa,pb,g1,g2 = input().split()
  pa = int(pa)
  pb = int(pb)
  g1 = float(g1)
  g2 = float(g2)
  tempo = 0
  while pa <= pb and tempo <= 100:
    pa = pa + (pa * g1) // 100
    pb = pb + (pb * g2) // 100
    tempo += 1
  if tempo > 100:
    print("Mais de 1 seculo.")
  else:
    print(f"{tempo} anos.")