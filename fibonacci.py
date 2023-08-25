

def retornaFibonacci(n):
    sequencia = [0, 1]
    indice = 1

    while(indice <= n):
        sequencia.append(sequencia[indice] + sequencia[indice -1])
        indice += 1
    return sequencia[n]

print(retornaFibonacci(3))