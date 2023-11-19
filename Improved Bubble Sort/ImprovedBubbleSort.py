import random
import time

def improved_bubble_sort(arr):
    n = len(arr)
    # Defina um flag para verificar se houve trocas durante a iteração
    swapped = True
    # Inicialize o número de iterações
    iteration = 0

    while swapped:
        swapped = False
        iteration += 1
        # Itera sobre todos os elementos do vetor
        for i in range(n - iteration):
            # Compara elementos adjacentes
            if arr[i] > arr[i + 1]:
                # Troca os elementos se estiverem na ordem errada
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                # Seta a flag para True pois houve uma troca
                swapped = True

# Criando um vetor com 1000 elementos aleatórios (Caso médio: O(n))
v_caso_medio = [random.randint(1, 1000) for _ in range(1000)]
# Criando um vetor ordenado de 1000 elementos(Melhor Caso: O(n))
v_melhorCaso = list(range(1, 1001))
# Criando um vetor ordenado de 1000 elementos em ordem decrescente(Pior Caso: O(n²)):
v_piorCaso = list(range(1000, 0, -1))

# Melhor caso
start_time = time.time()
improved_bubble_sort(v_melhorCaso)
end_time = time.time()
print("Tempo de execução para o melhor caso com 1000 elementos: ", end_time - start_time)

# Caso médio
start_time = time.time()
improved_bubble_sort(v_caso_medio)
end_time = time.time()
print("Tempo de execução para o caso médio com 1000 elementos: ", end_time - start_time)

# Pior caso
start_time = time.time()
improved_bubble_sort(v_piorCaso)
end_time = time.time()
print("Tempo de execução para o pior caso com 1000 elementos: ", end_time - start_time)

# Criando um vetor com 10000 elementos aleatórios (Caso médio: O(n))
v_caso_medio1 = [random.randint(1, 10000) for _ in range(10000)]
# Criando um vetor ordenado de 10000 elementos(Melhor Caso: O(n))
v_melhorCaso1 = list(range(1, 10001))
# Criando um vetor ordenado de 10000 elementos em ordem decrescente(Pior Caso: O(n²)):
v_piorCaso1 = list(range(10000, 0, -1))

# Melhor caso
start_time = time.time()
improved_bubble_sort(v_melhorCaso1)
end_time = time.time()
print("Tempo de execução para o melhor caso com 10000 elementos: ", end_time - start_time)

# Caso médio
start_time = time.time()
improved_bubble_sort(v_caso_medio1)
end_time = time.time()
print("Tempo de execução para o caso médio com 10000 elementos: ", end_time - start_time)

# Pior caso
start_time = time.time()
improved_bubble_sort(v_piorCaso1)
end_time = time.time()
print("Tempo de execução para o pior caso com 10000 elementos: ", end_time - start_time)

# Criando um vetor com 100000 elementos aleatórios (Caso médio: O(n))
v_caso_medio2 = [random.randint(1, 100000) for _ in range(100000)]
# Criando um vetor ordenado de 100000 elementos(Melhor Caso: O(n))
v_melhorCaso2 = list(range(1, 100001))
# Criando um vetor ordenado de 100000 elementos em ordem decrescente(Pior Caso: O(n²)):
v_piorCaso2 = list(range(100000, 0, -1))

# Melhor caso
start_time = time.time()
improved_bubble_sort(v_melhorCaso2)
end_time = time.time()
print("Tempo de execução para o melhor caso com 100000 elementos: ", end_time - start_time)

# Caso médio
start_time = time.time()
improved_bubble_sort(v_caso_medio2)
end_time = time.time()
print("Tempo de execução para o caso médio com 100000 elementos: ", end_time - start_time)

# Pior caso
start_time = time.time()
improved_bubble_sort(v_piorCaso2)
end_time = time.time()
print("Tempo de execução para o pior caso com 100000 elementos: ", end_time - start_time)
