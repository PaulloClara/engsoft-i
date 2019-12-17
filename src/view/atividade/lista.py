from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAtividades(Listagem):

    def __init__(self, master, eventos):
        super().__init__(master=master)

        self.eventos = eventos

    def adicionar(self, atividade):
        elemento =\
            self.criar_container(master=self.viewport, elemento=atividade)

        cnf, pack = {}, {}
        cnf['text'] = atividade['titulo']
        cnf['bg'] = 'blue'
        cnf['width'] = 92

        id_elemento = atividade['id_atividade']

        elemento.label = self.criar_label(master=elemento, cnf=cnf, pack=pack)
        elemento.botao_sortear = self.criar_botao_sortear(master=elemento)
        elemento.botao_remover =\
            self.criar_botao_remover(master=elemento, id_elemento=id_elemento)

        self.elementos.append(elemento)

        self.mudar_estado(id_elemento, 'id_atividade', atividade['em_uso'])
