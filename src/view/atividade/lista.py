from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAtividades(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, atividade):
        id_elemento = atividade['id_atividade']

        elemento = self.criar_elemento(dados=atividade)

        header = TKUtils.obter_container(master=elemento)
        body = TKUtils.obter_container(master=elemento)

        elemento.header = self.criar_header(header)
        elemento.body = self.criar_body(body)

        self.elementos.append(elemento)

        self.mudar_estado(id_elemento, 'id_atividade', atividade['em_uso'])

    def expandir(self, elemento):
        header = elemento.header
        body = elemento.body

        if elemento.selecionado:
            header.label.configure(width=header.label.cnf['width'], height=2)

            header.botao_sortear.pack_configure(side='left')
            header.botao_remover.pack_configure(side='left')

            body.pack_forget()

            elemento.selecionado = False
        else:
            header.label.configure(width=110, height=3)

            header.botao_remover.pack_forget()
            header.botao_sortear.pack_forget()

            body.pack_configure()

            elemento.selecionado = True

    def criar_header(self, header):
        id_elemento = header.master.dados['id_atividade']

        cnf, pack = {}, {}

        cnf['text'] = header.master.dados['titulo']
        cnf['bg'] = 'blue'
        cnf['width'] = 92
        pack['side'] = 'left'

        header.label = self.criar_label(master=header, cnf=cnf, pack=pack)
        header.botao_sortear = self.criar_botao_sortear(master=header)
        header.botao_remover =\
            self.criar_botao_remover(master=header, id_elemento=id_elemento)

        return header

    def criar_body(self, body):
        cnf, pack = {}, {}

        cnf['bg'] = 'blue'
        cnf['fg'] = 'white'
        cnf['height'] = 2
        pack['side'] = 'left'

        cnf['text'] = body.master.dados['descricao']
        cnf['width'] = 82

        body.label_descricao =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.label_descricao.cnf = cnf

        cnf['text'] = body.master.dados['data_cadastro'].replace(' ', ' as ')
        cnf['width'] = 20

        body.label_data_cadastro =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.label_data_cadastro.cnf = cnf

        body.pack_forget()

        return body
