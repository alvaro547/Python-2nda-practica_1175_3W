print(" ")
print("Alvaro Campechano 3W")
print(" ")
def contar_nombres_letra(nombres, letra):
    """
    Esta función recibe una lista de nombres y una letra, y cuenta cuántos nombres comienzan con esa letra.
    
    Parámetros:
    nombres (list): Una lista de nombres (cadenas de texto).
    letra (str): La letra con la que deben comenzar los nombres.
    
    Retorna:
    int: El número de nombres que comienzan con la letra especificada.
    
    Ejemplo:
    >>> contar_nombres_letra(["Ana", "Carlos", "Andrea", "Pedro", "Alba", "Lucas"], "A")
    4
    """
    return len([nombre for nombre in nombres if nombre.lower().startswith(letra.lower())])

# Entrada de datos
nombres = ["Ana", "Carlos", "Andrea", "Pedro", "Alba", "Lucas"]
letra_buscar = input("Introduce la letra que deseas buscar: ")

print(f"Cantidad de nombres que comienzan con {letra_buscar}: {contar_nombres_letra(nombres, letra_buscar)}")
