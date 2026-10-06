num = int(input("Dime tu numero: "))

valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
romanos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

resultado = ""

for i in range(len(valores)):
    while num >= valores[i]:
        resultado += romanos[i]
        num -= valores[i]

print("En números romanos:", resultado)