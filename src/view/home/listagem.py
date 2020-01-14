from src.utils import Utils

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
        self.elemento = self.criar_elemento(dados, integrantes=evento)
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

        base = (
            '{} marcad{} para ' + self.elemento.dados['data'] +
            ' com {} prevista {} ' + str(self.elemento.dados['duracao']) +
            ' {}')
        if self.elemento.defs.tipo == 'evento':
            texto = base.format('Evento', 'o', 'finalização', 'para', '')
        elif self.elemento.defs.tipo == 'tarefa':
            texto = base.format('Tarefa', 'a', 'duração', 'de', 'minutos')
        else:
            texto = base.format('Apresentação', 'a', 'duração', 'de', 'minutos')

        secundario.subelemento.apresentacao.defs.cnf['text'] = texto
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

    def inicializar_integrantes(self, elemento):
        if not elemento.subelemento.integrantes.ativo:
            elemento.subelemento.integrantes.iniciar(master=elemento)

        for integrante in elemento.subelemento.integrantes.lista:
            integrante.destroy()

        elemento.subelemento.integrantes.lista = []

        fim = elemento.dados['duracao']
        inicio = elemento.dados['data']
        for _elemento in self.elementos:
            data = _elemento.dados['data']
            if (_elemento.defs.tipo != 'apresentacao' or
                Utils.comparar_(data1=fim, data2=data) in [-1] or
                Utils.comparar_(data1=inicio, data2=data) in [1]):
                continue

            integrante = self.criar_label()

            integrante.defs.cnf['text'] = _elemento.dados['titulo']
            integrante.defs.cnf['width'] = 102
            integrante.defs.cnf['height'] = 1
            integrante.defs.cnf['bg'] = 'orange'

            integrante.defs.pack['side'] = 'top'

            integrante.iniciar(master=elemento.subelemento.integrantes)
            elemento.subelemento.integrantes.lista.append(integrante)
