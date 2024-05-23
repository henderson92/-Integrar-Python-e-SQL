import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Paulo;"
    "Database=PYTHONSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()

comando = """INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (6, 'Henderson', 'Celular', '22/05/2024', 2500, 2)"""

cursor.execute(comando)
cursor.commit()