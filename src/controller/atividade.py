"""Controller da Atividade."""


class Atividade(object):
    """Classe responsavel por gerenciar os componentes de Atividade.

    Attributes:
        view (View:obj): Objeto root View
        model (Mode:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Classe responsavel por gerenciar os componentes de Atividade.

        Args:
            controller (Controller:obj): Objeto Pai
        """
        self.view = controller.view
        self.model = controller.model

    def carregar_atividades(self) -> None:
        """Busca as atividades no Model e cria os componentes visuais."""
        for atv in self.model.atividade.atividades:
            self.view.atividade.lista_de_atividades.adicionar(atividade=atv)

    def evento_sortear(self, valor):
        self.model.atividade.atividade = valor

        self.view.destruir_container_ativo()
        self.view.criar_container_home()

        self.view.home.criar_janela_de_cadastro()

    def evento_cadastrar(self) -> None:
        """Evento click do botao cadastrar.

        - Cria a janela cadastro.
        """
        self.view.atividade.criar_janela_de_cadastro()

    def evento_remover_atividade(self, id_atividade: str) -> None:
        """Evento click do botao remover atividade no label da listagem.

        Args:
            id_atividade (str): id da atividade que sera removida do bd

        - Remove atividade do id passado como parametro
        - Destroi a listagem de atividades na view
        - Carrega a nova lista de atividades na view
        """
        self.model.atividade.remover_atividade(id_atividade=id_atividade)

        self.view.atividade.destruir_lista_de_atividades()
        self.carregar_atividades()

        self.model.apresentacao.obter_apresentacoes()

    def evento_confirmar_cadastro(self) -> None:
        """Evento click do botao confirmar cadastro.

        - Obtem os valores dos campos do formulario
        - Verifica se os campos sao validos
            - sim -> continua
            - nao -> cria janela de erro e para o evento
        - Salva atividade
        - Destroi janela de cadastro
        - Destroi listagem de atividades
        - Carrega nova listade de atividades
        """
        form = self.view.atividade.janela_de_cadastro.obter_campos()

        erro = self.model.atividade.validar_campos(formulario=form)
        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        self.model.atividade.cadastrar_atividade(atividade=form)
        self.view.atividade.destruir_janela_de_cadastro()

        self.view.atividade.destruir_lista_de_atividades()
        self.carregar_atividades()

    def evento_cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar do formulario.

        - Destroi a janela de cadastro
        """
        self.view.atividade.destruir_janela_de_cadastro()

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o componente Atividade da View e montado.

        - Inicia o componente/container visual da Atividade
        - Carrega a listagem das atividades na view
        """
        self.view.atividade.iniciar()
        self.carregar_atividades()
