class Cadastro(object):

    def __init__(self):
        pass

    def confirmar(self, evt=None) -> None:
        """Evento click do botao confirmar do formulario de cadastro."""
        formulario = self.view.grupo.cadastro.obter_campos()

        erro = self.model.grupo.validar(formulario)
        if erro:
            return self.view.janela_erro.iniciar(erro)

        grupos = self.model.grupo.gerar(formulario)
        for grupo in grupos:
            self.model.grupo.cadastrar(grupo)

        index = len(self.model.grupo.grupos) - len(grupos)
        for grupo in self.model.grupo.grupos[index:]:
            elemento = self.view.grupo.listagem.adicionar(grupo)
            self.configurar_(elemento)

        self.view.grupo.cadastro.fechar()

    def cancelar(self, evt=None) -> None:
        """Evento click do botao cancelar no formulario."""
        self.view.grupo.cadastro.fechar()

    def configurar(self):
        cadastro = self.view.grupo.cadastro.subelemento

        cadastro.nome.input.evento['<Return>'] = self.confirmar
        cadastro.quantidade.input.evento['<Return>'] = self.confirmar

        cadastro.cancelar.defs.mcnf['command'] = self.cancelar
        cadastro.confirmar.defs.mcnf['command'] = self.confirmar

        self.view.grupo.cadastro.carregar_eventos()
