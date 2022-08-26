from Banco import Banco


class clientes(object):


    def __init__(self, cnpjcpf = "", nome = "",cep = "",endereco = "",numero = "",complemento = "",bairro = "",cidade="",estado = "", telefone = "",email = ""):
      self.info = {}
      self.cnpjcpf = str(cnpjcpf)
      self.nome = nome
      self.cep = cep
      self.endereco = endereco
      self.numero = numero
      self.complemento  = complemento
      self.bairro = bairro
      self.cidade = cidade
      self.estado = estado
      self.telefone = telefone
      self.email = email



    def insertUser(self):

      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute("insert into clientes (cnpjcpf, nome, cep, endereco, numero, complemento, bairro,"
                    " cidade, estado, telefone, email) "f"values('{str(self.cnpjcpf)}',"
                    f" {self.nome}, {self.cep},{self.endereco},{self.numero}, {self.complemento},"
                    f" {self.bairro}, {self.cidade}, {self.estado}, {self.telefone}, {self.email} )")

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
                    "',numero = '" + self.numero + "',complemento = '" + self.complemento + "',bairro = '" + self.bairro + "',cidade = '" + self.cidade + "', estado = '"
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

          c.execute("delete from clientes where cnpjcpf = " + str(self.cnpjcpf) + " ")

          banco.conexao.commit()
          c.close()

          return "Usuário excluído com sucesso!"
      except:
          return "Ocorreu um erro na exclusão do usuário"

    def selectUser(self, cnpjcpf):
      banco = Banco()
      try:

          c = banco.conexao.cursor()

          c.execute(f"select * from clientes where cnpjcpf ='{str(cnpjcpf)}'")

          for linha in c:
              self.cnpjcpf = linha[0]
              print(self.cnpjcpf)
              self.nome = linha[1]
              self.cep = linha[2]
              self.endereco = linha[3]
              self.numero = linha[4]
              self.complemento = linha[5]
              self.bairro = linha[6]
              self.cidade = linha[7]
              self.estado = linha[8]
              self.telefone = linha[9]
              self.email = linha[10]

          c.close()

          return "Busca feita com sucesso!"
      except:
          return "Ocorreu um erro na busca do usuário"




## FAZER API DO CEP
