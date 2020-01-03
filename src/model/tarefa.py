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

    def obter(self, id_tarefa):
        return super().obter(_id=id_tarefa)

    def carregar(self):
        self.tarefas = super().carregar()

        for tarefa in self.tarefas:
            atividade = self.model.atividade.obter(tarefa['id_atividade'])

            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            tarefa['atividade'] = atividade[0]

            nome_aluno = tarefa['aluno']
            titulo_atividade = tarefa['atividade']['titulo']
            tarefa['titulo'] = f'{nome_aluno} - {titulo_atividade}'

    def cadastrar(self, tarefa):
        vals = []
        vals.append(tarefa['id_atividade'])
        vals.append(tarefa['aluno'])
        vals.append(tarefa['duracao'])
        vals.append(tarefa['data_tarefa'])
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)
        self.carregar()

        tarefa = self.tarefas[-1]

        return tarefa

    def remover(self, id_tarefa):
        tarefa = self.obter(id_tarefa)[0]

        id_atividade = tarefa['id_atividade']
        self.model.atividade.atualizar(id_atividade, campos={'em_uso': 0})

        super().remover(_id=id_tarefa)

        return {'atividade': id_atividade}

    def validar(self, formulario):
        data = formulario['data_tarefa']
        duracao = formulario['duracao']

        if not data:
            return 'O campo "Apresentação" não pode estar vazio!'

        if not duracao:
            return 'O campo "Duração" não pode estar vazio!'

        if data[2] != '/' or data[5] != '/':
            return 'Formato invalido! Entre com o formato dd/mm/aaaa'

        dia, mes, ano = data.split('/')

        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except Exception as e:
            return 'Os valores em dd, mm e aaaa precisam ser numeros!'

        data_valida = False

        meses_com_ate_31_dias = [1, 3, 5, 7, 8, 10, 12]
        if mes in meses_com_ate_31_dias:
            if dia <= 31:
                data_valida = True

        meses_com_ate_30_dias = [4, 6, 9, 11]
        if mes in meses_com_ate_30_dias:
            if dia <= 30:
                data_valida = True

        if mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                # Ano Bisexto! Fevereiro com possíveis 29 dias
                if dia <= 29:
                    data_valida = True

            if dia <= 28:
                data_valida = True

        if not data_valida:
            return 'Data INVALIDA!'

        try:
            duracao = int(duracao)
        except Exception as e:
            return 'O campo "Duração" só aceita valor inteiro!'

        if duracao < 5:
            return 'O tempo mínimo da apresentação é 5 min!'

        if duracao > 60:
            return 'Duração máxima de cada apresentação é 60 min!'

        return None
