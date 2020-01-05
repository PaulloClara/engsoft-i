from src.utils.tk import TKUtils


class Listagem(TKUtils.obter_scrollview()):

    def __init__(self):
        super().__init__()

        self.defs.cnf['bd'] = 2
        self.defs.cnf['bg'] = 'grey'
        self.defs.cnf['relief'] = 'flat'

        self.defs.pack['expand'] = True
        self.defs.pack['side'] = 'bottom'

        self.defs.canvas['width'] = 920
        self.defs.canvas['height'] = 360

        self.defs.scrollbar['bd'] = 4
        self.defs.scrollbar['bg'] = 'grey'
        self.defs.scrollbar['relief'] = 'flat'

        self.elemento = None
        self.elementos = []

    def iniciar(self, master):
        super().iniciar(master=master)

    def obter(self, _id, filtro='_id'):
        for i, elemento in enumerate(self.elementos):
            if filtro in elemento.dados and elemento.dados['_id'] == _id:
                return {'elemento': elemento, 'index': i}

    def remover(self, _id, filtro='_id'):
        resultado = self.obter(_id, filtro)

        resultado['elemento'].destroy()
        del self.elementos[resultado['index']]

    def criar_elemento(self, dados, integrantes=False):
        instanciar = True

        elemento = TKUtils.obter_container(instanciar)
        elemento.subelemento.primario = TKUtils.obter_container(instanciar)
        elemento.subelemento.secundario = TKUtils.obter_container(instanciar)

        elemento.defs.cnf['bd'] = 2
        elemento.defs.cnf['bg'] = 'grey'
        elemento.defs.cnf['relief'] = 'ridge'

        elemento.dados = dados

        elemento.subelemento.primario.defs.cnf['bd'] = 1
        elemento.subelemento.primario.defs.cnf['bg'] = 'grey'
        elemento.subelemento.primario.defs.cnf['relief'] = 'ridge'

        elemento.subelemento.primario.defs.pack['side'] = 'top'

        elemento.subelemento.secundario.defs.cnf['bd'] = 1
        elemento.subelemento.secundario.defs.cnf['bg'] = 'grey'
        elemento.subelemento.secundario.defs.cnf['relief'] = 'ridge'

        elemento.subelemento.secundario.defs.pack['side'] = 'bottom'

        if integrantes:
            elemento.subelemento.integrantes =\
                TKUtils.obter_container(instanciar)
            elemento.subelemento.integrantes.defs.cnf['bd'] = 1
            elemento.subelemento.integrantes.defs.cnf['bg'] = 'grey'
            elemento.subelemento.integrantes.defs.cnf['relief'] = 'ridge'
            elemento.subelemento.integrantes.lista = []

        elemento.iniciar(master=self.viewport)

        return elemento

    def criar_label(self):
        label = TKUtils.obter_label()

        label.defs.cnf['fg'] = 'white'
        label.defs.cnf['height'] = 2

        label.defs.pack['side'] = 'left'

        return label

    def criar_botao_sortear(self):
        botao = TKUtils.obter_botao()

        botao.defs.cnf['text'] = 'O'
        botao.defs.cnf['bg'] = 'orange'
        botao.defs.cnf['bd'] = 4
        botao.defs.cnf['width'] = 2
        botao.defs.cnf['relief'] = 'raised'

        botao.defs.pack['side'] = 'left'

        return botao

    def criar_botao_remover(self):
        botao = TKUtils.obter_botao()

        botao.defs.cnf['text'] = 'X'
        botao.defs.cnf['bg'] = 'red'
        botao.defs.cnf['bd'] = 4
        botao.defs.cnf['width'] = 2
        botao.defs.cnf['relief'] = 'raised'

        botao.defs.pack['side'] = 'right'

        return botao
