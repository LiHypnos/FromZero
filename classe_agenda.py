from classe_contato import *

class Agenda:
    def __init__(self):
        self.listaContatos = []

    def salvar_contatos(self):
        entrada_cod = str(len(self.listaContatos)+1)
        entrada_nome= input('Informe  o nome: ')
        entrada_telefone = input('Informe o telefone: ')
        fav = False
        self.listaContatos.append(Contato(cod=entrada_cod, nome=entrada_nome, telefone=entrada_telefone))
        print('O código da sua conta é:',entrada_cod,'*')
        print('Contato Salvo!')
        print('_______________________________________________________________________________________________________')

    def listagem_contatos(self):
        for i in range(len(self.listaContatos)):
            print('Código:',self.listaContatos[i].cod,'/',
                  'Nome:',self.listaContatos[i].nome,'/',
                  'Telefone:',self.listaContatos[i].telefone,'/') #print(self.listaContatos[0].nome
            if self.listaContatos[i].star == True:
                print('Favoritado √',self.listaContatos[i].star)
            print('___________________________________________________________________________________________________')

    #def alterar_telefone(self):
        #entrar_alterar = int(input('Informe o código da conta para alterar o telefone:\n'))

        #self.listaContatos[int(input('Digite o numero da conta\n'))].telefone = input('Informe o novo número de telefone:\n')
        #print('Alterado com Sucesso!')

    def alterar_telefone(self):
        entrada = input ('Informe o código do contato:')
        for i in range(len(self.listaContatos)):
            if entrada == self.listaContatos[i].cod:
                self.listaContatos[i].telefone = input('Novo Telefone:\n')
                print('_______________________________________________________________________________________________________')
            else:
                cont += 1
                if cont == len(self.listaContatos):
                    print('Código não existente')
                print('_______________________________________________________________________________________________________')
    #def alterar_telefone(self):
    #entrada = input ('Informe o código do contato:')
    #for i in range(len(self.listaContatos)):
     #if entrada == self.listaContatos[i].cod:
     #self.listaContatos[i].telefone = input('Novo Telefone:\n')

    def favoritar(self):
        entrar_alterar_fav = int(input('Informe o código da conta para favoritar:\n'))
        for i in range(len(self.listaContatos)):
            if entrar_alterar_fav == self.listaContatos[i].cod:
                self.listaContatos[i].star = input(True)
        print('_______________________________________________________________________________________________________')
    def buscar_favs(self):
        for i in range(len(self.listaContatos)):
            if self.listaContatos[i].star == True:
                print(self.listaContatos[i].nome)

