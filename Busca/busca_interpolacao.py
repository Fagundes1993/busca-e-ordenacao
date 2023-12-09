def busca_interp(arr, alvo):
    inicio, fim = 0, len(arr) - 1

    while inicio <= fim and arr[inicio] <= alvo <= arr[fim]:
        # Fórmula de interpolação para estimar a posição do alvo
        posicao = inicio + ((alvo - arr[inicio]) * (fim - inicio)) // (arr[fim] - arr[inicio])

        # Verifica se o alvo está no meio
        if arr[posicao] == alvo:
            return posicao
        elif arr[posicao] < alvo:
            inicio = posicao + 1  # Descarta a metade à esquerda
        else:
            fim = posicao - 1  # Descarta a metade à direita

    return -1  # Retorna -1 se o elemento não estiver no array

# Exemplo de uso:
arr = [11, 12, 22, 25, 34, 64, 90]
alvo = 25

resultado = busca_interp(arr, alvo)

if resultado != -1:
    print(f"O elemento {alvo} foi encontrado no índice {resultado}.")
else:
    print(f"O elemento {alvo} não está presente no array.")

# Neste exemplo, a função busca_interp recebe um array ordenado e um alvo como parâmetros.
# A fórmula de interpolação é utilizada para estimar a posição do alvo.
# E o algoritmo então compara o elemento estimado com o alvo, descartando metade do array a cada iteração.
# Lembre-se de que a busca por interpolação é mais eficaz quando os elementos estão uniformemente distribuídos.
# Em casos em que a distribuição não é uniforme, a busca binária pode ser uma escolha mais robusta.