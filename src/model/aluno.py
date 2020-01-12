from src import ARQUIVO_CSV
from src.model.modelo import Modelo


class Aluno(Modelo):

    def __init__(self):
        super().__init__()

        self.aluno = None
        self.alunos = []

    def iniciar(self, model):
        super().iniciar(model)

        self.ler_arquivo_csv()

    def sortear(self):
        if self.aluno:
            aluno, self.aluno = self.aluno, None

            return aluno

        return super().sortear(lista=self.alunos)

    def ler_arquivo_csv(self):
        csv = self.store.arquivo(ARQUIVO_CSV, modo='r')

        for linha in csv:
            self.alunos.append(self.formatar(linha))

        csv.close()

    def formatar(self, linha):
        return linha.replace('\n', '').title()
