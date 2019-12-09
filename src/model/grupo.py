from src.utils import Utils


class Grupo:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.grupo

        self.tabela = 'grupo'
        self.colunas = ['id_do_grupo', 'nome', 'tamanho', 'integrantes']

        self.grupos = []

        self.obter_grupos()

    def obter_grupo(self, id_do_grupo):
        condicao = f'id_do_grupo == "{id_do_grupo}"'
        codigo_sql =\
            self.store.select(tabela=self.tabela, colunas=self.colunas, condicao=condicao)

        return self.store.executar(codigo_sql=codigo_sql, colunas=self.colunas)

    def obter_grupos(self):
        codigo_sql = self.store.select(tabela=self.tabela, colunas=self.colunas)
        self.grupos =\
            self.store.executar(codigo_sql=codigo_sql, colunas=self.colunas)

    def cadastrar_grupo(self, grupo):
        grupo['nome'] = grupo['nome'].capitalize()
        tamanho = len(grupo['integrantes'])
        valores = [grupo['nome'], tamanho, grupo['integrantes']]

        codigo_sql =\
            self.store.insert(
                tabela=self.tabela, colunas=self.colunas[1:], valores=valores)
        self.store.executar(codigo_sql=codigo_sql)

        self.obter_grupos()

    def gerar_grupos(self, formulario):
        nome_base = formulario['nome']
        alunos_por_grupo = int(formulario['quantidade'])

        alunos = self.model.aluno.alunos

        grupos_gerados = []
        quantidade_de_grupos = len(alunos) // alunos_por_grupo

        for i in range(quantidade_de_grupos):
            grupo = {}
            grupo['nome'] = ''
            grupo['tamanho'] = 0
            grupo['integrantes'] = []

            grupos_gerados.append(grupo)

        for i, grupo in enumerate(grupos_gerados):
            grupo['nome'] = f'{nome_base}-{i + 1}'

            for j in range(alunos_por_grupo):
                index_do_aluno = Utils.obter_inteiro_aleatorio(0, len(alunos) - 1)

                grupo['integrantes'].append(alunos[index_do_aluno])
                grupo['tamanho'] += 1

                del alunos[index_do_aluno]

        # alunos sem grupo
        for aluno in alunos:
            index_do_grupo = Utils.obter_inteiro_aleatorio(0, quantidade_de_grupos - 1)

            grupos_gerados[index_do_grupo]['integrantes'].append(aluno)
            grupos_gerados[index_do_grupo]['tamanho'] += 1

        return grupos_gerados

    def remover_grupo(self, id_do_grupo):
        condicao = f'id_do_grupo = {id_do_grupo}'
        codigo_sql = self.store.delete(tabela=self.tabela, condicao=condicao)
        self.store.executar(codigo_sql=codigo_sql)

        self.obter_grupos()

    def validar_campos(self, formulario):
        return 'ok'

    def limpar_formulario(self, formulario):
        formulario['nome'] = ''
        formulario['quantidade'] = ''
