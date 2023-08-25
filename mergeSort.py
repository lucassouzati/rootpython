numeros = [2 , 1, 9, 5, 3, 4, 0, 10, 7, 12]


def mergeSort(numeros):
    tamanhoLista = len(numeros)
    if(tamanhoLista//2 >= 1):
        esquerda = mergeSort(numeros[:tamanhoLista//2])
        direita = mergeSort(numeros[tamanhoLista//2:])
    else:
        return numeros
    
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0

    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1

    resultado += esquerda[i:]
    resultado += direita[j:]
    return resultado



print(mergeSort(numeros))
