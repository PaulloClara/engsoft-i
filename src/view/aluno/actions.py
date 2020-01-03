from src.utils.tk import TKUtils


class Actions(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['bd'] = 10
        self.defs.pack['expand'] = True
        self.defs.pack['side'] = 'bottom'

        self.subelemento.sortear = TKUtils.obter_botao()
        self.subelemento.arquivo = TKUtils.obter_botao()

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_sorteio()
        self.inicializar_botao_carregar_arquivo()

    def inicializar_botao_sorteio(self):
        self.subelemento.sortear.defs.cnf['text'] = 'Sortear Aluno'
        self.subelemento.sortear.defs.cnf['bg'] = 'blue'
        self.subelemento.sortear.defs.cnf['width'] = 20

        self.subelemento.sortear.defs.pack['side'] = 'left'

        self.subelemento.sortear.iniciar(master=self)

    def inicializar_botao_carregar_arquivo(self):
        self.subelemento.arquivo.defs.cnf['text'] = 'Procurar CSV'
        self.subelemento.arquivo.defs.cnf['bg'] = 'green'
        self.subelemento.arquivo.defs.cnf['width'] = 20

        self.subelemento.arquivo.defs.pack['side'] = 'right'

        self.subelemento.arquivo.iniciar(master=self)
