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

# Exemplo com um vetor de 1000 elementos preenchidos aleatoriamente
import random

# Gerando um vetor com 1000 elementos aleatórios
vetor = [random.randint(1, 1000) for _ in range(1000)]

print("Vetor antes da ordenação:")
print(vetor)

# Chamando a função para ordenar o vetor
improved_bubble_sort(vetor)

print("\nVetor após a ordenação:")
print(vetor)
