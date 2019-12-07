from src.utils.tk import TKUtils


class Listagem(TKUtils.ScrollContainer()):

    def __init__(self, master):
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

    def criar_container(self, master):
        cnf = {}

        cnf['bd'] = 1
        cnf['bg'] = 'grey'

        container = TKUtils.obter_container(master=master, cnf=cnf)

        return container

    def criar_label(self, master, cnf={}, pack={}):
        cnf['fg'] = 'white'
        cnf['height'] = 2

        pack['side'] = 'left'

        label = TKUtils.obter_label(master=master, cnf=cnf, pack=pack)

        return label

    def criar_botao_sortear(self, master, defs, cnf={}, pack={}):
        cnf['text'] = 'O'
        cnf['bg'] = 'orange'
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.eventos['sortear'](defs=defs)

        pack['side'] = 'left'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)

        return botao

    def criar_botao_remover(self, master, id_do_elemento, cnf={}, pack={}):
        cnf['text'] = 'X'
        cnf['bg'] = 'red'
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.eventos['remover'](id_do_elemento)

        pack['side'] = 'right'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)

        return botao
