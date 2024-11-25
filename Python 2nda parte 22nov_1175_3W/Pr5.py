print(" ")
print("Alvaro Campechano 3W")
print(" ")
def binario_a_entero(binario):
    """
    Esta función convierte un número binario (en formato de cadena) en su equivalente decimal (entero).
    
    Parámetros:
    binario (str): Una cadena de caracteres que representa un número binario.
    
    Retorna:
    int: El número decimal equivalente al binario.
    
    Ejemplo:
    >>> binario_a_entero("1011")
    11
    """
    return int(binario, 2)

# Ejemplo de uso
numero_binario = input("Introduce un número binario: ")
print("El número entero es:", binario_a_entero(numero_binario))
