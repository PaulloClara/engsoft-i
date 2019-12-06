from src.store import Store
from src.utils import Utils

from src.model.aluno import Aluno
from src.model.atividade import Atividade
from src.model.grupo import Grupo


class Model:

    def __init__(self, controller):
        self.__controller = controller

        self.store = None
        self.aluno = None
        self.atividade = None
        self.grupo = None

    def segundo_init(self):
        self.store = Store()
        self.aluno = Aluno(model=self, controller=self.__controller)
        self.atividade = Atividade(controller=self.__controller, store=self.store)
        self.grupo = Grupo(controller=self.__controller, store=self.store)

    def iniciar(self):
        pass

    def sortear(self, defs):
        alunos = self.aluno.alunos
        atividades = self.atividade.atividades

        if not alunos:
            return 'Lista de estudantes vazia', None, None

        if not atividades:
            return 'Lista de atividades vazia', None, None

        if defs and defs['tipo'] == 'aluno':
            aluno = defs['valor']
        else:
            aluno = alunos[Utils.obter_inteiro_aleatorio(0, len(alunos)-1)]

        if defs and defs['tipo'] == 'atividade':
            atividade = defs['valor']
        else:
            atividade = atividades[Utils.obter_inteiro_aleatorio(0, len(atividades)-1)]

        return None, aluno, atividade
