from src.utils.tipo import Tipo


class Listagem(object):

    def __init__(self) -> None:
        pass

    def sortear_(self, evt: Tipo.evento_tk(), aluno: str) -> None:
        self.model.aluno.aluno = aluno

        self.view.ocultar_container_ativo()
        self.view.mostrar_container('home')

        self.cadastrar_tarefa(evt=None)

    def configurar_(self, elemento: Tipo.elemento_tk()) -> None:
        elemento.subelemento.sortear.evento['<Button-1>'] =\
            lambda evt: self.sortear_(evt, aluno=elemento.dados)

        elemento.carregar_eventos()

    def configurar(self) -> None:
        for aluno in self.model.aluno.alunos:
            elemento = self.view.aluno.listagem.adicionar(nome_do_aluno=aluno)
            self.configurar_(elemento)
