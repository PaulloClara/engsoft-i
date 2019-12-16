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

    def iniciar(self):
        self.pack(expand=True)

    def expandir(self, elemento):
        if elemento.selecionado:
            elemento.label.configure(height=2)
            elemento.label.configure(width=elemento.label.cnf['width'])

            elemento.selecionado = False
            elemento.botao_remover.pack_configure()
        else:
            elemento.label.configure(height=6)
            elemento.label.configure(width=110)

            elemento.selecionado = True
            elemento.botao_remover.pack_forget()

    def criar_container(self, master, elemento):
        cnf = {}

        cnf['bd'] = 1
        cnf['bg'] = 'grey'

        container = TKUtils.obter_container(master=master, cnf=cnf)

        try:
            container.desativado = elemento['em_uso']
        except Exception as e:
            container.desativado = False

        container.selecionado = False
        container.dados = elemento

        return container

    def criar_label(self, master, cnf={}, pack={}):
        cnf['fg'] = 'white'
        cnf['bg'] = 'grey' if master.desativado else cnf['bg']
        cnf['height'] = 2

        pack['side'] = 'left'

        label = TKUtils.obter_label(master=master, cnf=cnf, pack=pack)

        comando = self.eventos['expandir']
        label.bind('<Button-1>', lambda evt=None: comando(evt, master))

        label.cnf = cnf

        return label

    def criar_botao_sortear(self, master, cnf={}, pack={}):
        cnf['text'] = 'O'
        cnf['bg'] = 'grey' if master.desativado else 'orange'
        cnf['bd'] = 4
        cnf['width'] = 2
        cnf['state'] = 'disabled' if master.desativado else 'normal'
        cnf['command'] =\
            lambda evt=None: self.eventos['sortear'](valor=master.dados)

        pack['side'] = 'left'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)

        return botao

    def criar_botao_remover(self, master, id_do_elemento, cnf={}, pack={}):
        cnf['text'] = 'X'
        cnf['bg'] = 'grey' if master.desativado else 'red'
        cnf['state'] = 'disabled' if master.desativado else 'normal'
        cnf['bd'] = 4
        cnf['width'] = 2
        cnf['command'] =\
            lambda evt=None: self.eventos['remover'](id_do_elemento)

        pack['side'] = 'right'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)

        return botao
