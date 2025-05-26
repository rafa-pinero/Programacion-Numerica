import numpy as np

def multiplos_fila(vector):

    x = len(vector)
    matriz = np.zeros((x, x), dtype=int)

    for i in range(x):
        matriz[i, :]=[(j+1)*vector[i] for j in range(x)]

    print(matriz)

    return matriz

def multiplos_columna(vector):

    x=len(vector)
    matriz = np.zeros((x,x), dtype=int)

    for i in range(x):
        matriz[:, i]=[(j+1)*vector[i] for j in range(x)]

    print(matriz)

    return matriz

