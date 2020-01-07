class Cadastro(object):

    def __init__(self):
        pass

    def confirmar(self, evt=None) -> None:
        """Evento click do botao confirmar no formulario de cadastro."""
        formulario = self.view.home.cadastro_evento.obter_campos()

        erro = self.model.evento.validar(formulario)
        if erro:
            return self.view.janela_erro.iniciar(erro)

        evento = self.model.evento.cadastrar(formulario)

        elemento = self.view.home.listagem.adicionar(evento=evento)
        self.configurar_(elemento)

        self.view.home.cadastro_evento.fechar()

    def cancelar(self, evt=None) -> None:
        """Evento click do botao cancelar no formulario de cadastro."""
        self.view.home.cadastro_evento.fechar()

    def configurar(self) -> None:
        cadastro = self.view.home.cadastro_evento.subelemento

        cadastro.data.input.evento['<Return>'] = self.confirmar
        cadastro.titulo.input.evento['<Return>'] = self.confirmar
        cadastro.duracao.input.evento['<Return>'] = self.confirmar

        cadastro.cancelar.defs.mcnf['command'] = self.cancelar
        cadastro.confirmar.defs.mcnf['command'] = self.confirmar

        self.view.home.cadastro_evento.carregar_eventos()
