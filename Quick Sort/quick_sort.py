import time
import random

# Gerando vetores
vetores = [1000, 10000, 100000]

def quicksort(arr):
    if len(arr) <= 1:
        return arr, 0
    else:
        # Escolhe um pivô (neste caso, o elemento do meio)
        pivot = arr[len(arr) // 2]
        
        # Particiona os elementos em duas sublistas
        menores, trocas_menores = quicksort([x for x in arr if x < pivot])
        iguais = [x for x in arr if x == pivot]
        maiores, trocas_maiores = quicksort([x for x in arr if x > pivot])
        
        # Aplica recursivamente o QuickSort nas sublistas
        return menores + iguais + maiores, trocas_menores + len(menores) + trocas_maiores

for i in vetores:
    # Melhor caso (lista ordenada)
    v_melhorCaso = list(range(i))
    start_time = time.time()
    sorted_list, trocas = quicksort(v_melhorCaso)
    end_time = time.time()
    print(f"Tempo de execução para o melhor caso com {i} elementos: ", end_time - start_time)
    print(f"Quantidade de trocas para o melhor caso com {i} elementos: ", trocas)

    # Caso médio (lista aleatória)
    v_CasoMedio = random.sample(range(i), i)
    start_time = time.time()
    sorted_list, trocas = quicksort(v_CasoMedio)
    end_time = time.time()
    print(f"Tempo de execução para o caso médio com {i} elementos: ", end_time - start_time)
    print(f"Quantidade de trocas para o caso médio com {i} elementos: ", trocas)

    # Pior caso (lista ordenada de forma decrescente)
    v_piorCaso = list(range(i, 0, -1))
    start_time = time.time()
    sorted_list, trocas = quicksort(v_piorCaso)
    end_time = time.time()
    print(f"Tempo de execução para o pior caso com {i} elementos: ", end_time - start_time)
    print(f"Quantidade de trocas para o pior caso com {i} elementos: ", trocas)
    