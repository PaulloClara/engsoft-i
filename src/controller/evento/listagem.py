class Listagem(object):

    def __init__(self):
        pass

    def remover(self, evt, id_apresentacao: str) -> None:
        """Evento click do botao remover na lista de eventos."""
        self.model.evento.remover(id_apresentacao)
        self.view.home.listagem.remover(id_apresentacao, filtro='titulo')

    def expandir_recolher(self, evt, elemento):
        if elemento.subelemento.secundario.defs.visivel:
            elemento.subelemento.secundario.ocultar()
        else:
            elemento.subelemento.secundario.mostrar()

    def configurar_(self, elemento):
        primario = elemento.subelemento.primario
        secundario = elemento.subelemento.secundario

        primario.subelemento.label.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)

        primario.subelemento.remover.evento['<Button-1>'] =\
            lambda evt: self.remover(evt, elemento.dados['_id'])

        secundario.subelemento.cadastro.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)

        secundario.subelemento.apresentacao.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)

        elemento.carregar_eventos()

    def configurar(self) -> None:
        """Carrega as eventos na lista de eventos da Home na View."""
        for evento in self.model.evento.eventos:
            elemento = self.view.home.listagem.adicionar(evento=evento)
            self.configurar_(elemento)
