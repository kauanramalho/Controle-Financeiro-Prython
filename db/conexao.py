import mysql.connector

conexao = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "SUA_SENHA",
    database = "controle_financeiro"
)

cursor = conexao.cursor()