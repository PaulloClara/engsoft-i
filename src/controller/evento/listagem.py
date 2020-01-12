class Listagem(object):

    def __init__(self):
        pass

    def remover(self, evt, id_apresentacao: str) -> None:
        self.model.evento.remover(id_apresentacao)
        self.view.home.listagem.remover(id_apresentacao, filtro='titulo')

    def expandir_recolher(self, evt, elemento):
        if not elemento.subelemento.integrantes.lista:
            self.view.home.listagem.inicializar_integrantes(elemento)

        if elemento.subelemento.secundario.defs.visivel:
            elemento.subelemento.secundario.ocultar()
            elemento.subelemento.integrantes.ocultar()
        else:
            elemento.subelemento.secundario.mostrar()
            elemento.subelemento.integrantes.mostrar()

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
        for evento in self.model.evento.eventos:
            elemento = self.view.home.listagem.adicionar(evento=evento)
            self.configurar_(elemento)
