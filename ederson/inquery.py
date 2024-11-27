from InquirerPy import inquirer
'''
nome=inquirer.text("qual seu nome").execute()
cor=inquirer.select("qual é sua cor favorita?",
                    choices=['azul','vermelho','verde']).execute()'''


def valida_email(val):
    if '@' not in val:
        raise ValueError("Por favor, insira um e-mail válido.")
    return val
email=inquirer.text("qual seu email?", validate=valida_email).execute()