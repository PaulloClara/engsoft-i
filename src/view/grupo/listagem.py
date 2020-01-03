from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeGrupos(Listagem):

    def __init__(self):
        super().__init__()

        self.elemento = None
        self.elementos = []

    def iniciar(self, master):
        super().iniciar(master=master)

    def adicionar(self, grupo):
        self.elemento = self.criar_elemento(dados=grupo)

        self.inicializar_primario()
        self.inicializar_secundario()

        if self.elemento.dados['em_uso']:
            self.desativar(elemento=self.elemento)

        self.elementos.append(self.elemento)
        self.elemento = None

        return self.elementos[-1]

    def ativar(self, id_grupo='', elemento=None):
        if not elemento:
            elemento = super().obter(_id=id_grupo)['elemento']

        elemento.subelemento.primario.subelemento.remover.ativar()
        elemento.subelemento.primario.subelemento.sortear.ativar()

    def desativar(self, id_grupo='', elemento=None):
        if not elemento:
            elemento = super().obter(_id=id_grupo)['elemento']

        elemento.subelemento.primario.subelemento.remover.desativar()
        elemento.subelemento.primario.subelemento.sortear.desativar()

    def inicializar_primario(self):
        primario = self.elemento.subelemento.primario

        primario.subelemento.label = self.criar_label()
        primario.subelemento.sortear = self.criar_botao_sortear()
        primario.subelemento.remover = self.criar_botao_remover()

        primario.subelemento.label.defs.cnf['text'] =\
            self.elemento.dados['nome']
        primario.subelemento.label.defs.cnf['width'] = 92
        primario.subelemento.label.defs.cnf['bg'] = 'green'

        primario.iniciar(master=self.elemento)
        primario.subelemento.label.iniciar(master=primario)
        primario.subelemento.sortear.iniciar(master=primario)
        primario.subelemento.remover.iniciar(master=primario)

    def inicializar_secundario(self):
        secundario = self.elemento.subelemento.secundario

        secundario.subelemento.total = self.criar_label()
        secundario.subelemento.cadastro = self.criar_label()

        secundario.subelemento.total.defs.cnf['text'] =\
            f'Total de {len(self.elemento.dados["integrantes"])} integrantes'
        secundario.subelemento.total.defs.cnf['width'] = 80
        secundario.subelemento.total.defs.cnf['bg'] = 'green'

        secundario.subelemento.total.defs.pack['side'] = 'left'

        secundario.subelemento.cadastro.defs.cnf['text'] =\
            self.elemento.dados['cadastro'].replace(' ', ' as ')
        secundario.subelemento.cadastro.defs.cnf['width'] = 21
        secundario.subelemento.cadastro.defs.cnf['bg'] = 'green'

        secundario.iniciar(master=self.elemento)
        secundario.subelemento.total.iniciar(master=secundario)
        secundario.subelemento.cadastro.iniciar(master=secundario)

        secundario.ocultar()

    def inicializar_integrantes(self, elemento):
        elemento.subelemento.integrantes.iniciar(master=elemento)

        for nome in elemento.dados['integrantes']:
            integrante = self.criar_label()

            integrante.defs.cnf['text'] = nome
            integrante.defs.cnf['width'] = 102
            integrante.defs.cnf['height'] = 1
            integrante.defs.cnf['bg'] = 'green'

            integrante.defs.pack['side'] = 'top'

            integrante.iniciar(master=elemento.subelemento.integrantes)
            elemento.subelemento.integrantes.lista.append(integrante)
