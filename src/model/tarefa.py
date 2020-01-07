from src.utils import Utils
from src.model.modelo import Modelo


class Tarefa(Modelo):

    def __init__(self):
        super().__init__()
        self.tabela = 'tarefa'

        self.tarefas = []

    def iniciar(self, model):
        self.model = model
        self.store = self.model.store

        self.carregar()

    def obter(self, _id):
        return super().obter(_id)

    def carregar(self):
        self.tarefas = super().carregar()

        for tarefa in self.tarefas:
            atividade = self.model.atividade.obter(tarefa['id_atividade'])

            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            tarefa['atividade'] = atividade

            nome_aluno = tarefa['aluno']
            titulo_atividade = tarefa['atividade']['titulo']
            tarefa['titulo'] = f'{nome_aluno} - {titulo_atividade}'

    def cadastrar(self, tarefa):
        vals = []
        vals.append(tarefa['id_atividade'])
        vals.append(tarefa['aluno'])
        vals.append(tarefa['duracao'])
        vals.append(tarefa['data'])
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)
        self.carregar()

        tarefa = self.tarefas[-1]

        return tarefa

    def remover(self, _id):
        tarefa = self.obter(_id)

        id_atividade = tarefa['id_atividade']
        self.model.atividade.atualizar(id_atividade, campos={'em_uso': 0})

        super().remover(_id)

        return {'atividade': id_atividade}

    def validar(self, formulario):
        erro = super().validar_campos(formulario)
        erro = super().validar_data(formulario['data'])

        try:
            formulario['duracao'] = int(formulario['duracao'])
        except Exception as e:
            return 'O campo "Duração" só aceita valor inteiro!'

        if formulario['duracao'] < 5:
            return 'O tempo mínimo da apresentação é 5 min!'
        if formulario['duracao'] > 60:
            return 'Duração máxima de cada apresentação é 60 min!'

        return erro if erro else None
