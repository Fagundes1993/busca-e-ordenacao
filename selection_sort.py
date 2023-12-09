def selection_sort(arr):
    n = len(arr)

    # Percorre todos os elementos do array
    for i in range(n):
        # Encontra o índice do menor elemento não ordenado
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
selection_sort(arr)

print("Array ordenado:")
print(arr)

# Neste exemplo, a função selection_sort recebe um array como parâmetro e o ordena usando o algoritmo Selection Sort.
# A ideia é selecionar o menor elemento não ordenado a cada iteração e trocá-lo com o primeiro elemento não ordenado.
# Ao executar este código, você verá que o array [64, 34, 25, 12, 22, 11, 90] será ordenado em ordem crescente.
# Assim como o Bubble Sort, o Selection Sort tem uma complexidade quadrática e não é eficiente para grandes conjuntos de dados.
# Outros algoritmos, como o Merge Sort ou o Quick Sort, são preferidos em cenários práticos para conjuntos de dados maiores.