from classe_agenda import *

class Menu:
    def __init__(self):
        agenda = Agenda()

        #iniciar menu
        while True:
            entrada = input('Informe a opção desejada\n1 - Novo Contato\n2 - listar Contatos\n3 - Alterar Telefone\n4 - Favoritar\n5 - Buscar Favoritos\n0 - SAIR\n')

            if entrada == '1':
                agenda.salvar_contatos()
            elif entrada == '2':
                agenda.listagem_contatos()
            elif entrada == '0':
                break
            elif entrada == '3':
                agenda.alterar_telefone()
            elif entrada == '4':
                agenda.favoritar()
            elif entrada == '5':
                agenda.buscar_favs()
            else:
                print('Opção Inválida!')