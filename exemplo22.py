valor = input("Base do triângulo: ")
base = float(valor)

altura = float(input("Altura do triângulo: "))

area = base * altura / 2

print("A área vale", area)

area2 = round(area, 2) #arredondando para 2 casas decimais
print("A área vale " + str(area2))
