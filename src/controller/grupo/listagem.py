class Listagem(object):

    def __init__(self):
        pass

    def sortear_(self, evt, grupo: dict) -> None:
        self.model.grupo.grupo = grupo

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_apresentacao(evt=None)

    def remover(self, evt, id_grupo: str) -> None:
        """Evento click do botao remover da lista de grupos."""
        self.model.grupo.remover(id_grupo)
        self.view.grupo.listagem.remover(id_grupo)

    def expandir_recolher(self, evt, elemento):
        if not elemento.subelemento.integrantes.lista:
            self.view.grupo.listagem.inicializar_integrantes(elemento)

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
        primario.subelemento.sortear.evento['<Button-1>'] =\
            lambda evt: self.sortear_(evt, elemento.dados)
        primario.subelemento.remover.evento['<Button-1>'] =\
            lambda evt: self.remover(evt, elemento.dados['id_grupo'])

        secundario.subelemento.cadastro.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)
        secundario.subelemento.total.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)

        elemento.carregar_eventos()

    def configurar(self) -> None:
        """Busca os grupos no Model e carrega a listagem dos grupos na View."""
        for grupo in self.model.grupo.grupos:
            elemento = self.view.grupo.listagem.adicionar(grupo)
            self.configurar_(elemento)
