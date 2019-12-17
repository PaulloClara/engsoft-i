from src.utils.tk import TKUtils


class Navbar(TKUtils.Container()):

    def __init__(self, master, controller):
        super().__init__(master=master)

        self.controller = controller

        self.botao_home = None
        self.botao_aluno = None
        self.botao_grupo = None
        self.botao_atividade = None
        self.botao_sobre = None

    def iniciar(self):
        self.criar_botao_aluno()
        self.criar_botao_grupo()
        self.criar_botao_home()
        self.criar_botao_atividade()
        self.criar_botao_sobre()

        self.pack(side='top')

    def criar_botao_home(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Home'
        cnf['bg'] = 'orange'
        cnf['width'] = 28
        cnf['pady'] = 9
        cnf['font'] = ('times new roman', 15, 'bold')
        cnf['command'] = self.controller.tela_home

        pack['side'] = 'left'

        self.botao_home = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_aluno(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Alunos'
        cnf['bg'] = 'red'
        cnf['width'] = 14
        cnf['pady'] = 9
        cnf['font'] = ('times new roman', 15, 'bold')
        cnf['command'] = self.controller.tela_aluno

        pack['side'] = 'left'

        self.botao_aluno = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_atividade(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Atividades'
        cnf['bg'] = 'blue'
        cnf['width'] = 14
        cnf['pady'] = 9
        cnf['font'] = ('times new roman', 15, 'bold')
        cnf['command'] = self.controller.tela_atividade

        pack['side'] = 'left'

        self.botao_atividade =\
            TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_grupo(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Grupos'
        cnf['bg'] = 'green'
        cnf['width'] = 14
        cnf['pady'] = 9
        cnf['font'] = ('times new roman', 15, 'bold')
        cnf['command'] = self.controller.tela_grupo

        pack['side'] = 'left'

        self.botao_grupo = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)

    def criar_botao_sobre(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Sobre'
        cnf['bg'] = 'grey'
        cnf['width'] = 14
        cnf['pady'] = 9
        cnf['font'] = ('times new roman', 15, 'bold')
        cnf['command'] = self.controller.tela_sobre

        pack['side'] = 'left'

        self.botao_sobre = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
