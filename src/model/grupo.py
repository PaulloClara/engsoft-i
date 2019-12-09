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
        tab, cols = self.tabela, self.colunas
        con = f'id_do_grupo == "{id_do_grupo}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_grupos(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.grupos = self.store.executar(codigo_sql=sql, colunas=cols)

    def cadastrar_grupo(self, grupo):
        tab, cols = self.tabela, self.colunas[1:]
        vals = [grupo['nome'].capitalize(), len(grupo['integrantes']),
                grupo['integrantes']]

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_grupos()

    def remover_grupo(self, id_do_grupo):
        tab = self.tabela
        con = f'id_do_grupo = {id_do_grupo}'

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_grupos()

    def gerar_grupos(self, formulario):
        nome_base = formulario['nome']
        alunos_por_grupo = int(formulario['quantidade'])

        alunos = self.model.aluno.alunos.copy()

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
                fim = len(alunos) - 1
                index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

                grupo['integrantes'].append(alunos[index])
                grupo['tamanho'] += 1

                del alunos[index]

        # alunos sem grupo
        fim = quantidade_de_grupos - 1

        for aluno in alunos:
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

            grupos_gerados[index]['integrantes'].append(aluno)
            grupos_gerados[index]['tamanho'] += 1

        return grupos_gerados

    def validar_campos(self, formulario):
        return None

    def limpar_formulario(self, formulario):
        formulario['nome'] = ''
        formulario['quantidade'] = ''
