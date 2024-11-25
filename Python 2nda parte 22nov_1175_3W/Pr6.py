print(" ")
print("Alvaro Campechano 3W")
print(" ")
def calcular_edad(año_nacimiento, año_actual):
    """
    Esta función calcula la edad de una persona dado su año de nacimiento y el año actual.
    
    Parámetros:
    año_nacimiento (int): El año en que nació la persona.
    año_actual (int): El año actual.
    
    Retorna:
    int: La edad de la persona.
    
    Ejemplo:
    >>> calcular_edad(1990, 2024)
    34
    """
    return año_actual - año_nacimiento

# Entrada de datos
año_actual = int(input("Introduce el año en curso: "))
personas = []
for i in range(3):
    nombre = input(f"Introduce el nombre de la persona {i+1}: ")
    año_nacimiento = int(input(f"Introduce el año de nacimiento de {nombre}: "))
    edad = calcular_edad(año_nacimiento, año_actual)
    personas.append((nombre, edad))

# Mostrar resultados
for persona in personas:
    print(f"{persona[0]} tiene {persona[1]} años en {año_actual}.")
