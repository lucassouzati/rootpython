numeros = [10, 5, 2, 4, 7, 0]

def selectionSort(numeros):
    for i in range(0, len(numeros)):
        indiceMenor = i
        for j in range(i + 1, len(numeros)):
            if(numeros[j] < numeros[indiceMenor] ):
                indiceMenor = j
        numeros[i], numeros[indiceMenor] = numeros[indiceMenor], numeros[i]
    return numeros

print(selectionSort(numeros))
