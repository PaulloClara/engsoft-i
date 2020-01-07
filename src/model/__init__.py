from src.utils import Utils
from src.store import Store

from src.model.aluno import Aluno
from src.model.grupo import Grupo
from src.model.sobre import Sobre
from src.model.atividade import Atividade

from src.model.evento import Evento
from src.model.tarefa import Tarefa
from src.model.apresentacao import Apresentacao


class Model(object):

    def __init__(self):
        self.store = Store()

        self.aluno = Aluno()
        self.grupo = Grupo()
        self.sobre = Sobre()
        self.atividade = Atividade()

        self.evento = Evento()
        self.tarefa = Tarefa()
        self.apresentacao = Apresentacao()

    def iniciar(self):
        self.aluno.iniciar(model=self)
        self.grupo.iniciar(model=self)
        self.sobre.iniciar(model=self)
        self.atividade.iniciar(model=self)

        self.evento.iniciar(model=self)
        self.tarefa.iniciar(model=self)
        self.apresentacao.iniciar(model=self)
