import random

def generar_matriz(n):
    """
    Genera una matriz cuadrada de tamaño NxN y la rellena con números aleatorios entre 0 y 9.
    """
    matriz = []
    for _ in range(n):
        fila = []
        for _ in range(n):
            fila.append(random.randint(0, 9))
        matriz.append(fila)
    return matriz

def imprimir_matriz(matriz):
    """
    Imprime la matriz en pantalla.
    """
    for fila in matriz:
        print(fila)

def sumar_filas_columnas(matriz):
    """
    Calcula la suma de los elementos de cada fila y columna de la matriz.
    Retorna dos listas con las sumas de las filas y las columnas, respectivamente.
    """
    filas = []
    columnas = []
    n = len(matriz)
    for i in range(n):
        suma_fila = sum(matriz[i])
        suma_columna = sum(fila[i] for fila in matriz)
        filas.append(suma_fila)
        columnas.append(suma_columna)
    return filas, columnas

def imprimir_sumas(filas, columnas):
    """
    Imprime la suma de cada fila y columna en pantalla.
    """
    print("Suma de las filas:")
    for i, suma in enumerate(filas):
        print(f"Fila {i+1}: {suma}")
    print("\nSuma de las columnas:")
    for i, suma in enumerate(columnas):
        print(f"Columna {i+1}: {suma}")

# Pedir al usuario el tamaño de la matriz
while True:
    try:
        n = int(input("Ingrese el tamaño de la matriz cuadrada: "))
        if n <= 0:
            raise ValueError()
        break
    except ValueError:
        print("Error: el valor ingresado debe ser un número entero mayor a cero.")

# Generar la matriz
matriz = generar_matriz(n)

# Imprimir la matriz generada
print("Matriz generada:")
imprimir_matriz(matriz)

# Calcular la suma de cada fila y columna
filas, columnas = sumar_filas_columnas(matriz)

# Imprimir la suma de cada fila y columna
imprimir_sumas(filas, columnas)
