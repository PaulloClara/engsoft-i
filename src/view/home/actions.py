from src.utils.tk import TKUtils


class Actions(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['bd'] = 10
        self.defs.pack['expand'] = True
        self.defs.pack['side'] = 'bottom'

        self.subelemento.evento = TKUtils.obter_botao()
        self.subelemento.tarefa = TKUtils.obter_botao()
        self.subelemento.apresentacao = TKUtils.obter_botao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_cadastro_evento()
        self.inicializar_botao_cadastro_tarefa()
        self.inicializar_botao_cadastro_apresentacao()

    def inicializar_botao_cadastro_apresentacao(self):
        self.subelemento.apresentacao.defs.cnf['text'] =\
            'Cadastrar Apresentação'
        self.subelemento.apresentacao.defs.cnf['bg'] = 'green'
        self.subelemento.apresentacao.defs.cnf['width'] = 26

        self.subelemento.apresentacao.defs.pack['side'] = 'right'

        self.subelemento.apresentacao.iniciar(master=self)

    def inicializar_botao_cadastro_tarefa(self):
        self.subelemento.tarefa.defs.cnf['text'] = 'Cadastrar Tarefa'
        self.subelemento.tarefa.defs.cnf['bg'] = 'blue'
        self.subelemento.tarefa.defs.cnf['width'] = 20

        self.subelemento.tarefa.defs.pack['side'] = 'left'

        self.subelemento.tarefa.iniciar(master=self)

    def inicializar_botao_cadastro_evento(self):
        self.subelemento.evento.defs.cnf['text'] = 'Cadastrar Evento'
        self.subelemento.evento.defs.cnf['bg'] = 'orange'
        self.subelemento.evento.defs.cnf['width'] = 20

        self.subelemento.evento.defs.pack['side'] = 'right'

        self.subelemento.evento.iniciar(master=self)
