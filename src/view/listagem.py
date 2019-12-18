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

        self.elementos = []

    def iniciar(self):
        self.pack(expand=True)

    def mudar_estado(self, id_elemento, chave, desativar=True):
        for elemento in self.elementos:
            if elemento.dados[chave] == id_elemento:
                if desativar:
                    self.desativar_elemento(elemento=elemento)
                else:
                    self.ativar_elemento(elemento=elemento)
                return

    def remover_elemento(self, id_elemento, chave):
        for i, elemento in enumerate(self.elementos):
            if elemento.dados[chave] == id_elemento:
                elemento.destroy()
                del self.elementos[i]

    def ativar_elemento(self, elemento):
        header = elemento.header

        header.label.configure(bg=header.label.cnf['bg'])

        if 'botao_remover' in dir(header):
            header.botao_remover.configure(state='normal', bg='red')
        if 'botao_sortear' in dir(header):
            header.botao_sortear.configure(state='normal', bg='orange')

        elemento.desativado = False

    def desativar_elemento(self, elemento):
        header = elemento.header

        header.label.configure(bg='grey')

        if 'botao_remover' in dir(header):
            header.botao_remover.configure(state='disabled', bg='grey')
        if 'botao_sortear' in dir(header):
            header.botao_sortear.configure(state='disabled', bg='grey')

        elemento.desativado = True

    def criar_elemento(self, dados):
        cnf = {}

        cnf['bd'] = 2
        cnf['bg'] = 'grey'
        cnf['relief'] = 'ridge'

        container = TKUtils.obter_container(master=self.viewport, cnf=cnf)

        container.desativado = False
        container.selecionado = False

        container.dados = dados

        return container

    def criar_label(self, master, cnf={}, pack={}):
        cnf['fg'] = 'white'
        cnf['height'] = 2

        pack['side'] = 'left'

        label = TKUtils.obter_label(master=master, cnf=cnf, pack=pack)
        label.cnf = cnf

        comando = self.eventos['expandir']
        label.bind('<Button-1>', lambda evt=None: comando(evt, master.master))

        return label

    def criar_botao_sortear(self, master, cnf={}, pack={}):
        if 'dados' in dir(master.master):
            dados = master.master.dados
        else:
            dados = master.dados

        cnf['text'] = 'O'
        cnf['bg'] = 'orange'
        cnf['bd'] = 4
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.eventos['sortear'](valor=dados)

        pack['side'] = 'left'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)
        botao.cnf = cnf

        return botao

    def criar_botao_remover(self, master, id_elemento, cnf={}, pack={}):
        cnf['text'] = 'X'
        cnf['bg'] = 'red'
        cnf['bd'] = 4
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.eventos['remover'](id_elemento)

        pack['side'] = 'left'

        botao = TKUtils.obter_botao(master=master, cnf=cnf, pack=pack)
        botao.cnf = cnf

        return botao
