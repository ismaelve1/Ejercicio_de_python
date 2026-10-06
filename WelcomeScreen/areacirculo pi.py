import math

radio = float(input("Ingrese el radio de la circunferencia en metros: "))
if radio > 0:
    area = math.pi * (radio ** 2)
    longitud = 2 * math.pi * radio

else: print("Error: El radio debe ser un valor positivo")


print (f"area: {area:.2f} metros cuadrados")
print(f"longitud: {longitud:.2f} metros")