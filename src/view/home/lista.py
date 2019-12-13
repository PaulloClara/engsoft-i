from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeElementos(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.elementos = []

    def adicionar(self, elemento):
        cont = self.criar_container(master=self.viewport)

        cnf, pack = {}, {}
        cnf['text'] = elemento['titulo']
        cnf['bg'] = 'orange'
        cnf['width'] = 97

        cont.label =\
            self.criar_label(master=cont, cnf=cnf, pack=pack)

        id_do_elemento = elemento['id_apresentacao']

        cont.botao_remover =\
            self.criar_botao_remover(master=cont, id_do_elemento=id_do_elemento)

        self.elementos.append(cont)
