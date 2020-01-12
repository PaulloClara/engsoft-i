from src.utils.atributo import Atributo


class Elemento(object):

    def __init__(self) -> None:
        self.evento = {}
        self.dados = None

        self.defs = Atributo()
        self.subelemento = Atributo()

        self.defs.cnf = {}
        self.defs.mcnf = {}
        self.defs.pack = {}
        self.defs.grid = {}

        self.defs.visivel = False

    def mostrar(self) -> None:
        if self.defs.grid:
            self.grid(self.defs.grid)
        else:
            self.pack(self.defs.pack)

        self.defs.visivel = True

    def ocultar(self) -> None:
        if self.defs.grid:
            self.grid_forget()
        else:
            self.pack_forget()

        self.defs.visivel = False

    def carregar_eventos(self) -> None:
        for key in self.evento:
            self.bind(key, self.evento[key])

        subelementos = filter(lambda v: not '__' in v, dir(self.subelemento))
        for subelemento in list(subelementos):
            elemento = getattr(self.subelemento, subelemento)

            if 'carregar_eventos' in dir(elemento):
                elemento.carregar_eventos()
                continue

            subelementos = filter(lambda v: not '__' in v, dir(elemento))
            for subelemento in list(subelementos):
                getattr(elemento, subelemento).carregar_eventos()
