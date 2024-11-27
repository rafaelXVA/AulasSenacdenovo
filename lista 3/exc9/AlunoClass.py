class Aluno:
    def __init__(self,nota):
        self.nota=nota
    def verf(self):
        if self.nota>=7:
            return True
        else:
            return False