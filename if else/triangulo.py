a, b, c = input().split()
a = float(a)
b = float(b)
c = float(c)

if  a > b-c and a < b+c:
  perimetro = a + b + c
  print(f"Perimetro = {perimetro:.1f}")
elif b > a-c and b < a+c:
  perimetro = a + b + c
  print(f"Perimetro = {perimetro:.1f}")
elif c > a-b and c < a+b:
  perimetro = a + b + c
  print(f"Perimetro = {perimetro:.1f}")
else:
  trapezio = ((a+b)*c)/2
  print(f"Area = {trapezio:.1f}")