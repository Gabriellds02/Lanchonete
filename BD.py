import pyodbc

dados_conexao = ("Driver={SQL Server};"
                    "Server=DESKTOP-EC5CMDG;"
                    "Database=EstoqueLanchonete;")

conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()

class BandoDados:
    def __init__(self) -> None:
            
        comando = f"""INSERT INTO Tabela(coluna1, coluna2, coluna3, coluna4)
        VALUES
        ('{valor_coluna1}', '{valor_coluna2}', '{valor_coluna3}', '{valor_coluna4}')"""
        cursor.execute(comando)
        cursor.commit()

   
dados = BandoDados()