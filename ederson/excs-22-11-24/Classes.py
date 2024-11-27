class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor=cor
        self.circunferencia=circunferencia
        self.material=material
    def troca_cor(self,cor2):
        self.cor=cor2
    def mostra_cor(bola):
        print(bola.cor)

class Quadrado:
    def __init__(self,Tlado):
        self.Tlado=Tlado
    def mostrar_area(self):
        print(self.Tlado*self.Tlado)
    def mudar_lado(self,lado2):
        self.Tlado=lado2

class Retangulo:
    def __init__(self,largura,comprimento):
        self.largura=largura
        self.comprimento=comprimento
    def mostrar_lado(retangulo):
        print('comprimento: ',retangulo.comprimento)
        print('largura: ',retangulo.largura)
    def mudar_lados(self,comprimento2,largura2):
        self.comprimento=comprimento2
        self.largura=largura2
    def area(self):
        print(self.largura*self.comprimento)
    def perimetro(self):
        print(self.largura+self.comprimento)
class Pessoa:
    def __init__(self,nome,idade,peso,altura):
        self.nome=nome
        self.idade=idade
        self.peso=peso
        self.altura=altura
    def crescer(self,anos):
        cont=0
        if self.idade<21:    
            while self.idade<21:
                self.altura+0.05
                cont=+cont
            print(f'peso de {self.altura}\nidade de {self.idade+cont}')
        else:
            print('não cresce mais')

class Tv:
    def __init__(self,canal,volume):
        self.canal=canal
        self.volume=volume
    def aumentarVolume(self,test):
        if test=='baixar' and self.volume>=0:
            self.volume-1
        elif test=='aumentar' and self.volume<=10:
            self.volume+1
    def trocarCanal(self,test):
        if test=='baixar' and self.canal>=0:
            self.canal-1
        elif test=='aumentar' and self.canal<=10:
            self.canal+1
        else:
            print('opção inválida')
class BichinhoVirtual:
    def __init__(self,nome,fome,saude,idade,humor):
        self.nome=nome
        self.fome=fome
        self.saude=saude
        self.idade=idade
        self.humor=humor
    def humor(self):
        if self.fome=='satisfeito' and self.saude=='saudavel':
            humor='neutro'
            return humor
        if self.fome==''
class BombaDeCombustivel:
    def __init__(self):
        