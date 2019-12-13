from src.utils.tk import TKUtils


class Actions(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master, bd=10)

        self.eventos = eventos

        self.botao_de_sorteio = None
        self.botao_de_carregar_arquivo = None

    def iniciar(self):
        self.criar_botao_de_sorteio()
        self.criar_botao_de_carregar_arquivo()

        self.pack(expand=True)

    def criar_botao_de_sorteio(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sortear Aluno'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = lambda evt=None: self.eventos['sortear']({})

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
