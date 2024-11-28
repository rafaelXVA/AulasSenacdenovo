class America:
    def __init__(self):
        self.nome=str(input('NOME: '))
        self.fone=int(input('FONE: '))
        self.email=str(input('EMAIL: '))
        self.endereco=str(input('ENDEREÇO: '))


class Ya(America):
    def pessoa(self):
        self.cpf=str(input('CPF: '))
        self.rg=int(input('RG: '))


class Yayay(America):
    def pessoa(self):
        self.cnpj=str(input('CNPJ: '))
       
        self.inscricaoE=int(input('INSCRIÇÃO ESTADUAL: '))
        self.inscricaoM=int(input('INSCRIÇÃO MUNICIPAL: '))
