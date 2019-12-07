from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAlunos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.alunos = []

    def adicionar(self, nome_do_aluno):
        container = self.criar_container(master=self.viewport)

        cnf, pack = {}, {}
        cnf['text'] = nome_do_aluno
        cnf['bg'] = 'red'
        cnf['width'] = 98

        container.label =\
            self.criar_label(master=container, cnf=cnf, pack=pack)

        cnf, pack, defs = {}, {}, {}
        defs['tipo'] = 'aluno'
        defs['valor'] = nome_do_aluno

        container.botao_sortear =\
            self.criar_botao_sortear(master=container, cnf=cnf, pack=pack, defs=defs)

        self.alunos.append(container)
