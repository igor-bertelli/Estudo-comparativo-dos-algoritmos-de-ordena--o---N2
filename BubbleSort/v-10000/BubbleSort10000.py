import random
import time

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Criando um vetor ordenado de 10000 elementos(Melhor Caso: O(n))
v_melhorCaso = list(range(1, 10001))
# Criando um vetor com 10000 elementos aleatórios (Caso médio: O(n))
v_CasoMedio = [random.randint(1, 10000) for _ in range(10000)]
# Criando um vetor ordenado de 10000 elementos em ordem decrescente(Pior Caso: O(n²)):
v_piorCaso = list(range(10000, 0, -1))

# Melhor caso
start_time = time.time()
bubble_sort(v_melhorCaso)
end_time = time.time()
print("Tempo de execução para o melhor caso: ", end_time - start_time)

# Caso médio
start_time = time.time()
bubble_sort(v_CasoMedio)
end_time = time.time()
print("Tempo de execução para o caso médio: ", end_time - start_time)

# Pior caso
start_time = time.time()
bubble_sort(v_piorCaso)
end_time = time.time()
print("Tempo de execução para o pior caso: ", end_time - start_time)



