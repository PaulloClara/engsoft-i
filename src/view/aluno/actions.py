from src.utils.tk import TKUtils


class Actions(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master, cnf={'bd': 10})
        self.pack(expand=True)

        self.eventos = eventos

        self.botao_de_sorteio = None
        self.botao_de_carregar_arquivo = None

        self.criar_botao_de_sorteio()
        self.criar_botao_de_carregar_arquivo()

    def criar_botao_de_sorteio(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sortear Aluno'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = self.eventos['sortear']

        pack['side'] = 'left'

        self.botao_de_sorteio =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_de_carregar_arquivo(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Procurar CSV'
        cnf['bg'] = 'green'
        cnf['width'] = 20
        cnf['command'] = self.eventos['arquivo']

        pack['side'] = 'right'

        self.botao_de_carregar_arquivo =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
