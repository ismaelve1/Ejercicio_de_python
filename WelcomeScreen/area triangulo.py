from os import read
base = int(input("Dime la base del triangulo: "))

altura = int(input("Dime la altura del triangulo: "))
if base <=0 or altura <=0:
    print("La base y la altura no pueden ser numeros negativos")
else:
    resultado = (base*altura) / 2

    print("El área del triangulo es: ", resultado)