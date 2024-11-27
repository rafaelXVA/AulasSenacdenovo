class Cont: 
    def ocorrencia_palavras(texto):
        ocorrencia = {}
        palavra = texto.split()
    
        for palavras in palavra:
            ocorrencia[palavras] = ocorrencia.get(palavras,0)+1
        return ocorrencia