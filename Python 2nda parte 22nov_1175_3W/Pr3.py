print(" ")
print("Alvaro Campechano 3W")
print(" ")
def filtrar_palabras(lista_palabras, n):
    """
    Esta función recibe una lista de palabras y un número entero n, y devuelve una lista con las palabras
    que tienen más de n caracteres.
    
    Parámetros:
    lista_palabras (list): Una lista de cadenas de texto (palabras).
    n (int): El número mínimo de caracteres que deben tener las palabras.
    
    Retorna:
    list: Una lista con las palabras que tienen más de n caracteres.
    
    Ejemplo:
    >>> filtrar_palabras(["manzana", "kiwi", "cereza", "uva"], 4)
    ['manzana', 'cereza']
    """
    return [palabra for palabra in lista_palabras if len(palabra) > n]

# Ejemplo de uso
palabras = ["manzana", "kiwi", "cereza", "uva"]
print("Palabras con más de 4 caracteres:", filtrar_palabras(palabras, 4))
