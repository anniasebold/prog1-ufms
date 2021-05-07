def main():
  x = []
  x.append(int(input()))
  for i in range(0, 10):
    x.append(x[i]*2)
    print(f"N[{i}] = {x[i]}")

main()