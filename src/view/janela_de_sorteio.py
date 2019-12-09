from src.utils.tk import TKUtils


class JanelaDeSorteio(TKUtils.Janela()):

    def __init__(self, elemento, atividade):
        super().__init__()

        self.elemento = elemento
        self.atividade = atividade

        self.container = None
        self.label_do_elemento = None
        self.label_da_atividade = None

    def iniciar(self):
        self.title('Grande Felizardo(a)')
        self.geometry(f'{len(self.elemento) * 18 + 100}x100')
        self.resizable(0, 0)

        self.container = self.criar_container()

        texto = f'Aluno: {self.elemento}'
        self.label_do_elemento = self.criar_label(texto=texto, cor='red')

        texto = f'Atividade: {self.atividade["titulo"]}'
        self.label_do_elemento = self.criar_label(texto=texto, cor='green')

    def criar_container(self):
        return TKUtils.obter_container(master=self)

    def criar_label(self, texto, cor):
        cnf, pack = {}, {}

        cnf['text'] = texto
        cnf['bd'] = 4
        cnf['fg'] = cor
        cnf['font'] = ('times new roman', 22, 'bold')

        return TKUtils.obter_label(master=self.container, cnf=cnf, pack=pack)
