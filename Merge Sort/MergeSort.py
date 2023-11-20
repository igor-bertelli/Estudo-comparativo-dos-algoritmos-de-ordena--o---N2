import time
import random

def merge(left, right, compare):
    result = []
    i = j = comp = trocas = 0
    while i < len(left) and j < len(right):
        comp += 1
        if compare(left[i], right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            trocas += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result, comp, trocas

def merge_sort(arr, compare = lambda x, y: x < y):
    if len(arr) < 2:
        return arr[:], 0, 0
    else:
        middle = len(arr) // 2
        left, comp_left, trocas_left = merge_sort(arr[:middle], compare)
        right, comp_right, trocas_right = merge_sort(arr[middle:], compare)
        merged, comp_merge, trocas_merge = merge(left, right, compare)
        return merged, comp_left + comp_right + comp_merge, trocas_left + trocas_right + trocas_merge

sizes = [1000, 10000, 100000]
for size in sizes:
    # Melhor caso
    arr = list(range(size))
    start_time = time.time()
    sorted_arr, comp, trocas = merge_sort(arr)
    end_time = time.time()
    print(f"Melhor caso com {size} elementos - Tempo: {end_time - start_time}, Comparações: {comp}, Trocas: {trocas}")

    # Caso médio
    arr = random.sample(range(size), size)
    start_time = time.time()
    sorted_arr, comp, trocas = merge_sort(arr)
    end_time = time.time()
    print(f"Caso médio com {size} elementos - Tempo: {end_time - start_time}, Comparações: {comp}, Trocas: {trocas}")

    # Pior caso
    arr = list(range(size, 0, -1))
    start_time = time.time()
    sorted_arr, comp, trocas = merge_sort(arr, compare = lambda x, y: x > y)
    end_time = time.time()
    print(f"Pior caso com {size} elementos - Tempo: {end_time - start_time}, Comparações: {comp}, Trocas: {trocas}")