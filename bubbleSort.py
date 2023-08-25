numeros = [3, 2, 2, 5, 3, 3, 0]


def bubbleSort(numeros):
    continuaVerificando = True
    while(continuaVerificando):
        continuaVerificando = False
        for i in range(0, len(numeros) - 1):
            if(numeros[i] > numeros[i+1]):
                numeros[i], numeros[i+1] = numeros[i+1], numeros[i]
                continuaVerificando = True
    return numeros


print(bubbleSort(numeros))