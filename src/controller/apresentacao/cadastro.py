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

        erro = 'Todas as Atividades estão em uso'
        atividade = self.model.atividade.sortear()
        if not atividade:
            return self.view.janela_erro.iniciar(erro)

        formulario['id_grupo'] = grupo['_id']
        formulario['id_atividade'] = atividade['_id']

        apresentacao = self.model.apresentacao.cadastrar(formulario)

        elemento = self.view.home.listagem.adicionar(apresentacao)
        self.configurar_(elemento)

        self.view.grupo.listagem.desativar(grupo['_id'])
        self.model.grupo.atualizar(grupo['_id'], campos={'em_uso': 1})

        self.view.atividade.listagem.desativar(atividade['_id'])
        self.model.atividade.atualizar(atividade['_id'], campos={'em_uso': 1})

        self.view.home.cadastro_apresentacao.fechar()

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
