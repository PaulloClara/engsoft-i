class Eventos(object):

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def cadastrar_apresentacao(self) -> None:
        """Evento click do botao cadastrar na actions.

        - Cria a janela de cadastro
        """
        self.view.home.criar_janela_de_cadastro()

    def confirmar_cadastro(self) -> None:
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

        elemento = self.model.apresentacao.apresentacoes[-1]
        self.view.home.lista.adicionar(elemento)

        self.view.atividade.lista.mudar_estado(id_atividade, 'id_atividade')
        self.view.grupo.lista.mudar_estado(id_grupo, 'id_grupo')

    def cancelar_cadastro(self) -> None:
        """Evento click do botao cancelar no formulario de cadastro."""
        self.view.home.destruir_janela_de_cadastro()

    def remover_apresentacao(self, id_apr: str) -> None:
        """Evento click do botao remover na lista de apresentacoes."""
        id_atv, id_grupo =\
            self.model.apresentacao.remover_apresentacao(id_apr=id_apr)

        self.view.home.lista.remover_elemento(id_apr, 'id_apresentacao')

        self.view.atividade.lista.mudar_estado(id_atv, 'id_atividade', False)
        self.view.grupo.lista.mudar_estado(id_grupo, 'id_grupo', False)

    def ordenar_lista(self) -> None:
        """Evento click do botao ordenar na actions."""
        pass

    def expandir_label(self, evento, elemento):
        self.view.home.lista.expandir(elemento=elemento)
