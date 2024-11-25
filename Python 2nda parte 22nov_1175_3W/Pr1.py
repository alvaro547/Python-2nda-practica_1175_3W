print(" ")
print("Alvaro Campechano 3W")
print(" ")
def max_in_list(numbers):
    """
    Esta función recibe una lista de números y devuelve el número más grande de la lista.
    
    Parámetros:
    numbers (list): Una lista de números (enteros o flotantes).
    
    Retorna:
    int o float: El número más grande en la lista.
    
    Ejemplo:
    >>> max_in_list([3, 45, 12, 78, 5])
    78
    """
    return max(numbers)

# Ejemplo de uso
lista_numeros = [3, 45, 12, 78, 5]
print("El número más grande es:", max_in_list(lista_numeros))
