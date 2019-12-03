from src.utils.tk import TKUtils


class JanelaDeErro(TKUtils.Janela()):

    def __init__(self, erro):
        super().__init__()

        self.title('Janela de Erro')
        self.geometry(f'{len(erro) * 16}x140')
        self.resizable(0, 0)

        self.msg_de_erro = erro

        self.container = None
        self.label_de_erro = None
        self.botao_confirmar = None

        self.criar_container()

    def criar_container(self):
        cnf = {}
        cnf['bd'] = 10

        self.container = TKUtils.obter_container(master=self, cnf=cnf)

        self.criar_label_de_erro()
        self.criar_botao_confirmar()

    def criar_label_de_erro(self):
        cnf, pack = {}, {}

        cnf['text'] = self.msg_de_erro
        cnf['fg'] = 'red'
        cnf['font'] = ('arial', 16, 'bold')

        pack['pady'] = 10

        self.label_de_erro = TKUtils.obter_label(master=self, cnf=cnf, pack=pack)

    def criar_botao_confirmar(self):
        cnf, pack = {}, {}

        cnf['text'] = 'OK'
        cnf['bg'] = 'green'
        cnf['command'] = self.destroy

        pack['pady'] = 25
        pack['side'] = 'bottom'

        self.botao_confirmar = TKUtils.obter_botao(master=self, cnf=cnf, pack=pack)
