import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=Paulo;"
    "Database=PYTHONSQL;"
)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")

cursor = conexao.cursor()



comando = f"""INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, quantidade)
VALUES
    (7, 'Silva', 'Painel Solar', '22/04/2023', 2500, 2 )"""


cursor.execute(comando)
cursor.commit()