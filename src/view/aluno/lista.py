from src.utils.tk import TKUtils


class ListaDeAlunos(TKUtils.ScrollContainer()):

    def __init__(self, master, eventos):
        cnf, canvas_cnf, viewport_cnf, scrollbar_cnf = {}, {}, {}, {}

        cnf['bd'] = 2
        cnf['bg'] = 'grey'
        cnf['relief'] = 'flat'

        canvas_cnf['width'] = 920
        canvas_cnf['height'] = 360

        scrollbar_cnf['bd'] = 4
        scrollbar_cnf['bg'] = 'grey'
        scrollbar_cnf['relief'] = 'flat'

        super().__init__(master=master, cnf=cnf, cs_cnf=canvas_cnf,
                         vt_cnf=viewport_cnf, sr_cnf=scrollbar_cnf)
        self.pack(expand=True)

        self.eventos = eventos

        self.lista_de_alunos = []

    def adicionar(self, nome_do_aluno):
        # Container
        cnf, pack = {}, {}

        cnf['bd'] = 1
        cnf['bg'] = 'grey'

        container =\
            TKUtils.obter_container(master=self.viewport, cnf=cnf, pack=pack)

        # Label
        cnf, pack = {}, {}

        cnf['text'] = nome_do_aluno
        cnf['bg'] = 'red'
        cnf['fg'] = 'white'
        cnf['width'] = 98
        cnf['height'] = 2

        pack['side'] = 'left'

        container.label =\
            TKUtils.obter_label(master=container, cnf=cnf, pack=pack)

        # Raffle Button
        cnf, pack, defs = {}, {}, {}

        defs['tipo'] = 'aluno'
        defs['valor'] = nome_do_aluno

        cnf['text'] = 'O'
        cnf['bg'] = 'orange'
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.eventos['sortear'](defs=defs)

        pack['side'] = 'right'

        container.botao =\
            TKUtils.obter_botao(master=container, cnf=cnf, pack=pack)

        self.lista_de_alunos.append(container)
