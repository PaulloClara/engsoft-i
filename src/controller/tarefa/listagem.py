class Listagem(object):

    def __init__(self):
        pass

    def remover(self, evt, id_tarefa: str) -> None:
        ids = self.model.tarefa.remover(id_tarefa)
        self.view.home.listagem.remover(id_tarefa, filtro='aluno')

        self.model.atividade.atualizar(ids['atividade'], campos={'em_uso': 0})
        self.view.atividade.listagem.ativar(ids['atividade'])

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
        for tarefa in self.model.tarefa.tarefas:
            elemento = self.view.home.listagem.adicionar(tarefa=tarefa)
            self.configurar_(elemento)
