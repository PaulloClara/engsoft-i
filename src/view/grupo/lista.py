from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeGrupos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, grupo):
        id_elemento = grupo['id_grupo']

        elemento = self.criar_container(master=self.viewport, elemento=grupo)

        cnf, pack = {}, {}
        cnf['text'] = grupo['nome']
        cnf['bg'] = 'green'
        cnf['width'] = 92

        elemento.label = self.criar_label(master=elemento, cnf=cnf, pack=pack)
        elemento.botao_sortear = self.criar_botao_sortear(master=elemento)
        elemento.botao_remover =\
            self.criar_botao_remover(master=elemento, id_elemento=id_elemento)

        self.elementos.append(elemento)
        self.mudar_estado(id_elemento, 'id_grupo', grupo['em_uso'])
