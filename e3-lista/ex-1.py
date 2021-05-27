def main():
  impar = []
  par = []
  for i in range(0,15):
    n = int(input())

    if n % 2 == 0:
      par.append(n)
    
    else:
      impar.append(n)
    
    if len(par) == 5:
      for i in range(0, 5):
        print(f"par[{i}] = {par[i]}")
      par = []
    
    if len(impar) == 5:
      for i in range(0, 5):
        print(f"impar[{i}] = {impar[i]}")
      impar = []
  
  for i in range(0, len(impar)):
    print(f"impar[{i}] = {impar[i]}")

  for i in range(0, len(par)):
    print(f"par[{i}] = {par[i]}")

main()