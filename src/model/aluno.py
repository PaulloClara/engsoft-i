class Aluno:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.aluno

        self.alunos = []

        self.ler_arquivo()

    def ler_arquivo(self):
        caminho = 'src/store/alunos.csv'
        arquivo = self.store.obter_arquivo(caminho=caminho, modo='r')

        for linha in arquivo:
            self.alunos.append(self.limpar_linha(linha=linha))

        arquivo.close()

    def limpar_linha(self, linha):
        return linha.replace('\n', '').title()
