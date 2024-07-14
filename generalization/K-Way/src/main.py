def k_way_merge_sort(arr, k=2):
    if len(arr) <= 1:
        return arr
    
    # Dividir o array em k partes
    subarrays = []
    size = len(arr) // k
    for i in range(k):
        start_index = i * size
        end_index = (i + 1) * size if i != k - 1 else len(arr)
        subarrays.append(arr[start_index:end_index])
    
    # Recursivamente ordenar cada subarray
    sorted_subarrays = [k_way_merge_sort(subarray, k) for subarray in subarrays]
    
    # Mesclar todos os subarrays ordenados
    return merge(sorted_subarrays)

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
arr = [38, 27, 43, 3, 9, 82, 10]
k = 3  # Dividir o array em 3 partes
sorted_arr = k_way_merge_sort(arr, k)
print(sorted_arr)
