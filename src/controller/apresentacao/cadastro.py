class Cadastro(object):

    def __init__(self):
        pass

    def confirmar(self, evt=None) -> None:
        """Evento click do botao confirmar no formulario de cadastro."""
        formulario = self.view.home.cadastro_apresentacao.obter_campos()

        erro = self.model.apresentacao.validar(formulario)
        if erro:
            return self.view.janela_erro.iniciar(erro)

        erro = 'Todos os Grupos estão em uso'
        grupo = self.model.grupo.sortear()
        if not grupo:
            return self.view.janela_erro.iniciar(erro)

        id_grupo = grupo['id_grupo']
        formulario['id_grupo'] = id_grupo

        erro = 'Todas as Atividades estão em uso'
        atividade = self.model.atividade.sortear()
        if not atividade:
            self.view.janela_erro.iniciar(erro)
            return

        id_atividade = atividade['id_atividade']
        formulario['id_atividade'] = id_atividade

        apresentacao = self.model.apresentacao.cadastrar(formulario)

        self.model.grupo.atualizar(id_grupo, campos={'em_uso': 1})
        self.model.atividade.atualizar(id_atividade, campos={'em_uso': 1})

        self.view.home.cadastro_apresentacao.fechar()

        elemento = self.view.home.listagem.adicionar(apresentacao)
        self.configurar_(elemento)

        self.view.grupo.listagem.desativar(id_grupo)
        self.view.atividade.listagem.desativar(id_atividade)

    def cancelar(self, evt=None) -> None:
        """Evento click do botao cancelar no formulario de cadastro."""
        self.view.home.cadastro_apresentacao.fechar()

    def configurar(self) -> None:
        cadastro = self.view.home.cadastro_apresentacao.subelemento

        cadastro.data.input.evento['<Return>'] = self.confirmar
        cadastro.duracao.input.evento['<Return>'] = self.confirmar

        cadastro.cancelar.defs.mcnf['command'] = self.cancelar
        cadastro.confirmar.defs.mcnf['command'] = self.confirmar

        self.view.home.cadastro_apresentacao.carregar_eventos()
