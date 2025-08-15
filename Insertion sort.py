# Insertion sort  
def insertion_sort(v):
    for i in range(1, len(v)):
        x = v[i]
        j = i-1
        while j >= 0 and x < v[j]:
            v[j+1] = v[j]
            j -= 1
            v[j+1] = x

lista = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
insertion_sort(lista)
print(f'Lista ordenada: {lista}')