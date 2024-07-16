class Elemento:
    def __init__(self, valor):
        self.valor = valor

    def __repr__(self):
        return self.valor

def merge_sort(arr, order):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], order)
    right = merge_sort(arr[mid:], order)

    return merge(left, right, order)

def merge(left, right, order):
    result = []
    order_index = {char: i for i, char in enumerate(order)}
    i = j = 0

    while i < len(left) and j < len(right):
        if order_index[left[i].valor] <= order_index[right[j].valor]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Exemplo de uso
elementos = [
    Elemento('#'),
    Elemento('@'),
    Elemento('$'),
    Elemento('!'),
    Elemento('%')
]
sequencia = '!@#$%¨&*/'  # Sequência personalizada de caracteres
print("Ordem dos caracteres: !, @, #, $, %, ¨, &, *")
print("Sequência não ordenada: ", elementos)
print("Ordenando...\n")
sorted_elementos = merge_sort(elementos, sequencia)
print("Sequência ordenada: ", sorted_elementos)
