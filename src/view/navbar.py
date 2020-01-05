from src.utils.tk import TKUtils


class Navbar(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['side'] = 'top'

        self.subelemento.home = TKUtils.obter_botao()
        self.subelemento.aluno = TKUtils.obter_botao()
        self.subelemento.grupo = TKUtils.obter_botao()
        self.subelemento.sobre = TKUtils.obter_botao()
        self.subelemento.atividade = TKUtils.obter_botao()

        self.elemento_ativo = ''

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_botao_aluno()
        self.inicializar_botao_grupo()
        self.inicializar_botao_home()
        self.inicializar_botao_atividade()
        self.inicializar_botao_sobre()

    def desativar_(self, elemento: str):
        if self.elemento_ativo:
            getattr(self.subelemento, self.elemento_ativo).ativar()

        getattr(self.subelemento, elemento).desativar()

        self.elemento_ativo = elemento

    def inicializar_botao_home(self):
        self.subelemento.home.defs.cnf['text'] = 'Home'
        self.subelemento.home.defs.cnf['bg'] = 'orange'
        self.subelemento.home.defs.cnf['width'] = 28
        self.subelemento.home.defs.cnf['pady'] = 9
        self.subelemento.home.defs.cnf['bd'] = 1
        self.subelemento.home.defs.mcnf['fz'] = 15

        self.subelemento.home.defs.pack['side'] = 'left'

        self.subelemento.home.iniciar(master=self)

    def inicializar_botao_aluno(self):
        self.subelemento.aluno.defs.cnf['text'] = 'Alunos'
        self.subelemento.aluno.defs.cnf['bg'] = 'red'
        self.subelemento.aluno.defs.cnf['width'] = 14
        self.subelemento.aluno.defs.cnf['pady'] = 9
        self.subelemento.aluno.defs.cnf['bd'] = 1
        self.subelemento.aluno.defs.mcnf['fz'] = 15

        self.subelemento.aluno.defs.pack['side'] = 'left'

        self.subelemento.aluno.iniciar(master=self)

    def inicializar_botao_atividade(self):
        self.subelemento.atividade.defs.cnf['text'] = 'Atividades'
        self.subelemento.atividade.defs.cnf['bg'] = 'blue'
        self.subelemento.atividade.defs.cnf['width'] = 14
        self.subelemento.atividade.defs.cnf['pady'] = 9
        self.subelemento.atividade.defs.cnf['bd'] = 1
        self.subelemento.atividade.defs.mcnf['fz'] = 15

        self.subelemento.atividade.defs.pack['side'] = 'left'

        self.subelemento.atividade.iniciar(master=self)

    def inicializar_botao_grupo(self):
        self.subelemento.grupo.defs.cnf['text'] = 'Grupos'
        self.subelemento.grupo.defs.cnf['bg'] = 'green'
        self.subelemento.grupo.defs.cnf['width'] = 14
        self.subelemento.grupo.defs.cnf['pady'] = 9
        self.subelemento.grupo.defs.cnf['bd'] = 1
        self.subelemento.grupo.defs.mcnf['fz'] = 15

        self.subelemento.grupo.defs.pack['side'] = 'left'

        self.subelemento.grupo.iniciar(master=self)

    def inicializar_botao_sobre(self):
        self.subelemento.sobre.defs.cnf['text'] = 'Sobre'
        self.subelemento.sobre.defs.cnf['bg'] = '#FFD700'
        self.subelemento.sobre.defs.cnf['width'] = 14
        self.subelemento.sobre.defs.cnf['pady'] = 9
        self.subelemento.sobre.defs.cnf['bd'] = 1
        self.subelemento.sobre.defs.mcnf['fz'] = 15

        self.subelemento.sobre.defs.pack['side'] = 'left'

        self.subelemento.sobre.iniciar(master=self)
