# EXERCÍCIO 1 - FILAS
# IMPLEMENTE um programa que leia a idade dos clientes 
# e organize duas filas, prioritária e normal e atenda,
# a cada dois prioritário, um cliente normal - usando recurso filas 

class FilaBanco:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    
    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > 60:
                maxi = i
        item = self.items[maxi]
        self.items[maxi:maxi+1] = []
        return item
    
prioritario = FilaBanco()
normal = FilaBanco()

numprioritario = 0
numnormal = 0
numidosos = 0
numjovens = 0
while True:
    cliente = int(input('DIGITE SUA IDADE OU ZERO PRA SAIR: '))

    if cliente < 0:
        print('INVÁLIDO')
        continue

    if cliente > 60:
        numidosos += 1
        numprioritario += 1
        prioritario.insert(numprioritario)
        print('TOTAL DE IDOSOS É: {}'.format(numidosos))

    elif cliente != 0:
        numjovens += 1
        numnormal += 1
        normal.insert(numnormal)
        print('TOTAL DE JOVENS: {}'.format(numjovens))
    else:
        break
print('-='*20)
print('ORDEM DAS FILAS:')
print('-='*20)
while len(prioritario.items) != 0 or  len(normal.items) != 0:  #contando de dois em dois
        cont = 0
        for n in range(2):
            if len(prioritario.items) != 0:
                print('ATENDIMENTO PRIORITÁRIO')
                print('P ', prioritario.remove())
        if len(normal.items) != 0:
            print('ATENDIMENTO NORMAL')
            print('N ', normal.remove())


