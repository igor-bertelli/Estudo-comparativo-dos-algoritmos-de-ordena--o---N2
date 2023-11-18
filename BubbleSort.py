import random

def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr

# Cria um vetor de 100.000 elementos com números aleatórios
vetor = [random.randint(1, 100000) for _ in range(100000)]

print("Vetor não ordenado:")
print(vetor)

# Aplica o Bubble Sort para ordenar o vetor
bubble_sort(vetor)

print("\nVetor ordenado:")
print(vetor)
