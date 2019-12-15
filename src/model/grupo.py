from src.utils import Utils


class Grupo:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.grupo

        self.tabela = 'grupo'
        self.colunas = ['id_grupo', 'nome', 'integrantes', 'em_uso',
                        'data_cadastro']

        self.grupos = []
        self.grupo = None

        self.obter_grupos()

    def sortear(self):
        grupos_disponiveis = []

        grupo = self.grupo
        if grupo:
            self.grupo = None

            return grupo

        for grupo in self.grupos:
            if not grupo['em_uso']:
                grupos_disponiveis.append(grupo)

        if grupos_disponiveis:
            fim = len(grupos_disponiveis) - 1
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

            return grupos_disponiveis[index]

        return None

    def obter_grupo(self, id_grupo):
        tab, cols = self.tabela, self.colunas
        con = f'id_grupo == "{id_grupo}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_grupos(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.grupos = self.store.executar(codigo_sql=sql, colunas=cols)

    def cadastrar_grupo(self, grupo):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        vals.append(grupo['nome'].capitalize())
        vals.append(grupo['integrantes'])
        vals.append(0)
        vals.append(Utils.obter_data_e_hora_atual())

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_grupos()

    def atualizar_uso(self, id_grupo, valor=1):
        tab = self.tabela
        cam = f'em_uso = {valor}'
        con = f'id_grupo = {id_grupo}'

        sql = self.store.update(tabela=tab, campos=cam, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_grupos()

    def remover_grupo(self, id_grupo):
        tab = self.tabela
        con = f'id_grupo = {id_grupo}'

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
            grupo['integrantes'] = []

            grupos_gerados.append(grupo)

        for i, grupo in enumerate(grupos_gerados):
            grupo['nome'] = f'{nome_base}-{i + 1}'

            for j in range(alunos_por_grupo):
                fim = len(alunos) - 1
                index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

                grupo['integrantes'].append(alunos[index])

                del alunos[index]

        # alunos sem grupo
        fim = quantidade_de_grupos - 1

        for aluno in alunos:
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

            grupos_gerados[index]['integrantes'].append(aluno)

        return grupos_gerados

    def validar_campos(self, formulario):
        alunos = self.model.aluno.alunos.copy()

        if formulario['nome'] == '':
            return 'O campo "Nome" não pode estar vazio!'

        if formulario['quantidade'] == '':
            return 'O campo "Nome Base" não pode estar vazio!'

        try:
            quantidade = int(formulario['quantidade'])
        except:
            return 'O campo "Quantidade" só aceita valor inteiro!'

        if quantidade < 2:
            return 'A quantidade mínima de integrantes é 2'
        
        if quantidade > len(alunos):
            return 'Quantidade de integrantes maior que a quantidade de alunos!'
        
        if (len(alunos) / quantidade) < 2:
            return 'Numero de integrantes insuficientes para gerar grupos!'

        return None

    def limpar_formulario(self, formulario):
        formulario['nome'] = ''
        formulario['quantidade'] = ''
