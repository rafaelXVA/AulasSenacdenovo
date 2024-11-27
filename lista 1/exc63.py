def calcula_juros_compostos(capital, taxa, tempo):
    montante = capital * (1 + taxa) ** tempo
    return montante
capital = 1000  
taxa = 0.05     
tempo = 3 
montante = calcula_juros_compostos(capital, taxa, tempo)
print(f"O montante final após {tempo} anos é: R${montante:.2f}")