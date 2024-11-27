class veiculo:
    def __init__(self,velocidade,modelo):
        self.velocidade=velocidade
        self.modelo=modelo
    def aumentarV(self,novaV):
        return self.velocidade+novaV