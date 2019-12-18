from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeGrupos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, grupo):
        id_elemento = grupo['id_grupo']

        elemento = self.criar_elemento(dados=grupo)

        header = TKUtils.obter_container(master=elemento)
        lista = TKUtils.obter_container(master=elemento)
        body = TKUtils.obter_container(master=elemento)

        elemento.header = self.criar_header(header)
        elemento.lista = self.criar_lista(lista)
        elemento.body = self.criar_body(body)

        self.elementos.append(elemento)

        self.mudar_estado(id_elemento, 'id_grupo', grupo['em_uso'])

    def expandir(self, elemento):
        header = elemento.header
        lista = elemento.lista
        body = elemento.body

        if elemento.selecionado:
            header.label.configure(width=header.label.cnf['width'], height=2)

            header.botao_sortear.pack_configure(side='left')
            header.botao_remover.pack_configure(side='left')

            lista.pack_forget()
            body.pack_forget()

            elemento.selecionado = False
        else:
            header.label.configure(width=110, height=3)

            header.botao_remover.pack_forget()
            header.botao_sortear.pack_forget()

            lista.pack_configure()
            body.pack_configure()

            elemento.selecionado = True

    def criar_header(self, header):
        id_elemento = header.master.dados['id_grupo']

        cnf, pack = {}, {}

        cnf['text'] = header.master.dados['nome']
        cnf['bg'] = 'green'
        cnf['width'] = 92

        header.label = self.criar_label(master=header, cnf=cnf, pack=pack)
        header.botao_sortear = self.criar_botao_sortear(master=header)
        header.botao_remover =\
            self.criar_botao_remover(master=header, id_elemento=id_elemento)

        return header

    def criar_body(self, body):
        cnf, pack = {}, {}

        cnf['bg'] = 'green'
        cnf['fg'] = 'white'
        cnf['height'] = 3
        pack['side'] = 'left'

        cnf['text'] =\
            f'Total de {len(body.master.dados["integrantes"])} integrantes'
        cnf['width'] = 82

        body.integrantes =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.integrantes.cnf = cnf

        cnf['text'] = body.master.dados['data_cadastro'].replace(' ', ' as ')
        cnf['width'] = 20

        body.label_data_cadastro =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.label_data_cadastro.cnf = cnf

        body.pack_forget()

        return body

    def criar_lista(self, lista):
        cnf, pack = {}, {}

        cnf['bg'] = 'green'
        cnf['fg'] = 'white'
        cnf['height'] = 1
        cnf['width'] = 110

        for integrante in lista.master.dados['integrantes']:
            cnf['text'] = integrante

            TKUtils.obter_label(master=lista, cnf=cnf, pack=pack)

        lista.pack_forget()

        return lista
