from src.utils.tk import TKUtils


class JanelaDeSorteio(TKUtils.Janela()):

    def __init__(self, aluno, atividade):
        super().__init__()

        self.title('Grande Felizardo(a)')
        self.geometry(f'{len(aluno) * 18 + 100}x100')
        self.resizable(0, 0)

        self.nome_do_aluno = aluno
        self.titulo_da_atividade = atividade

        self.container = None
        self.label_do_aluno = None
        self.label_da_atividade = None
        self.botao_confirmar = None

        self.criar_container()
        self.criar_label_do_aluno()
        self.criar_label_da_atividade()

    def criar_container(self):
        self.container = TKUtils.obter_container(master=self)

    def criar_label_do_aluno(self):
        cnf, pack = {}, {}

        cnf['text'] = f'Aluno: {self.nome_do_aluno}'
        cnf['bd'] = 4
        cnf['fg'] = 'red'
        cnf['font'] = ('arial', 16, 'bold')

        self.label_do_aluno =\
            TKUtils.obter_label(master=self.container, cnf=cnf, pack=pack)

    def criar_label_da_atividade(self):
        cnf, pack = {}, {}

        cnf['text'] = f'Atividade: {self.titulo_da_atividade}'
        cnf['bd'] = 4
        cnf['fg'] = 'blue'
        cnf['font'] = ('arial', 16, 'bold')

        self.label_da_atividade =\
            TKUtils.obter_label(master=self.container, cnf=cnf, pack=pack)
