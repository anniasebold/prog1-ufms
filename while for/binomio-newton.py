n = int(input())
k = int(input())

fat1 = 1
for i in range(1, n+1):
  fat1 = fat1 * i

fat2 = 1 
for i in range(1, k+1):
  fat2 = fat2 * i

fat3 = 1
for i in range(1, n-k+1):
  fat3 = fat3 * i
  
comb = fat1 // (fat2 * fat3)
print(comb)