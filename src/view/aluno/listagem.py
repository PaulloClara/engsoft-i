from src.view.listagem import Listagem


class ListaDeAlunos(Listagem):

    def __init__(self):
        super().__init__()

    def iniciar(self, master):
        super().iniciar(master=master)

    def adicionar(self, nome_do_aluno):
        elemento = self.criar_elemento(dados=nome_do_aluno)

        elemento.subelemento.label = self.criar_label()
        elemento.subelemento.sortear = self.criar_botao_sortear()

        elemento.subelemento.label.defs.cnf['text'] = nome_do_aluno
        elemento.subelemento.label.defs.cnf['bg'] = 'red'
        elemento.subelemento.label.defs.cnf['width'] = 97

        elemento.iniciar(master=self.viewport)

        elemento.subelemento.label.iniciar(master=elemento)
        elemento.subelemento.sortear.iniciar(master=elemento)

        self.elementos.append(elemento)

        return elemento
