# Merge Sort 
def merge_sort(v,ini,fim):
    if ini < fim:
        meio = (ini + fim) // 2
        merge_sort(v, ini, meio)
        merge_sort(v, meio+1, fim)
        intercala(v, ini, meio, fim)


def intercala(v, ini, meio, fim):
    l = v[ini:meio+1]
    r = v[meio+1:fim+1]
    l.append(999) #sentinela
    r.append(999) #sentinela
    i = 0
    j = 0
    for k in range(ini, fim+1):
        if l[i] <= r[j]:
            v[k] = l[i]
            i += 1
        else:
            v[k] = r[j]
            j += 1

       

