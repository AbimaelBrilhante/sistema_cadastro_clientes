from Banco import Banco


class clientes(object):


    def __init__(self, cnpjcpf = "000.000.000-00", nome = "",cep = "",endereco = "",
                 numero = "",bairro = "",cidade="",estado = "", telefone = "",
    email = ""):
      self.info = {}
      self.cnpjcpf = cnpjcpf
      self.nome = nome
      self.cep = cep
      self.endereco = endereco
      self.numero = numero
      self.bairro = bairro
      self.cidade = cidade
      self.estado = estado
      self.telefone = telefone
      self.email = email



    def insertUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("insert into clientes (cnpjcpf, nome, cep, endereco, numero, bairro, cidade, estado, telefone, email) "
                    "values('"+ self.cnpjcpf + "', '" + self.nome + "', '" + self.cep + "','"+self.endereco + "','"+self.numero + "','"
                    +self.bairro + "', '"+self.cidade + "', '" + self.estado + "', '" +self.telefone + "', '" + self.email + "' )")

          banco.conexao.commit()
          c.close()

          return "Usuário cadastrado com sucesso!"
      except:
          return "Ocorreu um erro na inserção do usuário"

    def updateUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("update clientes set nome = '" + self.nome + "',cep = '" + self.cep + "',endereco = '" + self.endereco +
                    "',numero = '" + self.numero + "',bairro = '" + self.bairro + "',cidade = '" + self.cidade + "', estado = '"
                    + self.estado +"', telefone = '" + self.telefone + "', email = '" + self.email +
                    "' where cnpjcpf = " + self.cnpjcpf + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário atualizado com sucesso!"
      except:
          return "Ocorreu um erro na alteração do usuário"

    def deleteUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("delete from clientes where cnpjcpf = " + self.cnpjcpf + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, cnpjcpf):
      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("select * from clientes where cnpjcpf = " + cnpjcpf + "  ")

          for linha in c:
              self.cnpjcpf = linha[0]
              self.nome = linha[1]
              self.cep = linha[2]
              self.endereco = linha[3]
              self.numero = linha[4]
              self.bairro = linha[5]
              self.cidade = linha[6]
              self.estado = linha[7]
              self.telefone = linha[8]
              self.email = linha[9]

          c.close()

          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do usuário"