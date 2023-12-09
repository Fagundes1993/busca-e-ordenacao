def merge_sort(arr):
    if len(arr) > 1:
        # Divide o array ao meio
        meio = len(arr) // 2
        esquerda = arr[:meio]
        direita = arr[meio:]

        # Recursivamente, ordena as duas metades
        merge_sort(esquerda)
        merge_sort(direita)

        # Combina as duas metades ordenadas
        i = j = k = 0

        while i < len(esquerda) and j < len(direita):
            if esquerda[i] < direita[j]:
                arr[k] = esquerda[i]
                i += 1
            else:
                arr[k] = direita[j]
                j += 1
            k += 1

        # Adiciona os elementos restantes, se houver, em esquerda
        while i < len(esquerda):
            arr[k] = esquerda[i]
            i += 1
            k += 1

        # Adiciona os elementos restantes, se houver, em direita
        while j < len(direita):
            arr[k] = direita[j]
            j += 1
            k += 1

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)

print("Array ordenado:")
print(arr)

# Neste exemplo, a função merge_sort implementa o algoritmo Merge Sort.
# O algoritmo segue a abordagem de dividir e conquistar, dividindo o array em metades, ordenando recursivamente cada metade e, finalmente, mesclando as duas metades ordenadas.
# Ao executar este código, você verá que o array [64, 34, 25, 12, 22, 11, 90] será ordenado em ordem crescente.
# O Merge Sort tem uma complexidade de tempo de O(n log n) em todos os casos, tornando-o eficiente para conjuntos de dados maiores em comparação com algoritmos de ordenação quadráticos.