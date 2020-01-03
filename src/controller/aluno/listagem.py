class Listagem(object):

    def __init__(self):
        pass

    def sortear_(self, evt, aluno):
        self.model.aluno.aluno = aluno

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_tarefa(evt=None)

    def expandir_label(self, evt, elemento):
        pass

    def configurar_(self, elemento):
        elemento.subelemento.sortear.evento['<Button-1>'] =\
            lambda evt: self.sortear_(evt, aluno=elemento.dados)

        elemento.carregar_eventos()

    def configurar(self):
        for aluno in self.model.aluno.alunos:
            elemento = self.view.aluno.listagem.adicionar(nome_do_aluno=aluno)
            self.configurar_(elemento)
