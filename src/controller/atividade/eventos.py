class Eventos(object):

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def sortear(self, valor):
        self.model.atividade.atividade = valor

        self.view.destruir_container_ativo()
        self.view.criar_container_home()

        self.view.home.criar_janela_de_cadastro()

    def cadastrar(self) -> None:
        """Evento click do botao cadastrar.

        - Cria a janela cadastro.
        """
        self.view.atividade.criar_janela_de_cadastro()

    def confirmar_cadastro(self) -> None:
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

        atividade = self.model.atividade.atividades[-1]
        self.view.atividade.lista.adicionar(atividade=atividade)

    def cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar do formulario.

        - Destroi a janela de cadastro
        """
        self.view.atividade.destruir_janela_de_cadastro()

    def remover_atividade(self, id_atividade: str) -> None:
        """Evento click do botao remover atividade no label da listagem.

        Args:
            id_atividade (str): id da atividade que sera removida do bd

        - Remove atividade do id passado como parametro
        - Destroi a listagem de atividades na view
        - Carrega a nova lista de atividades na view
        """
        self.model.atividade.remover_atividade(id_atividade=id_atividade)
        self.view.atividade.lista.remover_elemento(id_atividade, 'id_atividade')

    def expandir_label(self, evento, elemento):
        self.view.atividade.lista.expandir(elemento=elemento)
