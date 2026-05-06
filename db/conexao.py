import mysql.connector
from mysql.connector import Error

try:
    conexao = mysql.connector.connect(
        host="localhost",
        user="root",
        password="17103012Kb!",
        database="controle_financeiro",
    )
except Error as erro:
    print("Nao foi possivel conectar ao banco de dados.")
    print(f"Erro: {erro}")
    raise SystemExit

cursor = conexao.cursor()
