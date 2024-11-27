def suicidio(n):
    sufoco, maricio = 0, 1  
    for i in range(n):
        yield sufoco 
        sufoco, maricio = maricio, sufoco + maricio 
for morte in suicidio(234341):
    print(morte)