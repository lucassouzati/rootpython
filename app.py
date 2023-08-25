

numero_ordenados = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


def busca_binaria(numero_ordenados, numero_procurado):
    inicio = 0
    fim = len(numero_ordenados) - 1
    while(inicio <= fim):
        indice = (inicio + fim) // 2
        if(numero_ordenados[indice] == numero_procurado):
            return indice
        elif(numero_ordenados[indice] > numero_procurado):
            fim = indice - 1
        else:
            inicio = indice + 1
    return -1


resultado = busca_binaria(numero_ordenados, 3)
print(resultado)