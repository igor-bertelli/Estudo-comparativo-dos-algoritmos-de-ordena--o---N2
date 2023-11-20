import random
import time

def swap(arr, a, b, trocas):
    arr[a], arr[b] = arr[b], arr[a]
    trocas[0] += 1

def partition(arr, low, high, trocas, comparacoes):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        comparacoes[0] += 1
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j, trocas)

    swap(arr, i + 1, high, trocas)
    return i + 1

def quickSort(arr, trocas, comparacoes):
    stack = [(0, len(arr) - 1)]

    while stack:
        low, high = stack.pop()

        if low < high:
            pi = partition(arr, low, high, trocas, comparacoes)

            if pi - low < high - pi:
                stack.append((low, pi - 1))
                stack.append((pi + 1, high))
            else:
                stack.append((pi + 1, high))
                stack.append((low, pi - 1))

def performQuickSort(arr):
    trocas = [0]
    comparacoes = [0]
    low = 0
    high = len(arr) - 1
    quickSort(arr, trocas, comparacoes)
    return trocas[0], comparacoes[0]

# Tamanhos dos vetores
tamanhos = [1000, 10000, 100000]

for tamanho in tamanhos:
    vetorMelhorCaso = list(range(tamanho))
    vetorCasoMedio = [random.randint(0, tamanho) for _ in range(tamanho)]
    vetorPiorCaso = list(range(tamanho, 0, -1))

    # Medir o tempo de execução, quantidade de trocas e comparações para o Melhor Caso
    startMelhorCaso = time.time()
    trocasMelhorCaso, comparacoesMelhorCaso = performQuickSort(vetorMelhorCaso.copy())
    endMelhorCaso = time.time()
    tempoMelhorCaso = endMelhorCaso - startMelhorCaso

    # Medir o tempo de execução, quantidade de trocas e comparações para o Caso Médio
    startCasoMedio = time.time()
    trocasCasoMedio, comparacoesCasoMedio = performQuickSort(vetorCasoMedio.copy())
    endCasoMedio = time.time()
    tempoCasoMedio = endCasoMedio - startCasoMedio

    # Medir o tempo de execução, quantidade de trocas e comparações para o Pior Caso
    startPiorCaso = time.time()
    trocasPiorCaso, comparacoesPiorCaso = performQuickSort(vetorPiorCaso.copy())
    endPiorCaso = time.time()
    tempoPiorCaso = endPiorCaso - startPiorCaso

    # Exibir resultados
    print(f"Tamanho do vetor: {tamanho}")
    print("Melhor Caso:")
    print(f"Tempo de Execucao: {tempoMelhorCaso:.6f} segundos")
    print(f"Quantidade de Trocas: {trocasMelhorCaso}")
    print(f"Quantidade de Comparacoes: {comparacoesMelhorCaso}")

    print("Caso Medio:")
    print(f"Tempo de Execucao: {tempoCasoMedio:.6f} segundos")
    print(f"Quantidade de Trocas: {trocasCasoMedio}")
    print(f"Quantidade de Comparacoes: {comparacoesCasoMedio}")

    print("Pior Caso:")
    print(f"Tempo de Execucao: {tempoPiorCaso:.6f} segundos")
    print(f"Quantidade de Trocas: {trocasPiorCaso}")
    print(f"Quantidade de Comparacoes: {comparacoesPiorCaso}")

    print("----------------------------------------")
