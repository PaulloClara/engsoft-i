from src.utils import Utils


class Aluno:

    def __init__(self, model, controller):
        self.__model = model
        self.__controller = controller

        self.alunos = []

        self.ler_arquivo()

    def ler_arquivo(self):
        arquivo = open(Utils.obter_caminho('src/store/alunos.csv'), mode='r')

        for linha in arquivo:
            self.alunos.append(self.limpar_linha(linha=linha))

        arquivo.close()

    def limpar_linha(self, linha):
        return linha.replace('\n', '').title()
