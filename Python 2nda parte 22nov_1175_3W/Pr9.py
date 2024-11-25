print(" ")
print("Alvaro Campechano 3W")
print(" ")
def contar_vocales(palabra):
    """
    Esta función recibe una palabra y cuenta cuántas veces aparece cada una de las vocales.
    
    Parámetros:
    palabra (str): La palabra en la que se contarán las vocales.
    
    Retorna:
    dict: Un diccionario con la cantidad de veces que aparece cada vocal en la palabra.
    
    Ejemplo:
    >>> contar_vocales("banana")
    {'a': 3, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
    """
    conteo_vocales = {vocal: palabra.lower().count(vocal) for vocal in "aeiou"}
    return conteo_vocales

# Entrada de datos
palabra = input("Introduce una palabra: ")
vocales = contar_vocales(palabra)

for vocal, cantidad in vocales.items():
    print(f"La letra '{vocal}' aparece {cantidad} veces.")
