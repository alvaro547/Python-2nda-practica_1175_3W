print(" ")
print("Alvaro Campechano 3W")
print(" ")
def contar_mayusculas(cadena):
    """
    Esta función recibe una cadena de texto y devuelve la cantidad de letras mayúsculas que contiene.
    
    Parámetros:
    cadena (str): Una cadena de texto (puede contener letras mayúsculas y minúsculas).
    
    Retorna:
    int: La cantidad de letras mayúsculas en la cadena.
    
    Ejemplo:
    >>> contar_mayusculas("Hola Mundo")
    2
    """
    return sum(1 for c in cadena if c.isupper())

# Ejemplo de uso
cadena_usuario = input("Introduce una cadena de texto: ")
print("Número de letras mayúsculas:", contar_mayusculas(cadena_usuario))
