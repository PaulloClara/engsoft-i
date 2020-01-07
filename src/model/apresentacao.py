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

            apresentacao['grupo'] = grupo
            apresentacao['atividade'] = atividade

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
        apresentacao = self.obter(_id)

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
        chave = 'data'
        self.apresentacoes.sort(key=lambda a: a[chave].split('/')[::-1])

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

        if formulario['duracao'] < 5:
            return 'O tempo mínimo da apresentação é 5 min!'

        if formulario['duracao'] > 60:
            return 'Duração máxima de cada apresentação é 60 min!'

        return erro if erro else None
