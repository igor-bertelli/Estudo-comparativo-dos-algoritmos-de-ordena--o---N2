import time
import random

def merge_sort(arr):
    trocas = 0
    comparacoes = 0

    def merge(left, right):
        nonlocal trocas, comparacoes
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparacoes += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
                trocas += len(left) - i  # Conta as trocas ao inserir elementos da metade direita

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    sorted_arr = merge(left, right)

    return sorted_arr, trocas, comparacoes

def run_merge_sort_case(case, size):
    if case == "melhor":
        arr = list(range(1, size + 1))  # Melhor Caso: Valores em ordem crescente
    elif case == "medio":
        arr = random.sample(range(1, size + 1), size)  # Caso Médio: Valores desordenados com números aleatórios
    elif case == "pior":
        arr = list(range(size, 0, -1))  # Pior Caso: Valores em ordem decrescente

    start_time = time.time()
    sorted_arr, trocas, comparacoes = merge_sort(arr.copy())
    end_time = time.time()

    execution_time = end_time - start_time
    return execution_time, trocas, comparacoes

# Teste para vetores de tamanho 1000, 10000, 100000
sizes = [1000, 10000, 100000]

for size in sizes:
    print(f"Tamanho do vetor: {size}")

    melhor_caso = run_merge_sort_case("melhor", size)
    medio_caso = run_merge_sort_case("medio", size)
    pior_caso = run_merge_sort_case("pior", size)

    print(f"Melhor Caso: Tempo de Execução = {melhor_caso[0]:.6f}s, Quantidade de Trocas = {melhor_caso[1]}, Quantidade de Comparações = {melhor_caso[2]}")
    print(f"Caso Médio: Tempo de Execução = {medio_caso[0]:.6f}s, Quantidade de Trocas = {medio_caso[1]}, Quantidade de Comparações = {medio_caso[2]}")
    print(f"Pior Caso: Tempo de Execução = {pior_caso[0]:.6f}s, Quantidade de Trocas = {pior_caso[1]}, Quantidade de Comparações = {pior_caso[2]}")
    print("-" * 50)
