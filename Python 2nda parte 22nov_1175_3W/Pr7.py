print(" ")
print("Alvaro Campechano 3W")
print(" ")
edades = (25, 30, 18, 22, 19, 40, 12, 65, 33, 18)

# Contar personas mayores de 20
mayores_de_20 = len([edad for edad in edades if edad > 20])

print(f"Cantidad de personas con edades mayores a 20: {mayores_de_20}")
