from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAlunos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, nome_do_aluno):
        elemento = self.criar_elemento(dados=nome_do_aluno)

        cnf, pack = {}, {}
        cnf['text'] = nome_do_aluno
        cnf['bg'] = 'red'
        cnf['width'] = 97

        elemento.label = self.criar_label(master=elemento, cnf=cnf, pack=pack)
        elemento.botao_sortear = self.criar_botao_sortear(master=elemento)

        self.elementos.append(elemento)
