valor_digitado = int(input(""))
notas_100 =  valor_digitado  // 100
valor = valor_digitado % 100
notas_50 = valor // 50
valor = valor %  50
notas_20 = valor // 20
valor = valor %  20
notas_10 = valor // 10
valor = valor %  10
notas_5 = valor // 5
valor = valor %  5
notas_2 = valor // 2
valor = valor %  2
notas_1 = valor // 1

print(str(valor_digitado))
print(str(notas_100) + " nota(s) de R$ 100,00")
print(str(notas_50) + " nota(s) de R$ 50,00")
print(str(notas_20) + " nota(s) de R$ 20,00")
print(str(notas_10) + " nota(s) de R$ 10,00")
print(str(notas_5) + " nota(s) de R$ 5,00")
print(str(notas_2) + " nota(s) de R$ 2,00")
print(str(notas_1) + " nota(s) de R$ 1,00")