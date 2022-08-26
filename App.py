from Clientes import clientes
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 100
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 100
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 5
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["padx"] = 20
        self.container9["pady"] = 5
        self.container9.pack()
        self.container10 = Frame(master)
        self.container10["padx"] = 20
        self.container10["pady"] = 5
        self.container10.pack()
        self.container11 = Frame(master)
        self.container11["padx"] = 20
        self.container11["pady"] = 5
        self.container11.pack()
        self.container12 = Frame(master)
        self.container12["padx"] = 20
        self.container12["pady"] = 5
        self.container12.pack()
        self.container13 = Frame(master)
        self.container13["padx"] = 20
        self.container13["pady"] = 5
        self.container13.pack()
        self.container14 = Frame(master)
        self.container14["padx"] = 20
        self.container14["pady"] = 10
        self.container14.pack()
        self.container15 = Frame(master)
        self.container15["pady"] = 15
        self.container15.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblcnpjcpf = Label(self.container2,
        text="CNPJ ou CPF:", font=self.fonte, width=10)
        self.lblcnpjcpf.pack(side=LEFT)

        self.txtcnpjcpf = Entry(self.container2)
        self.txtcnpjcpf["width"] = 18
        self.txtcnpjcpf["font"] = self.fonte
        self.txtcnpjcpf.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarcliente
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 30
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lblcep = Label(self.container4, text="CEP:",
        font=self.fonte, width=10)
        self.lblcep.pack(side=LEFT)

        self.txtcep = Entry(self.container4)
        self.txtcep["width"] = 30
        self.txtcep["font"] = self.fonte
        self.txtcep.pack(side=LEFT)

        self.lblendereco = Label(self.container5, text="Endereco:",
        font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)

        self.txtendereco = Entry(self.container5)
        self.txtendereco["width"] = 14
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=LEFT)

        self.lblnumero = Label(self.container5, text="Nº:",
        font=self.fonte, width=10)
        self.lblnumero.pack(side=LEFT)

        self.txtcomplemento = Entry(self.container5)
        self.txtcomplemento["width"] = 5
        self.txtcomplemento["font"] = self.fonte
        self.txtcomplemento.pack(side=LEFT)

        self.lblcomplemento = Label(self.container6, text="Complemento:",
        font=self.fonte, width=10)
        self.lblcomplemento.pack(side=LEFT)

        self.txtnumero = Entry(self.container6)
        self.txtnumero["width"] = 30
        self.txtnumero["font"] = self.fonte
        self.txtnumero.pack(side=LEFT)

        self.lblbairro= Label(self.container7, text="Bairro:",
        font=self.fonte, width=10)
        self.lblbairro.pack(side=LEFT)

        self.txtbairro = Entry(self.container7)
        self.txtbairro["width"] = 30
        self.txtbairro["font"] = self.fonte
        self.txtbairro.pack(side=LEFT)

        self.lblcidade= Label(self.container8, text="Cidade:",
        font=self.fonte, width=10)
        self.lblcidade.pack(side=LEFT)

        self.txtcidade = Entry(self.container8)
        self.txtcidade["width"] = 14
        self.txtcidade["font"] = self.fonte
        self.txtcidade.pack(side=LEFT)

        self.lblestado = Label(self.container8, text="UF:",
        font=self.fonte, width=10)
        self.lblestado.pack(side=LEFT)

        self.txtestado = Entry(self.container8)
        self.txtestado["width"] = 5
        self.txtestado["font"] = self.fonte
        self.txtestado.pack(side=LEFT)


        self.lbltelefone= Label(self.container10, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container10)
        self.txttelefone["width"] = 30
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail= Label(self.container11, text="Email::",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container11)
        self.txtemail["width"] = 30
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.bntInsert = Button(self.container12, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserircliente
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container12, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarcliente
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container12, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluircliente
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container13, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserircliente(self):
        user = clientes()

        user.cnpjcpf = self.txtcnpjcpf.get()
        user.nome = self.txtnome.get()
        user.cep = self.txtcep.get()
        user.endereco = self.txtendereco.get()
        user.numero = self.txtnumero.get()
        user.complemento = self.txtcomplemento.get()
        user.bairro = self.txtbairro.get()
        user.cidade = self.txtcidade.get()
        user.estado = self.txtestado.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()


        self.lblmsg["text"] = user.insertUser()

        self.txtcnpjcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcep.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtnumero.delete(0, END)
        self.txtcomplemento.delete(0, END)
        self.txtbairro.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtestado.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)




    def alterarcliente(self):
        user = clientes()

        user.cnpjcpf = self.txtcnpjcpf.get()
        user.nome = self.txtnome.get()
        user.cep = self.txtcep.get()
        user.endereco = self.txtendereco.get()
        user.numero = self.txtnumero.get()
        user.complemento = self.txtcomplemento.get()
        user.bairro = self.txtbairro.get()
        user.cidade = self.txtcidade.get()
        user.estado = self.txtestado.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtcnpjcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcep.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtnumero.delete(0, END)
        self.txtcomplemento.delete(0, END)
        self.txtbairro.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtestado.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)



    def excluircliente(self):
        user = clientes()

        user.idcliente = self.txtcnpjcpf.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtcnpjcpf.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtcep.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtnumero.delete(0, END)
        self.txtcomplemento.delete(0, END)
        self.txtbairro.delete(0, END)
        self.txtcidade.delete(0, END)
        self.txtestado.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)


    def buscarcliente(self):
        user = clientes()

        cnpjcpf = (self.txtcnpjcpf.get())

        self.lblmsg["text"] = user.selectUser(cnpjcpf)

        self.txtcnpjcpf.delete(0, END)
        self.txtcnpjcpf.insert(INSERT, user.cnpjcpf)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txtcep.delete(0, END)
        self.txtcep.insert(INSERT, user.cep)

        self.txtendereco.delete(0, END)
        self.txtendereco.insert(INSERT,user.endereco)

        self.txtnumero.delete(0, END)
        self.txtnumero.insert(INSERT,user.numero)

        self.txtcomplemento.delete(0, END)
        self.txtcomplemento.insert(INSERT,user.complemento)

        self.txtbairro.delete(0, END)
        self.txtbairro.insert(INSERT, user.bairro)

        self.txtcidade.delete(0, END)
        self.txtcidade.insert(INSERT,user.cidade)

        self.txtestado.delete(0, END)
        self.txtestado.insert(INSERT,user.estado)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)





root = Tk()
Application(root)
root.mainloop()