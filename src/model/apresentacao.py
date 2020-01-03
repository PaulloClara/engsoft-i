from src.utils import Utils
from src.model.modelo import Modelo


class Apresentacao(Modelo):

    def __init__(self):
        super().__init__()

        self.tabela = 'apresentacao'
        self.apresentacoes = []

    def iniciar(self, model):
        super().iniciar(model)

        self.carregar()
        self.ordenar()

    def obter(self, _id):
        return super().obter(_id)

    def carregar(self):
        self.apresentacoes = super().carregar()

        for apresentacao in self.apresentacoes:
            id_grupo = apresentacao['id_grupo']
            id_atividade = apresentacao['id_atividade']

            grupo = self.model.grupo.obter(id_grupo)
            atividade = self.model.atividade.obter(id_atividade)

            if not grupo:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if not atividade:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            apresentacao['grupo'] = grupo[0]
            apresentacao['atividade'] = atividade[0]

            nome_grupo = apresentacao['grupo']['nome']
            titulo_atividade = apresentacao['atividade']['titulo']
            apresentacao['titulo'] = f'{nome_grupo} | {titulo_atividade}'

    def cadastrar(self, apresentacao):
        vals = []
        vals.append(apresentacao['id_atividade'])
        vals.append(apresentacao['id_grupo'])
        vals.append(apresentacao['duracao'])
        vals.append(apresentacao['data'])
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)
        self.carregar()

        apresentacao = self.apresentacoes[-1]
        self.ordenar()

        return apresentacao

    def remover(self, _id):
        apresentacao = self.obter(_id)[0]

        id_grupo = apresentacao['id_grupo']
        id_atividade = apresentacao['id_atividade']

        self.model.grupo.atualizar(id_grupo, campos={'em_uso': 0})
        self.model.atividade.atualizar(id_atividade, campos={'em_uso': 0})

        super().remover(_id)

        for i, apresentacao in enumerate(self.apresentacoes):
            if apresentacao['_id'] == _id:
                del self.apresentacoes[i]

        return {'atividade': id_atividade, 'grupo': id_grupo}

    def ordenar(self):
        dp = 'data'
        self.apresentacoes.sort(key=lambda a: a[dp].split('/')[::-1])

    def validar(self, formulario):
        data, duracao = formulario['data'], formulario['duracao']

        if not self.model.atividade.atividades:
            return 'Lista de Atividades vazia'

        if not self.model.grupo.grupos:
            return 'Lista de Grupos vazia'

        if not data:
            return 'O campo "Apresentação" não pode estar vazio!'
        if not duracao:
            return 'O campo "Duração" não pode estar vazio!'

        if data[2] != '/' or data[5] != '/':
            return 'Formato invalido! Entre com o formato dd/mm/aaaa'

        dia, mes, ano = data.split('/')
        data_atual = Utils.data_e_hora_atual().split(' ')[0].split('/')

        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except Exception as e:
            return 'Os valores em dd, mm e aaaa precisam ser numeros!'

        data_valida = False

        if data_atual[::-1] > data.split('/')[::-1]:
            return 'Data INVALIDA'

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
