"""Controller do Grupo."""
from src.controller.grupo.eventos import Eventos


class Grupo(object):
    """Classe responsavel por gerenciar a View e Model relacionados a Grupo.

    Attributes:
        view (View:obj): Objeto root View
        model (Model:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define os atributos view e model."""
        self.view = controller.view
        self.model = controller.model

        self.eventos = Eventos(controller=self)

    def carregar_grupos(self) -> None:
        """Busca os grupos no Model e carrega a listagem dos grupos na View."""
        for grupo in self.model.grupo.grupos:
            self.view.grupo.lista.adicionar(grupo=grupo)

    def elemento_montado(self) -> None:
        """Disparado quando o componente/container Grupo e montado.

        - Inicia o componente/container Grupo
        - Carrea a lista de grupos
        """
        self.view.grupo.iniciar()
        self.carregar_grupos()

        self.view.grupo.desativar()
