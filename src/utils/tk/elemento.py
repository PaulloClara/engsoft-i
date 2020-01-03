"""Subelemento de Utils."""

from src.utils.atributo import Atributo


class Elemento(object):
    """Salva os dados de cada elemento TK de forma padronizada e organizada."""

    def __init__(self) -> None:
        """Define os atributos customizados que podem ser usados."""
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
        """Deixa o componente visivel com as regras geometricas predefinidas."""
        if self.defs.grid:
            self.grid(self.defs.grid)
        else:
            self.pack(self.defs.pack)

        self.defs.visivel = True

    def ocultar(self) -> None:
        """Oculta o elemento."""
        if self.defs.grid:
            self.grid_forget()
        else:
            self.pack_forget()

        self.defs.visivel = False

    def carregar_eventos(self) -> None:
        """Carrega/ativa os eventos predefinidos do elemento e subelementos."""
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
