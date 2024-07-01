class Elemento:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
        return f'{self.nome}: {self.idade} anos'

def merge_sort(arr, key):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key)
    right = merge_sort(arr[mid:], key)

    return merge(left, right, key)

def merge(left, right, key):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if getattr(left[i], key) <= getattr(right[j], key):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

# Exemplo de uso
arr = [
    Elemento('Alice', 34),
    Elemento('Bob', 23),
    Elemento('Charlie', 25),
    Elemento('Diana', 30),
    Elemento('Edward', 28)
]
key = 'idade'  # Campo pelo qual queremos ordenar
sorted_arr = merge_sort(arr, key)

for elemento in sorted_arr:
    print(elemento)
