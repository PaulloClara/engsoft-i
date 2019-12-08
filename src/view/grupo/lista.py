from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeGrupos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.grupos = []

    def adicionar(self, grupo):
        container = self.criar_container(master=self.viewport)

        cnf, pack = {}, {}
        cnf['text'] = grupo['nome']
        cnf['bg'] = 'green'
        cnf['width'] = 93

        container.label =\
            self.criar_label(master=container, cnf=cnf, pack=pack)

        cnf, pack, defs = {}, {}, {}
        defs['tipo'] = 'grupo'
        defs['valor'] = grupo

        container.botao_sortear =\
            self.criar_botao_sortear(master=container, cnf=cnf, pack=pack, defs=defs)

        cnf, pack = {}, {}
        id_do_elemento = grupo['id_do_grupo']

        container.botao_remover =\
            self.criar_botao_remover(master=container, id_do_elemento=id_do_elemento)

        self.grupos.append(container)
