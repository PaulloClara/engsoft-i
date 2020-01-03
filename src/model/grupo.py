from src.utils import Utils
from src.model.modelo import Modelo


class Grupo(Modelo):

    def __init__(self):
        super().__init__()

        self.tabela = 'grupo'

        self.grupo = None
        self.grupos = []

    def iniciar(self, model):
        super().iniciar(model)
        self.carregar()

    def sortear(self) -> dict or None:
        if self.grupo:
            grupo, self.grupo = self.grupo, None

            return grupo

        return super().sortear(lista=self.grupos)

    def obter(self, id_grupo):
        return super().obter(_id=id_grupo)

    def carregar(self):
        self.grupos = super().carregar()

        for grupo in self.grupos:
            grupo['integrantes'] =\
                grupo['integrantes'][1:-2].replace("'", '').split(', ')

    def cadastrar(self, grupo):
        vals = []
        vals.append(grupo['nome'].capitalize())
        vals.append(grupo['integrantes'])
        vals.append(0)
        vals.append(Utils.data_e_hora_atual())

        super().cadastrar(vals)
        self.carregar()

    def atualizar(self, id_grupo, campos):
        super().atualizar(_id=id_grupo, campos=campos)
        self.carregar()

    def remover(self, id_grupo):
        super().remover(_id=id_grupo)
        self.carregar()

    def gerar(self, formulario):
        nome, quantidade = formulario['nome'], int(formulario['quantidade'])

        alunos = self.model.aluno.alunos.copy()

        grupos_gerados = []
        quantidade_grupos = len(alunos) // quantidade

        for i in range(quantidade_grupos):
            grupo = {}
            grupo['nome'] = ''
            grupo['integrantes'] = []

            grupos_gerados.append(grupo)

        for i, grupo in enumerate(grupos_gerados):
            grupo['nome'] = f'{nome}-{i + 1}'

            for j in range(quantidade):
                fim = len(alunos) - 1
                index = Utils.inteiro_aleatorio(inicio=0, fim=fim)

                grupo['integrantes'].append(alunos[index])

                del alunos[index]

        # alunos sem grupo
        fim = quantidade_grupos - 1

        for aluno in alunos:
            index = Utils.inteiro_aleatorio(inicio=0, fim=fim)

            grupos_gerados[index]['integrantes'].append(aluno)

        return grupos_gerados

    def validar(self, formulario):
        alunos = self.model.aluno.alunos.copy()

        if formulario['nome'] == '':
            return 'O campo "Nome" não pode estar vazio'

        if formulario['quantidade'] == '':
            return 'O campo "Nome Base" não pode estar vazio'

        try:
            quantidade = int(formulario['quantidade'])
        except:
            return 'O campo "Quantidade" só aceita valor inteiro'

        if quantidade < 2:
            return 'A quantidade mínima de integrantes é 2'

        if quantidade > len(alunos):
            return 'Quantidade de integrantes maior que a quantidade de alunos'

        if len(alunos) / quantidade < 2:
            return 'Numero de integrantes insuficientes para gerar grupos'

        return None

    def limpar(self, formulario):
        formulario['nome'] = ''
        formulario['quantidade'] = ''
