# Função recursiva para calcular o fatorial de um número
def fatorial (numero):
    if numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial (numero - 1)
    
x = int(input('Digite um número para calcular seu fatorial: '))
res = fatorial (x)
print('O fatorial de %d é %d' % (x, res))

def f(n):
    if n < 2:
        return n
    else:
        return f(n - 1) + f(n - 2)  