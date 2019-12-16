"""Controller da Home e da Apresentacao."""


class Home(object):
    """Classe responsavel por gerenciar Home de View e Apresentacao de Model.

    Attributes:
        view (View:obj): Objeto root View
        model (Model:obj): Objeto root Model
    """

    def __init__(self, controller: object) -> None:
        """Construtor padrao, define os atributos view e model."""
        self.view = controller.view
        self.model = controller.model

    def carregar_apresentacoes(self) -> None:
        """Carrega as apresentacoes na lista de eventos da Home na View."""
        for apresentacao in self.model.apresentacao.apresentacoes:
            self.view.home.lista_de_elementos.adicionar(elemento=apresentacao)

    def evento_cadastrar_apresentacao(self) -> None:
        """Evento click do botao cadastrar na actions.

        - Cria a janela de cadastro
        """
        self.view.home.criar_janela_de_cadastro()

    def evento_confirmar_cadastro(self) -> None:
        """Evento click do botao confirmar no formulario de cadastro."""
        formulario = self.view.home.janela_de_cadastro.obter_campos()

        erro = self.model.apresentacao.validar_cadastro(formulario=formulario)
        if erro:
            self.view.criar_janela_de_erro(erro=erro)
            return

        grupo = self.model.grupo.sortear()
        if not grupo:
            erro = 'Todos os Grupos estão em uso'
            self.view.criar_janela_de_erro(erro=erro)
            return

        id_grupo = grupo['id_grupo']
        formulario['id_grupo'] = id_grupo

        atividade = self.model.atividade.sortear()
        if not atividade:
            erro = 'Todas as Atividades estão em uso'
            self.view.criar_janela_de_erro(erro=erro)
            return

        id_atividade = atividade['id_atividade']
        formulario['id_atividade'] = id_atividade

        self.model.apresentacao.cadastrar_apresentacao(apresentacao=formulario)

        self.model.grupo.atualizar_uso(id_grupo=id_grupo)
        self.model.atividade.atualizar_uso(id_atividade=id_atividade)

        self.view.home.destruir_janela_de_cadastro()

        self.view.home.destruir_lista_de_elementos()
        self.carregar_apresentacoes()

    def evento_cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar no formulario de cadastro."""
        self.view.home.destruir_janela_de_cadastro()

    def evento_remover_apresentacao(self, id_apr: str) -> None:
        """Evento click do botao remover na lista de apresentacoes."""
        self.model.apresentacao.remover_apresentacao(id_apr=id_apr)

        self.view.home.destruir_lista_de_elementos()
        self.carregar_apresentacoes()

    def evento_ordenar_lista(self) -> None:
        """Evento click do botao ordenar na actions."""
        pass

    def evento_expandir_label(self, evento, elemento):
        pass

    def evento_elemento_montado(self) -> None:
        """Evento disparado quando o componente Home na View e montado.

        - Inicia o container Home
        - Carrega a lista de apresentacoes
        """
        self.view.home.iniciar()
        self.carregar_apresentacoes()
