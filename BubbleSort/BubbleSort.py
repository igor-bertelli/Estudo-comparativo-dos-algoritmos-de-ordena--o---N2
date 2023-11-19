import time
import random

def bubble_sort(arr):
    trocas = 0
    comparacoes = 0
    n = len(arr)

    for i in range(n):
        trocas_passo = 0
        for j in range(0, n-i-1):
            comparacoes += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                trocas += 1
                trocas_passo += 1

        # Se nenhuma troca ocorreu durante um passo, o vetor já está ordenado
        if trocas_passo == 0:
            break

    return trocas, comparacoes

def run_bubble_sort_case(case, size):
    if case == "melhor":
        arr = list(range(1, size + 1))  # Melhor Caso: Valores em ordem crescente
    elif case == "medio":
        arr = random.sample(range(1, size + 1), size)  # Caso Médio: Valores desordenados com números aleatórios
    elif case == "pior":
        arr = list(range(size, 0, -1))  # Pior Caso: Valores em ordem decrescente

    start_time = time.time()
    trocas, comparacoes = bubble_sort(arr)
    end_time = time.time()
    execution_time = end_time - start_time

    return execution_time, trocas, comparacoes

# Teste para vetores de tamanho 1000, 10000, 100000
sizes = [1000, 10000, 100000]

for size in sizes:
    print(f"Tamanho do vetor: {size}")
    
    melhor_caso = run_bubble_sort_case("melhor", size)
    medio_caso = run_bubble_sort_case("medio", size)
    pior_caso = run_bubble_sort_case("pior", size)

    print(f"Melhor Caso: Tempo de Execução = {melhor_caso[0]:.6f}s, Quantidade de Trocas = {melhor_caso[1]}, Quantidade de Comparações = {melhor_caso[2]}")
    print(f"Caso Médio: Tempo de Execução = {medio_caso[0]:.6f}s, Quantidade de Trocas = {medio_caso[1]}, Quantidade de Comparações = {medio_caso[2]}")
    print(f"Pior Caso: Tempo de Execução = {pior_caso[0]:.6f}s, Quantidade de Trocas = {pior_caso[1]}, Quantidade de Comparações = {pior_caso[2]}")
    print("-" * 50)
