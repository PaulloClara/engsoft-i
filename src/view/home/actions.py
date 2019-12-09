from src.utils.tk import TKUtils


class Actions(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master, bd=10)

        self.eventos = eventos

        self.botao_ordenar = None
        self.botao_cadastrar = None

    def iniciar(self):
        self.criar_botao_ordenar()
        self.criar_botao_cadastrar()

        self.pack(expand=True)

    def criar_botao_ordenar(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Ordenar'
        cnf['bg'] = 'blue'
        cnf['width'] = 20
        cnf['command'] = self.eventos['ordenar']

        pack['side'] = 'left'

        self.botao_ordenar =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_cadastrar(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Cadastrar'
        cnf['bg'] = 'green'
        cnf['width'] = 20
        cnf['command'] = self.eventos['cadastrar']

        pack['side'] = 'left'

        self.botao_cadastrar =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
