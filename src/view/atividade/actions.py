from src.utils.tk import TKUtils


class Actions(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master, bd=10)

        self.eventos = eventos

        self.botao_de_sorteio = None
        self.botao_de_cadastro = None

    def iniciar(self):
        self.criar_botao_de_sorteio()
        self.criar_botao_de_cadastro()

        self.pack(expand=True)

    def criar_botao_de_sorteio(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sortear Atividade'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = lambda evt=None: self.eventos['sortear']({})

        pack['side'] = 'left'

        self.botao_de_sorteio =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_de_cadastro(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Cadastrar Atividade'
        cnf['bg'] = 'green'
        cnf['width'] = 20
        cnf['command'] = self.eventos['cadastrar']

        pack['side'] = 'right'

        self.botao_de_cadastro = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
