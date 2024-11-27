from LivroClass import *

livro1=Livro(10,'Homem Torto')
livro2=Livro(20,'Trono de vidro')
livro3=Livro(5,'hq-Anakin Skywalker')

while True:
    test=input()
    if test=='colocar':
        test=input()
        if test=='livro1':
            Livro.colocar(livro1)
        elif test=='livro2':
            Livro.colocar(livro2)
        else:
            Livro.colocar(livro3)
    if test=='tirar':
        test+input()
        if test=='livro1':
            Livro.tirar(livro1)
        elif test=='livro2':
            Livro.tirar(livro2)
        else:
            Livro.tirar(livro3)
    if test=='mostrar':
        test=input()
        if test=='livro1':
            Livro.mostrar(livro1)
        elif test=='livro2':
            Livro.mostrar(livro2)
        else:
            Livro.mostrar(livro3)