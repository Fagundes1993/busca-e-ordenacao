def busca_linear(arr, alvo):
    for i in range(len(arr)):
        if arr[i] == alvo:
            return i  # Retorna o índice se o elemento for encontrado
    return -1  # Retorna -1 se o elemento não estiver no array

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
alvo = 25

resultado = busca_linear(arr, alvo)

if resultado != -1:
    print(f"O elemento {alvo} foi encontrado no índice {resultado}.")
else:
    print(f"O elemento {alvo} não está presente no array.")

# Neste exemplo, a função busca_linear recebe um array e um alvo como parâmetros e percorre o array sequencialmente.
# Se o elemento for encontrado, a função retorna o índice desse elemento.
# Caso contrário, retorna -1 para indicar que o elemento não está presente no array.
# Ao executar este código com o exemplo fornecido, você verá que o algoritmo imprime que o elemento 25 foi encontrado no índice 2 do array.
# A busca linear é um método simples, porém, para grandes conjuntos de dados, outros algoritmos de busca mais eficientes, como a busca binária em arrays ordenados, podem ser preferíveis.