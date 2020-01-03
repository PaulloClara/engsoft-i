from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeAtividades(Listagem):

    def __init__(self):
        super().__init__()

        self.elemento = None
        self.elementos = []

    def iniciar(self, master):
        super().iniciar(master=master)

    def adicionar(self, atividade):
        self.elemento = self.criar_elemento(dados=atividade)

        self.inicializar_primario()
        self.inicializar_secundario()

        self.elemento.subelemento.secundario.ocultar()

        if self.elemento.dados['em_uso']:
            self.desativar(elemento=self.elemento)

        self.elementos.append(self.elemento)
        self.elemento = None

        return self.elementos[-1]

    def ativar(self, id_atividade='', elemento=None):
        if not elemento:
            elemento = super().obter(_id=id_atividade)['elemento']

        elemento.subelemento.primario.subelemento.remover.ativar()
        elemento.subelemento.primario.subelemento.sortear.ativar()

    def desativar(self, id_atividade='', elemento=None):
        if not elemento:
            elemento = super().obter(_id=id_atividade)['elemento']

        elemento.subelemento.primario.subelemento.remover.desativar()
        elemento.subelemento.primario.subelemento.sortear.desativar()

    def inicializar_primario(self):
        primario = self.elemento.subelemento.primario

        primario.subelemento.label = self.criar_label()
        primario.subelemento.sortear = self.criar_botao_sortear()
        primario.subelemento.remover = self.criar_botao_remover()

        primario.subelemento.label.defs.cnf['text'] =\
            self.elemento.dados['titulo']
        primario.subelemento.label.defs.cnf['bg'] = 'blue'
        primario.subelemento.label.defs.cnf['width'] = 92

        primario.subelemento.label.defs.pack['side'] = 'left'

        primario.iniciar(master=self.elemento)
        primario.subelemento.label.iniciar(master=primario)
        primario.subelemento.sortear.iniciar(master=primario)
        primario.subelemento.remover.iniciar(master=primario)

    def inicializar_secundario(self):
        secundario = self.elemento.subelemento.secundario

        secundario.subelemento.cadastro = self.criar_label()
        secundario.subelemento.descricao = self.criar_label()

        secundario.subelemento.descricao.defs.cnf['text'] =\
            self.elemento.dados['descricao']
        secundario.subelemento.descricao.defs.cnf['width'] = 80
        secundario.subelemento.descricao.defs.cnf['bg'] = 'blue'

        secundario.subelemento.descricao.defs.pack['side'] = 'left'

        secundario.subelemento.cadastro.defs.cnf['text'] =\
            self.elemento.dados['data_cadastro'].replace(' ', ' as ')
        secundario.subelemento.cadastro.defs.cnf['width'] = 21
        secundario.subelemento.cadastro.defs.cnf['bg'] = 'blue'

        secundario.iniciar(master=self.elemento)
        secundario.subelemento.descricao.iniciar(master=secundario)
        secundario.subelemento.cadastro.iniciar(master=secundario)
