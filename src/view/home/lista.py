from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeElementos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.elementos = []

    def adicionar(self, elemento):
        container = self.criar_container(master=self.viewport)

        cnf, pack = {}, {}
        cnf['text'] = elemento['titulo']
        cnf['bg'] = 'orange'
        cnf['width'] = 97

        container.label =\
            self.criar_label(master=container, cnf=cnf, pack=pack)

        id_do_elemento = elemento['id_da_apresentacao']

        container.botao_remover =\
            self.criar_botao_remover(master=container, id_do_elemento=id_do_elemento)

        self.elementos.append(container)
