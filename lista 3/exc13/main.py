from VeiculoClass import *

carro=veiculo(20,'jetta')

while True:
    test=int(input(f'carro modelo {carro.modelo} está a {carro.velocidade}km/h\ndeseja aumentar a velocidade em quantos km/h?\n'))
    veiculo.aumentarV(carro,test)