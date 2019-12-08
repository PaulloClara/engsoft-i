class Aluno:

    def __init__(self, controller):
        self.view = controller.view
        self.model = controller.model

    def carregar_lista_de_alunos(self):
        for aluno in self.model.aluno.alunos:
            self.view.aluno.lista_de_alunos.adicionar(nome_do_aluno=aluno)

    def evento_carregar_arquivo(self):
        pass

    def evento_elemento_montado(self):
        self.view.aluno.iniciar()
        self.carregar_lista_de_alunos()
