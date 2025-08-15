# Bubble sort 
def bubble_sort(v):
    for i in range(len(v)-1):
        for j in range(len(v)-i-1):
            if (v[j] > v[j+1]):
                v[j], v[j+1] = v[j+1], v[j]


lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
bubble_sort(lista)
print(f'Lista ordenada: {lista}')