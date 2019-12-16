from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAlunos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.alunos = []

    def adicionar(self, nome_do_aluno):
        cont =\
            self.criar_container(master=self.viewport, elemento=nome_do_aluno)

        cnf, pack = {}, {}
        cnf['text'] = nome_do_aluno
        cnf['bg'] = 'red'
        cnf['width'] = 97

        cont.label = self.criar_label(master=cont, cnf=cnf, pack=pack)

        cont.botao_sortear = self.criar_botao_sortear(master=cont)

        self.alunos.append(cont)
