from src.utils.tk import TKUtils


class Navbar(TKUtils.Container()):

    def __init__(self, master, eventos):
        super().__init__(master=master)
        self.pack()

        self.eventos = eventos

        self.botao_grupo = None
        self.botao_aluno = None
        self.botao_atividade = None

        self.criar_botao_aluno()
        self.criar_botao_atividade()
        self.criar_botao_grupo()

    def criar_botao_aluno(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Alunos'
        cnf['bg'] = 'red'
        cnf['width'] = 14
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.eventos['aluno']

        pack['side'] = 'left'

        self.botao_aluno =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_atividade(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Atividades'
        cnf['bg'] = 'blue'
        cnf['width'] = 24
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.eventos['atividade']

        pack['side'] = 'left'

        self.botao_atividade =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_grupo(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Grupos'
        cnf['bg'] = 'green'
        cnf['width'] = 14
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.eventos['grupo']

        pack['side'] = 'left'

        self.botao_grupo = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
