class Aluno:

    def __init__(self, controller):
        self.__controller = controller

    def carregar_lista_de_alunos(self):
        view = self.__controller.view.aluno
        model = self.__controller.model.aluno

        for aluno in model.alunos:
            view.lista_de_alunos.adicionar(nome_do_aluno=aluno)

    def evento_carregar_arquivo(self):
        pass

    def evento_montado(self):
        self.carregar_lista_de_alunos()
