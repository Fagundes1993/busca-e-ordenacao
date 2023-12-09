def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        # Escolhe um elemento como pivô (geralmente o último elemento)
        pivot = arr.pop()

        # Particiona os elementos restantes em dois subarrays
        menores = [elem for elem in arr if elem <= pivot]
        maiores = [elem for elem in arr if elem > pivot]

        # Recursivamente, ordena os subarrays e concatena com o pivô no meio
        return quick_sort(menores) + [pivot] + quick_sort(maiores)

# Exemplo de uso:
arr = [64, 34, 25, 12, 22, 11, 90]
arr_ordenado = quick_sort(arr)

print("Array ordenado:")
print(arr_ordenado)

# Neste exemplo, a função quick_sort implementa o algoritmo Quick Sort.
# O algoritmo escolhe um elemento como pivô, particiona os elementos restantes em dois subarrays (um com elementos menores ou iguais ao pivô e outro com elementos maiores), e, em seguida, ordena recursivamente esses subarrays.
# O pivô é concatenado entre os subarrays ordenados para formar a solução final.
# Ao executar este código, você verá que o array [64, 34, 25, 12, 22, 11, 90] será ordenado em ordem crescente.
# O Quick Sort tem uma complexidade de tempo média de O(n log n), tornando-o eficiente para muitos conjuntos de dados.
# No entanto, é importante notar que o desempenho do Quick Sort pode degradar para casos extremos, como quando o array já está quase ordenado.