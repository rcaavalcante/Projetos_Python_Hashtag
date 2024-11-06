import sqlite3

# Abrir uma conexão com o banco de dados
data_base = r'/Users/rafaellacavalcante/PycharmProjects/pythonProject/CodigosHashtag/IntegrandoPythonSQL/salarios.sqlite'
dados_conexao = ("Driver={SQLite3 ODBC Driver};"
      "Server=localhost;"
      f"Database=data_base;")
conn = sqlite3.connect(dados_conexao)
print('Conexão bem sucedida')
# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Criar o comando SQL
cursor.execute('SELECT * FROM Salaries')
valores = cursor.fetchall()
print(valores[:10])
