from Banco import Banco


class clientes(object):


    def __init__(self, idcliente = 0, nome = "", telefone = "",
    email = "", cliente = "", senha = ""):
      self.info = {}
      self.idcliente = idcliente
      self.nome = nome
      self.telefone = telefone
      self.email = email
      self.cliente = cliente
      self.senha = senha


    def insertUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("insert into clientes (nome, telefone, email,cliente, senha) "
                    "values('" + self.nome + "', '" +self.telefone + "', '" + self.email + "', '" +self.cliente + "', '" + self.senha + "' )")

          banco.conexao.commit()
          c.close()

          return "Usuário cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("update clientes set nome = '" + self.nome + "',telefone = '" + self.telefone + "', email = '"
                    + self.email +"', cliente = '" + self.cliente + "', senha = '" + self.senha +
                    "' where idcliente = " + self.idcliente + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("delete from clientes where idcliente = " + self.idcliente + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, idcliente):
      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("select * from clientes where idcliente = " + idcliente + "  ")

          for linha in c:
              self.idcliente = linha[0]
              self.nome = linha[1]
              self.telefone = linha[2]
              self.email = linha[3]
              self.cliente = linha[4]
              self.senha = linha[5]

          c.close()

          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do usuário"