from src.utils.tk import TKUtils


class Sobre(TKUtils.obter_container()):

    def __init__(self):
        super().__init__()

        self.defs.pack['padx'] = 20

    def iniciar(self, master):
        super().iniciar(master=master)

        self.inicializar_infos()
        self.inicializar_repositorio()
        self.inicializar_devs()

        self.ocultar()

    def inicializar_infos(self):
        infos = TKUtils.obter_mensagem()
        infos.defs.cnf['text'] = (
            'Projeto referente à disciplina de ' +
            'Engenharia de Software I do Instituto Federal do Piauí - IFPI')
        infos.defs.cnf['width'] = 700
        infos.defs.mcnf['fz'] = 18
        infos.defs.pack['padx'] = 20
        infos.defs.pack['pady'] = 20
        infos.iniciar(master=self)

    def inicializar_devs(self):
        def criar_label(master, texto):
            label = TKUtils.obter_label()
            label.defs.cnf['text'] = texto
            label.defs.cnf['width'] = 200
            label.defs.mcnf['fz'] = 18
            label.iniciar(master=master)

        devs = TKUtils.obter_container(instanciar=True)
        devs.defs.pack['pady'] = 6
        devs.iniciar(master=self)

        label = TKUtils.obter_label()
        label.defs.cnf['text'] = 'Desenvolvedores'
        label.defs.mcnf['fz'] = 24
        label.defs.pack['padx'] = 20
        label.defs.pack['side'] = 'left'
        label.iniciar(master=devs)

        membros = TKUtils.obter_container(instanciar=True)
        membros.defs.cnf['bd'] = 4
        membros.defs.cnf['bg'] = 'grey'
        membros.defs.pack['side'] = 'right'
        membros.iniciar(master=devs)

        criar_label(membros, 'Paulo Ricardo: github.com/paulloclara')
        criar_label(membros, 'Josivan Cardoso: github.com/josivancs')
        criar_label(membros, 'Weslley Isidorio: github.com/weslleyisidorio')

    def inicializar_repositorio(self):
        label = TKUtils.obter_label()
        label.defs.cnf['text'] = 'Stuki: github.com/paulloclara/stuki'
        label.defs.mcnf['fz'] = 16
        label.defs.pack['pady'] = 10
        label.defs.pack['side'] = 'bottom'
        label.iniciar(master=self)
