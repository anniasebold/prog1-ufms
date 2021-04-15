t = float(input())

if t < 0.0:
  print("Frio")
elif t >= 0 and t < 14:
  print("Um pouco frio")
elif t <= 14 and t < 23:
  print("Agradavel")
else:
  print("Calor")