import sqlite3

class Banco():

    def __init__(self):
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists clientes (
                     cnpjcpf text primary key  ,                     
                     nome text,
                     cep text,
                     endereco text,
                     numero integer,
                     complemento text,
                     bairro text,
                     cidade text,
                     estado text,
                     telefone text,
                     email text)""")
        self.conexao.commit()
        c.close()