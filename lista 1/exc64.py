import random
import string
def gera_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha
tamanho = 12 
senha_gerada = gera_senha(tamanho)
print(f"A senha gerada é: {senha_gerada}")