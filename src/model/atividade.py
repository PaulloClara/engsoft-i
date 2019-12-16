from src.utils import Utils


class Atividade:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.atividade

        self.tabela = 'atividade'
        self.colunas = ['id_atividade', 'titulo', 'descricao', 'em_uso',
                        'data_cadastro']

        self.atividades = []
        self.atividade = None

    def iniciar(self):
        self.obter_atividades()

    def sortear(self):
        atividades_disponiveis = []

        atividade = self.atividade
        if atividade:
            self.atividade = None

            return atividade

        for atividade in self.atividades:
            if not atividade['em_uso']:
                atividades_disponiveis.append(atividade)

        if atividades_disponiveis:
            fim = len(atividades_disponiveis) - 1
            index = Utils.obter_inteiro_aleatorio(inicio=0, fim=fim)

            return atividades_disponiveis[index]

        return None

    def obter_atividade(self, id_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_atividade == "{id_atividade}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_atividades(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.atividades = self.store.executar(codigo_sql=sql, colunas=cols)

    def cadastrar_atividade(self, atividade):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        vals.append(atividade['titulo'].capitalize())
        vals.append(atividade['descricao'].capitalize())
        vals.append(0)
        vals.append(Utils.obter_data_e_hora_atual())

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_atividades()

    def atualizar_uso(self, id_atividade, valor=1):
        tab = self.tabela
        cam = f'em_uso = {valor}'
        con = f'id_atividade = {id_atividade}'

        sql = self.store.update(tabela=tab, campos=cam, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_atividades()

    def remover_atividade(self, id_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_atividade = {id_atividade}'

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_atividades()

    def validar_campos(self, formulario):
        if formulario['titulo'] == '':
            return 'O campo "Titulo" não pode estar vazio'

        if formulario['descricao'] == '':
            return 'O campo "Descrição" não pode estar vazio'

        return None

    def limpar_formulario(self, formulario):
        formulario['titulo'] = ''
        formulario['descricao'] = ''
