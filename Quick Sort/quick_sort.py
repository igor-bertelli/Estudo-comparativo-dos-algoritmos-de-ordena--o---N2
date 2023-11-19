import time
import random

def quick_sort(arr):
    trocas = 0
    comparacoes = 0

    def partition(arr, low, high):
        nonlocal trocas, comparacoes
        pivot = arr[high]
        i = low - 1

        for j in range(low, high):
            comparacoes += 1
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                trocas += 1

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        trocas += 1

        return i + 1

    def quick_sort_recursive(arr, low, high):
        nonlocal trocas, comparacoes
        if low < high:
            partition_index = partition(arr, low, high)
            quick_sort_recursive(arr, low, partition_index - 1)
            quick_sort_recursive(arr, partition_index + 1, high)

    start_time = time.time()
    quick_sort_recursive(arr, 0, len(arr) - 1)
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time, trocas, comparacoes

def run_quick_sort_case(case, size):
    if case == "melhor":
        arr = list(range(1, size + 1))  # Melhor Caso: Valores em ordem crescente
    elif case == "medio":
        arr = random.sample(range(1, size + 1), size)  # Caso Médio: Valores desordenados com números aleatórios
    elif case == "pior":
        arr = list(range(size, 0, -1))  # Pior Caso: Valores em ordem decrescente

    start_time = time.time()
    trocas, comparacoes = quick_sort(arr.copy())
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time, trocas, comparacoes

# Teste para vetores de tamanho 1000, 10000, 100000
sizes = [1000, 10000, 100000]

for size in sizes:
    print(f"Tamanho do vetor: {size}")

    melhor_caso = run_quick_sort_case("melhor", size)
    medio_caso = run_quick_sort_case("medio", size)
    pior_caso = run_quick_sort_case("pior", size)

    print(f"Melhor Caso: Tempo de Execução = {melhor_caso[0]:.6f}s, Quantidade de Trocas = {melhor_caso[1]}, Quantidade de Comparações = {melhor_caso[2]}")
    print(f"Caso Médio: Tempo de Execução = {medio_caso[0]:.6f}s, Quantidade de Trocas = {medio_caso[1]}, Quantidade de Comparações = {medio_caso[2]}")
    print(f"Pior Caso: Tempo de Execução = {pior_caso[0]:.6f}s, Quantidade de Trocas = {pior_caso[1]}, Quantidade de Comparações = {pior_caso[2]}")
    print("-" * 50)
