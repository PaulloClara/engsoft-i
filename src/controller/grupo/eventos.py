class Eventos(object):

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def sortear(self, valor: dict) -> None:
        self.model.grupo.grupo = valor

        self.view.desativar_container_ativo()

        self.view.home.ativar()
        self.view.container_ativo = 'home'

        self.view.home.criar_janela_de_cadastro()

    def cadastrar(self) -> None:
        """Evento click do botao cadastrar.

        - Cria a janela de cadastro
        """
        self.view.grupo.criar_janela_de_cadastro()

    def confirmar_cadastro(self) -> None:
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

        index = len(self.model.grupo.grupos) - len(grupos)
        for grupo in self.model.grupo.grupos[index:]:
            self.view.grupo.lista.adicionar(grupo=grupo)

    def cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar no formulario.

        - Destroi a janela de cadastro
        """
        self.view.grupo.destruir_janela_de_cadastro()

    def remover_grupo(self, id_grupo: str) -> None:
        """Evento click do botao remover da lista de grupos.

        Args:
            id_grupo (str): ID do grupo que sera removido

        - Remove o grupo do bd
        - Destroi a lista de grupos
        - Carrega a lista de grupos
        """
        self.model.grupo.remover_grupo(id_grupo=id_grupo)
        self.view.grupo.lista.remover_elemento(id_grupo, 'id_grupo')

    def expandir_label(self, evento, elemento):
        self.view.grupo.lista.expandir(elemento=elemento)
