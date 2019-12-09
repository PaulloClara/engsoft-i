from src.utils import Utils
from src.store import Store

from src.model.aluno import Aluno
from src.model.grupo import Grupo
from src.model.atividade import Atividade
from src.model.sobre import Sobre

from src.model.apresentacao import Apresentacao


class Model:

    def __init__(self, controller):
        self.controller = controller

        self.store = None

        self.aluno = None
        self.atividade = None
        self.grupo = None
        self.sobre = None

        self.apresentacao = None

    def segundo_init(self):
        self.store = Store()

        self.aluno = Aluno(model=self)
        self.grupo = Grupo(model=self)
        self.atividade = Atividade(model=self)
        self.sobre = Sobre(model=self)

        self.apresentacao = Apresentacao(model=self)

    def iniciar(self):
        pass

    def sortear(self, defs):
        aluno, atividade = None, None

        erro = self.validar_sorteio()
        if erro:
            return erro, aluno, atividade

        if defs and defs['tipo'] == 'aluno':
            aluno = defs['valor']
        else:
            fim = len(self.aluno.alunos) - 1
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)
            aluno = self.aluno.alunos[index]

        if defs and defs['tipo'] == 'atividade':
            atividade = defs['valor']
        else:
            fim = len(self.atividade.atividades) - 1
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)
            atividade = self.atividade.atividades[index]

        return erro, aluno, atividade

    def validar_sorteio(self):
        if not self.aluno.alunos:
            return 'Lista de estudantes vazia'

        if not self.atividade.atividades:
            return 'Lista de atividades vazia'

        return None
