from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAtividades(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos
        self.atividades = []

    def adicionar(self, atividade):
        cont = self.criar_container(master=self.viewport, elemento=atividade)

        cnf, pack = {}, {}
        cnf['text'] = atividade['titulo']
        cnf['bg'] = 'blue'
        cnf['width'] = 93

        cont.label = self.criar_label(master=cont, cnf=cnf, pack=pack)

        cont.botao_sortear = self.criar_botao_sortear(master=cont)

        id_do_elemento = atividade['id_atividade']

        cont.botao_remover =\
            self.criar_botao_remover(master=cont, id_do_elemento=id_do_elemento)

        self.atividades.append(cont)
