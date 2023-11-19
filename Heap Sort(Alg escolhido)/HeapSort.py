import time
import random

def heap_sort(arr):
    trocas = 0
    comparacoes = 0

    def heapify(arr, n, i):
        nonlocal trocas, comparacoes
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        comparacoes += 1
        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        comparacoes += 1
        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            trocas += 1
            heapify(arr, n, largest)

    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        trocas += 1
        heapify(arr, i, 0)

    return trocas, comparacoes

def run_heap_sort_case(case, size):
    if case == "melhor":
        arr = list(range(1, size + 1))  # Melhor Caso: Valores em ordem crescente
    elif case == "medio":
        arr = random.sample(range(1, size + 1), size)  # Caso Médio: Valores desordenados com números aleatórios
    elif case == "pior":
        arr = list(range(size, 0, -1))  # Pior Caso: Valores em ordem decrescente

    start_time = time.time()
    trocas, comparacoes = heap_sort(arr.copy())
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time, trocas, comparacoes

# Teste para vetores de tamanho 1000, 10000, 100000
sizes = [1000, 10000, 100000]

for size in sizes:
    print(f"Tamanho do vetor: {size}")

    melhor_caso = run_heap_sort_case("melhor", size)
    medio_caso = run_heap_sort_case("medio", size)
    pior_caso = run_heap_sort_case("pior", size)

    print(f"Melhor Caso: Tempo de Execução = {melhor_caso[0]:.6f}s, Quantidade de Trocas = {melhor_caso[1]}, Quantidade de Comparações = {melhor_caso[2]}")
    print(f"Caso Médio: Tempo de Execução = {medio_caso[0]:.6f}s, Quantidade de Trocas = {medio_caso[1]}, Quantidade de Comparações = {medio_caso[2]}")
    print(f"Pior Caso: Tempo de Execução = {pior_caso[0]:.6f}s, Quantidade de Trocas = {pior_caso[1]}, Quantidade de Comparações = {pior_caso[2]}")
    print("-" * 50)