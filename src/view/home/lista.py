from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeElementos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, apresentacao):
        elemento = self.criar_elemento(dados=apresentacao)

        header = TKUtils.obter_container(master=elemento)
        body = TKUtils.obter_container(master=elemento)

        elemento.header = self.criar_header(header)
        elemento.body = self.criar_body(body)

        self.elementos.append(elemento)

    def expandir(self, elemento):
        header = elemento.header
        body = elemento.body

        if elemento.selecionado:
            header.label.configure(width=header.label.cnf['width'], height=2)

            header.botao_remover.pack_configure(side='left')

            body.pack_forget()

            elemento.selecionado = False
        else:
            header.label.configure(width=110, height=3)

            header.botao_remover.pack_forget()

            body.pack_configure()

            elemento.selecionado = True

    def criar_header(self, header):
        id_elemento = header.master.dados['id_apresentacao']

        cnf, pack = {}, {}

        cnf['text'] = header.master.dados['titulo']
        cnf['bg'] = 'orange'
        cnf['width'] = 97
        pack['side'] = 'left'

        header.label = self.criar_label(master=header, cnf=cnf, pack=pack)
        header.botao_remover =\
            self.criar_botao_remover(master=header, id_elemento=id_elemento)

        return header

    def criar_body(self, body):
        cnf, pack = {}, {}

        cnf['bg'] = 'orange'
        cnf['fg'] = 'white'
        cnf['height'] = 2
        pack['side'] = 'left'

        data_apresentacao = body.master.dados['data_apresentacao']
        duracao = body.master.dados['duracao']
        cnf['text'] = f'Apresentação marcada para {data_apresentacao}'
        cnf['text'] += f' com duração prevista de {duracao} minutos'
        cnf['width'] = 82

        body.label_data_apresentacao =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.label_data_apresentacao.cnf = cnf

        cnf['text'] = body.master.dados['data_cadastro'].replace(' ', ' as ')
        cnf['width'] = 20

        body.label_data_cadastro =\
            TKUtils.obter_label(master=body, cnf=cnf, pack=pack)
        body.label_data_cadastro.cnf = cnf

        body.pack_forget()

        return body
