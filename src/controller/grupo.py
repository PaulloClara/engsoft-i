"""Controller do Grupo."""


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

    def carregar_grupos(self) -> None:
        """Busca os grupos no Model e carrega a listagem dos grupos na View."""
        for grupo in self.model.grupo.grupos:
            self.view.grupo.lista_de_grupos.adicionar(grupo=grupo)

    def evento_sortear(self, valor: dict) -> None:
        self.model.grupo.grupo = valor

        self.view.destruir_container_ativo()
        self.view.criar_container_home()

        self.view.home.criar_janela_de_cadastro()

    def evento_cadastrar(self) -> None:
        """Evento click do botao cadastrar.

        - Cria a janela de cadastro
        """
        self.view.grupo.criar_janela_de_cadastro()

    def evento_confirmar_cadastro(self) -> None:
        """Evento click do botao confirmar do formulario de cadastro.

        - Obtem os campos do formulario
        - Valida os campos a procura de erros
            - se tudo ok -> continua
            - se ouver erro -> cria uma janela de erro
        - Gera os grupos de acordo com os dados do formulario
        - Salva cada grupo gerado
        - Destroi janela de cadastro
        - Destroi a lista de grupos
        - Carrega a lista de grupos
        """
        form = self.view.grupo.janela_de_cadastro.obter_campos()

        erro = self.model.grupo.validar_campos(formulario=form)
        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        grupos = self.model.grupo.gerar_grupos(formulario=form)

        for grupo in grupos:
            self.model.grupo.cadastrar_grupo(grupo=grupo)

        self.view.grupo.destruir_janela_de_cadastro()

        self.view.grupo.destruir_lista_de_grupos()
        self.carregar_grupos()

    def evento_cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar no formulario.

        - Destroi a janela de cadastro
        """
        self.view.grupo.destruir_janela_de_cadastro()

    def evento_remover_grupo(self, id_grupo: str) -> None:
        """Evento click do botao remover da lista de grupos.

        Args:
            id_grupo (str): ID do grupo que sera removido

        - Remove o grupo do bd
        - Destroi a lista de grupos
        - Carrega a lista de grupos
        """
        self.model.grupo.remover_grupo(id_grupo=id_grupo)

        self.view.grupo.destruir_lista_de_grupos()
        self.carregar_grupos()

        self.model.apresentacao.obter_apresentacoes()

    def evento_expandir_label(self, evento, elemento):
        self.view.grupo.lista_de_grupos.expandir(elemento=elemento)

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o componente/container Grupo e montado.

        - Inicia o componente/container Grupo
        - Carrea a lista de grupos
        """
        self.view.grupo.iniciar()
        self.carregar_grupos()
