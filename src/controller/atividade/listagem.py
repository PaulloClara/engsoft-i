class Listagem(object):

    def __init__(self):
        pass

    def sortear_(self, evt, atividade):
        self.model.atividade.atividade = atividade

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_apresentacao(evt=None)

    def remover(self, evt, id_atividade: str) -> None:
        """Evento click do botao remover atividade no label da listagem."""
        self.model.atividade.remover(id_atividade)
        self.view.atividade.listagem.remover(id_atividade, 'id_atividade')

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
        primario.subelemento.sortear.evento['<Button-1>'] =\
            lambda evt: self.sortear_(evt, elemento.dados)
        primario.subelemento.remover.evento['<Button-1>'] =\
            lambda evt: self.remover(evt, elemento.dados['id_atividade'])

        secundario.subelemento.cadastro.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)
        secundario.subelemento.descricao.evento['<Button-1>'] =\
            lambda evt: self.expandir_recolher(evt, elemento)

        elemento.carregar_eventos()

    def configurar(self) -> None:
        """Busca as atividades no Model e cria os componentes visuais."""
        for atividade in self.model.atividade.atividades:
            elemento = self.view.atividade.listagem.adicionar(atividade)
            self.configurar_(elemento)
