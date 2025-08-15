# Definição de uma classe Computador com atributos e métodos
class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def Ligar(self):
        print('Estou ligando')
    
    def Desligar(self):
        print('Estou desligando')

    def exibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)


computador1 = Computador('Asus', '8gb', 'Nvidia')
computador1.Ligar()
computador1.Desligar()
computador1.exibirInformacoesDesteComputador()

# ligar, Desligar, Exibir Configuração