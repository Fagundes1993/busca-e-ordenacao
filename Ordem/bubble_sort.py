def bubble_sort(arr):
    n = len(arr)

    # Percorre todos os elementos do array
    for i in range(n):
        # Últimos i elementos já estão ordenados, então não precisamos verificar novamente
        for j in range(0, n-i-1):
            # Troca se o elemento encontrado for maior que o próximo elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("Array ordenado:")
print(arr)

# Neste exemplo, a função bubble_sort recebe um array como parâmetro e o ordena usando o algoritmo Bubble Sort.
# A lógica é comparar elementos adjacentes e trocá-los se estiverem na ordem errada.
# O processo é repetido até que todo o array esteja ordenado.
# Ao executar este código, você verá que o array [64, 34, 25, 12, 22, 11, 90] será ordenado em ordem crescente.
# Você pode experimentar com diferentes arrays para ver como o algoritmo funciona em diferentes cenários.
# Lembre-se de que o Bubble Sort não é eficiente para grandes conjuntos de dados, pois tem uma complexidade quadrática.
# Em situações práticas, outros algoritmos de ordenação, como o Merge Sort ou o Quick Sort, são geralmente preferidos para conjuntos de dados maiores.
