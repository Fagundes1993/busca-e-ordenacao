def insertion_sort(arr):
    n = len(arr)

    # Percorre todos os elementos do array
    for i in range(1, n):
        chave = arr[i]
        
        # Move os elementos do array que são maiores que a chave
        # para uma posição à frente de sua posição atual
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        # Insere a chave na posição correta
        arr[j + 1] = chave

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(arr)

print("Array ordenado:")
print(arr)

# Neste exemplo, a função insertion_sort recebe um array como parâmetro e o ordena usando o algoritmo Insertion Sort.
# A ideia é dividir o array em duas partes: uma parte ordenada e uma parte não ordenada.
# A cada iteração, o algoritmo pega um elemento da parte não ordenada e o insere na posição correta da parte ordenada.
# Ao executar este código, você verá que o array [64, 34, 25, 12, 22, 11, 90] será ordenado em ordem crescente.
# O Insertion Sort tem uma complexidade quadrática, assim como o Bubble Sort e o Selection Sort.
# Em cenários práticos, algoritmos mais eficientes, como o Merge Sort ou o Quick Sort, são preferidos para conjuntos de dados maiores.