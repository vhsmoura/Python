# Exemplo de uso do método append e pop
growth: list[str] = []

growth.append('A')  ### append = adiciona um elemento
growth.append('B')
growth.append('C')

musculacao = growth.pop()  ### Tirou a letra C

print(growth, musculacao)