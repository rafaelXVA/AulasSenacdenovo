class Alt:
    def alternar_maiusculas(texto):
        texto2=''
        for i in range(0, len(texto)):
            if(i%2):
                texto2 += texto[i].lower()
            else:
                texto2 += texto[i].upper()
        return texto2