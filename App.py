from Clientes import clientes
from tkinter import *


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
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
        self.container5["padx"] = 20
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
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack ()

        self.lblidcliente = Label(self.container2,
        text="idcliente:", font=self.fonte, width=10)
        self.lblidcliente.pack(side=LEFT)

        self.txtidcliente = Entry(self.container2)
        self.txtidcliente["width"] = 10
        self.txtidcliente["font"] = self.fonte
        self.txtidcliente.pack(side=LEFT)

        self.btnBuscar = Button(self.container2, text="Buscar",
        font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarcliente
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
        font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        self.lbltelefone = Label(self.container4, text="Telefone:",
        font=self.fonte, width=10)
        self.lbltelefone.pack(side=LEFT)

        self.txttelefone = Entry(self.container4)
        self.txttelefone["width"] = 25
        self.txttelefone["font"] = self.fonte
        self.txttelefone.pack(side=LEFT)

        self.lblemail= Label(self.container5, text="E-mail:",
        font=self.fonte, width=10)
        self.lblemail.pack(side=LEFT)

        self.txtemail = Entry(self.container5)
        self.txtemail["width"] = 25
        self.txtemail["font"] = self.fonte
        self.txtemail.pack(side=LEFT)

        self.lblcliente= Label(self.container6, text="Usuário:",
        font=self.fonte, width=10)
        self.lblcliente.pack(side=LEFT)

        self.txtcliente = Entry(self.container6)
        self.txtcliente["width"] = 25
        self.txtcliente["font"] = self.fonte
        self.txtcliente.pack(side=LEFT)

        self.lblsenha= Label(self.container7, text="Senha:",
        font=self.fonte, width=10)
        self.lblsenha.pack(side=LEFT)

        self.txtsenha = Entry(self.container7)
        self.txtsenha["width"] = 25
        self.txtsenha["show"] = "*"
        self.txtsenha["font"] = self.fonte
        self.txtsenha.pack(side=LEFT)

        self.bntInsert = Button(self.container8, text="Inserir",
        font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserircliente
        self.bntInsert.pack (side=LEFT)

        self.bntAlterar = Button(self.container8, text="Alterar",
        font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarcliente
        self.bntAlterar.pack (side=LEFT)

        self.bntExcluir = Button(self.container8, text="Excluir",
        font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluircliente
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()


    def inserircliente(self):
        user = clientes()

        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.cliente = self.txtcliente.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.insertUser()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcliente.delete(0, END)
        self.txtsenha.delete(0, END)



    def alterarcliente(self):
        user = clientes()

        user.idcliente = self.txtidcliente.get()
        user.nome = self.txtnome.get()
        user.telefone = self.txttelefone.get()
        user.email = self.txtemail.get()
        user.cliente = self.txtcliente.get()
        user.senha = self.txtsenha.get()

        self.lblmsg["text"] = user.updateUser()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcliente.delete(0, END)
        self.txtsenha.delete(0, END)



    def excluircliente(self):
        user = clientes()

        user.idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = user.deleteUser()

        self.txtidcliente.delete(0, END)
        self.txtnome.delete(0, END)
        self.txttelefone.delete(0, END)
        self.txtemail.delete(0, END)
        self.txtcliente.delete(0, END)
        self.txtsenha.delete(0, END)


    def buscarcliente(self):
        user = clientes()

        idcliente = self.txtidcliente.get()

        self.lblmsg["text"] = user.selectUser(idcliente)

        self.txtidcliente.delete(0, END)
        self.txtidcliente.insert(INSERT, user.idcliente)

        self.txtnome.delete(0, END)
        self.txtnome.insert(INSERT, user.nome)

        self.txttelefone.delete(0, END)
        self.txttelefone.insert(INSERT,user.telefone)

        self.txtemail.delete(0, END)
        self.txtemail.insert(INSERT, user.email)

        self.txtcliente.delete(0, END)
        self.txtcliente.insert(INSERT, user.cliente)

        self.txtsenha.delete(0, END)
        self.txtsenha.insert(INSERT,user.senha)



root = Tk()
Application(root)
root.mainloop()