dec = int(input())

binario = 0
exp = 0
while dec != 0:
  binario += (dec % 2) * (10 ** exp)
  exp += 1
  dec = dec // 2
  
print(binario)