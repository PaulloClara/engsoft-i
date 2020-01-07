from src.utils.tk import TKUtils
from src.view.listagem import Listagem


class ListaDeElementos(Listagem):

    def __init__(self):
        super().__init__()

        self.defs.canvas['height'] = 348

        self.elemento = None
        self.elementos = []
        self.elemento_ativo = ''

    def iniciar(self, master):
        super().iniciar(master=master)

    def adicionar(self, apresentacao=None, tarefa=None, evento=None):
        dados = tarefa if tarefa else evento if evento else apresentacao
        self.elemento = self.criar_elemento(dados)
        self.elemento.defs.tipo =\
            'tarefa' if tarefa else 'evento' if evento else 'apresentacao'

        self.inicializar_primario()
        self.inicializar_secundario()

        if self.elemento_ativo != self.elemento.defs.tipo:
            self.elemento.ocultar()

        self.elementos.append(self.elemento)
        self.elemento = None

        return self.elementos[-1]

    def inicializar_primario(self):
        primario = self.elemento.subelemento.primario

        primario.subelemento.label = self.criar_label()
        primario.subelemento.remover = self.criar_botao_remover()

        primario.subelemento.label.defs.cnf['text'] =\
            self.elemento.dados['titulo']
        primario.subelemento.label.defs.cnf['width'] = 97
        primario.subelemento.label.defs.cnf['bg'] = 'orange'

        primario.iniciar(master=self.elemento)
        primario.subelemento.label.iniciar(master=primario)
        primario.subelemento.remover.iniciar(master=primario)

    def inicializar_secundario(self):
        secundario = self.elemento.subelemento.secundario

        secundario.subelemento.cadastro = self.criar_label()
        secundario.subelemento.apresentacao = self.criar_label()

        if self.elemento.defs.tipo == 'evento':
            tipo = 'Evento marcado'
        elif self.elemento.defs.tipo == 'tarefa':
            tipo = 'Tarefa marcada'
        else:
            tipo = 'Apresentação marcada'

        secundario.subelemento.apresentacao.defs.cnf['text'] = (
            tipo + ' para ' + self.elemento.dados['data'] +
            ' com duração prevista de ' + str(self.elemento.dados['duracao']) +
            ' minutos')
        secundario.subelemento.apresentacao.defs.cnf['width'] = 82
        secundario.subelemento.apresentacao.defs.cnf['bg'] = 'orange'

        secundario.subelemento.apresentacao.defs.pack['side'] = 'left'

        secundario.subelemento.cadastro.defs.cnf['text'] =\
            self.elemento.dados['cadastro'].replace(' ', ' as ')
        secundario.subelemento.cadastro.defs.cnf['width'] = 20
        secundario.subelemento.cadastro.defs.cnf['bg'] = 'orange'

        secundario.subelemento.cadastro.defs.pack['side'] = 'right'

        secundario.iniciar(master=self.elemento)
        secundario.subelemento.cadastro.iniciar(master=secundario)
        secundario.subelemento.apresentacao.iniciar(master=secundario)

        secundario.ocultar()
