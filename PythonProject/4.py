def numero_a_romano(num):
    if num < 1 or num > 3999:
        return "numero invalido"

    valores = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "XL"), (5, "X"), (4, "IX"), (1, "I"),
    ]

    resultado = ""
    for valor, simbolo in valores:
        while num >= valor:
            resultado += simbolo
            num -= valor
    return resultado

try:
    numero = int(input("introduce un numero entero: "))
    print(numero_a_romano(numero))
except ValueError:
    print("numero invalido")