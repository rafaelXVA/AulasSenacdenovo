def produto_escalar(vetor1, vetor2):
    if len(vetor1) != len(vetor2):
        raise ValueError("Os vetores devem ter o mesmo tamanho")
    produto = sum(a * b for a, b in zip(vetor1, vetor2))
    return produto
vetor1 = [1, 2, 3]
vetor2 = [4, 5, 6]
resultado = produto_escalar(vetor1, vetor2)
print(resultado)
