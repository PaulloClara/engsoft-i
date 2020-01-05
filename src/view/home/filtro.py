from src.utils.tk import TKUtils


class Filtro(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['pady'] = 6
        self.defs.pack['side'] = 'top'

        self.elemento_ativo = ''
        self.subelemento.tarefa = TKUtils.obter_botao()
        self.subelemento.apresentacao = TKUtils.obter_botao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_tarefa()
        self.inicializar_botao_apresentacao()

    def desativar_(self, elemento: str):
        getattr(self.subelemento, elemento).desativar()

        if self.elemento_ativo:
            getattr(self.subelemento, self.elemento_ativo).ativar()

        self.elemento_ativo = elemento

    def inicializar_botao_tarefa(self):
        self.subelemento.tarefa.defs.cnf['text'] = 'Tarefa'
        self.subelemento.tarefa.defs.cnf['bg'] = 'blue'
        self.subelemento.tarefa.defs.cnf['width'] = 8
        self.subelemento.tarefa.defs.cnf['pady'] = 2

        self.subelemento.tarefa.defs.pack['side'] = 'left'

        self.subelemento.tarefa.iniciar(master=self)

    def inicializar_botao_apresentacao(self):
        self.subelemento.apresentacao.defs.cnf['text'] = 'Apresentação'
        self.subelemento.apresentacao.defs.cnf['bg'] = 'green'
        self.subelemento.apresentacao.defs.cnf['width'] = 14
        self.subelemento.apresentacao.defs.cnf['pady'] = 2

        self.subelemento.tarefa.defs.pack['side'] = 'right'

        self.subelemento.apresentacao.iniciar(master=self)
