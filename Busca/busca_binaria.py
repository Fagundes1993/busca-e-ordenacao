def busca_binaria(arr, alvo):
    inicio, fim = 0, len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        # Verifica se o elemento no meio é igual ao alvo
        if arr[meio] == alvo:
            return meio  # Retorna o índice se o elemento for encontrado
        elif arr[meio] < alvo:
            inicio = meio + 1  # Descarta a metade à esquerda
        else:
            fim = meio - 1  # Descarta a metade à direita

    return -1  # Retorna -1 se o elemento não estiver no array

# Exemplo de uso:
arr = [11, 12, 22, 25, 34, 64, 90]
alvo = 25

resultado = busca_binaria(arr, alvo)

if resultado != -1:
    print(f"O elemento {alvo} foi encontrado no índice {resultado}.")
else:
    print(f"O elemento {alvo} não está presente no array.")

# Neste exemplo, a função busca_binaria recebe um array ordenado e um alvo como parâmetros.
# O algoritmo compara o elemento no meio do array com o alvo e descarta metade do array a cada iteração com base nessa comparação.
# Ao executar este código com o exemplo fornecido, você verá que o algoritmo imprime que o elemento 25 foi encontrado no índice 3 do array.
# A busca binária é mais eficiente do que a busca linear para arrays ordenados, pois reduz pela metade o espaço de busca a cada iteração.