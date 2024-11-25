print(" ")
print("Alvaro Campechano 3W")
print(" ")
def mas_larga(lista_palabras):
    """
    Esta función recibe una lista de palabras y devuelve la palabra más larga de la lista.
    
    Parámetros:
    lista_palabras (list): Una lista de cadenas de texto (palabras).
    
    Retorna:
    str: La palabra más larga en la lista.
    
    Ejemplo:
    >>> mas_larga(["manzana", "banana", "cereza", "kiwi"])
    'manzana'
    """
    return max(lista_palabras, key=len)

# Ejemplo de uso
palabras = ["manzana", "banana", "cereza", "kiwi"]
print("La palabra más larga es:", mas_larga(palabras))
