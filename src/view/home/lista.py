from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeElementos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, apresentacao):
        id_elemento = apresentacao['id_apresentacao']

        elemento =\
            self.criar_container(master=self.viewport, elemento=apresentacao)

        cnf, pack = {}, {}
        cnf['text'] = apresentacao['titulo']
        cnf['bg'] = 'orange'
        cnf['width'] = 97

        elemento.label = self.criar_label(master=elemento, cnf=cnf, pack=pack)
        elemento.botao_remover =\
            self.criar_botao_remover(master=elemento, id_elemento=id_elemento)

        self.elementos.append(elemento)
