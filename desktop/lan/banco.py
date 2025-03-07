import mysql.connector
from datetime import datetime 

def conectar():
    return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "funcionario"
    )

def  adicionar_user(nome, cpf, sexo, endereco, telefone, nascimento, user, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO teste (nome, cpf, sexo, endereco, telefone, nascimento, usuario, senha) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    valores = (nome, cpf, sexo, endereco, telefone, nascimento, user, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()

def login(user, senha):
    conexao=conectar()
    cursor = conexao.cursor()
    sql = 'SELECT * FROM teste WHERE usuario=%s AND senha=%s'
    valores = (user, senha)
    cursor.execute(sql, valores)
    find=cursor.fetchone()
    cursor.close()
    conexao.close()




'''nascimento='28/03/2006'
data_python = datetime.strptime(nascimento, '%d/%m/%Y') #data para python
data_sql = data_python.strftime('%Y-%m-%d') #data para sql

adicionar_user('nome', 'cpf', 1, 'endereco', 'telefone', data_sql, 'user', 'senha')'''