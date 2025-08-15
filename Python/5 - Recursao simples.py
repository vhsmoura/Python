# Exemplo de recursão simples
def f1(n):
    if n >= 1:
        return 1
    
    else:
        return n * f1(n - 1)

print(f1(4))

###  Para qualquer valor maior ou igual a 1, o programa sempre vai entrar no “if”, retornando o valor 1.

def fib_it(n):
    res = na, b = 0,1
    for k in range(2, n+1):
        res = a + b
        a, b = b, res
        return res
    
