from src.utils.tk import TKUtils


class Actions(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['bd'] = 10
        self.defs.pack['expand'] = True
        self.defs.pack['side'] = 'bottom'

        self.subelemento.tarefa = TKUtils.obter_botao()
        self.subelemento.cadastrar = TKUtils.obter_botao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_cadastro()
        self.inicializar_botao_cadastro_tarefa()

    def inicializar_botao_cadastro(self):
        self.subelemento.cadastrar.defs.cnf['text'] = 'Cadastrar Apresentação'
        self.subelemento.cadastrar.defs.cnf['bg'] = 'green'
        self.subelemento.cadastrar.defs.cnf['width'] = 30

        self.subelemento.cadastrar.defs.pack['side'] = 'right'

        self.subelemento.cadastrar.iniciar(master=self)

    def inicializar_botao_cadastro_tarefa(self):
        self.subelemento.tarefa.defs.cnf['text'] = 'Cadastrar Tarefa'
        self.subelemento.tarefa.defs.cnf['bg'] = 'blue'
        self.subelemento.tarefa.defs.cnf['width'] = 30

        self.subelemento.tarefa.defs.pack['side'] = 'left'

        self.subelemento.tarefa.iniciar(master=self)
