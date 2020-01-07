from src.utils import Utils
from src.model.modelo import Modelo


class Evento(Modelo):

    def __init__(self):
        super().__init__()

        self.tabela = 'evento'
        self.eventos = []

    def iniciar(self, model):
        super().iniciar(model)

        self.carregar()
        self.ordenar()

    def obter(self, _id):
        return super().obter(_id)

    def carregar(self):
        self.eventos = super().carregar()

    def cadastrar(self, evento):
        vals = []
        vals.append(evento['titulo'])
        vals.append(evento['duracao'])
        vals.append(evento['data'])
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)
        self.carregar()

        evento = self.eventos[-1]
        self.ordenar()

        return evento

    def remover(self, _id):
        super().remover(_id)

    def ordenar(self):
        chave = 'data'
        self.eventos.sort(key=lambda a: a[chave].split('/')[::-1])

    def validar(self, formulario):
        erro = super().validar_campos(formulario)
        erro = super().validar_data(formulario['data'])

        if not self.model.atividade.atividades:
            return 'Lista de Atividades vazia'

        if not self.model.grupo.grupos:
            return 'Lista de Grupos vazia'

        try:
            formulario['duracao'] = int(formulario['duracao'])
        except Exception as e:
            return 'O campo "Duração" só aceita valor inteiro!'

        return erro if erro else None
