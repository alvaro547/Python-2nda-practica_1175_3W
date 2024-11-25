print(" ")
print("Alvaro Campechano 3W")
print(" ")
def es_bisiesto(año):
    """
    Esta función determina si un año dado es bisiesto o no.
    
    Un año es bisiesto si es divisible por 4, pero no por 100, excepto cuando también es divisible por 400.
    
    Parámetros:
    año (int): El año que se evaluará.
    
    Retorna:
    bool: True si el año es bisiesto, False en caso contrario.
    
    Ejemplo:
    >>> es_bisiesto(2024)
    True
    """
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Entrada de datos
año = int(input("Introduce un año para saber si es bisiesto: "))
if es_bisiesto(año):
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")
