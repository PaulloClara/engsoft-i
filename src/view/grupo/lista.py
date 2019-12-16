from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeGrupos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.grupos = []

    def adicionar(self, grupo):
        estado = grupo['em_uso']
        cont = self.criar_container(master=self.viewport, desativado=estado)

        cnf, pack = {}, {}
        cnf['text'] = grupo['nome']
        cnf['bg'] = 'green'
        cnf['width'] = 93

        cont.label = self.criar_label(master=cont, cnf=cnf, pack=pack)

        cont.botao_sortear = self.criar_botao_sortear(master=cont, valor=grupo)

        cnf, pack = {}, {}
        id_do_elemento = grupo['id_grupo']

        cont.botao_remover =\
            self.criar_botao_remover(master=cont, id_do_elemento=id_do_elemento)

        self.grupos.append(cont)
