def k_way_merge_sort(arr, k=2, level=0):
    if len(arr) <= 1:
        return arr

    # Se o tamanho do array for menor que k, não dividimos mais
    if len(arr) < k:
        print(f"{'  ' * level}Analisando: {arr}")
        sorted_arr = sorted(arr)
        print(f"{'  ' * level}Mesclando: {sorted_arr}")
        return sorted_arr

    # Dividir o array em k partes
    subarrays = []
    size = len(arr) // k
    for i in range(k):
        start_index = i * size
        end_index = (i + 1) * size if i != k - 1 else len(arr)
        if start_index < len(arr):  # Certificar que o subarray não está vazio
            subarrays.append(arr[start_index:end_index])
    
    print(f"{'  ' * level}Dividindo: {subarrays}")
    
    # Recursivamente ordenar cada subarray
    sorted_subarrays = [k_way_merge_sort(subarray, k, level + 1) for subarray in subarrays]
    
    # Mesclar todos os subarrays ordenados
    merged = merge(sorted_subarrays)
    print(f"{'  ' * level}Mesclando: {merged}")
    return merged

def merge(subarrays):
    import heapq
    # Criar uma fila de prioridade com todos os primeiros elementos dos subarrays
    heap = [(subarray[0], i, 0) for i, subarray in enumerate(subarrays) if subarray]
    heapq.heapify(heap)
    
    result = []
    while heap:
        # Pegar o menor elemento do heap
        val, subarray_idx, element_idx = heapq.heappop(heap)
        result.append(val)
        
        # Adicionar o próximo elemento do mesmo subarray ao heap, se houver
        if element_idx + 1 < len(subarrays[subarray_idx]):
            next_tuple = (subarrays[subarray_idx][element_idx + 1], subarray_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)
    
    return result

# Exemplo de uso
arr = [38, 27, 43, 3, 9, 82, 10, 7, 52, 100]
k = 3  # Dividir o array em 3 partes
print("Array original:", arr)
print("Será dividido em", k, "partes por vez")
print("Ordenando...\n")
sorted_arr = k_way_merge_sort(arr, k)
print("\nArray ordenado final:", sorted_arr)
