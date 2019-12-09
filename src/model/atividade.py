class Atividade:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller.atividade

        self.tabela = 'atividade'
        self.colunas = ['id_da_atividade', 'titulo', 'desc']

        self.atividades = []

        self.obter_atividades()

    def obter_atividade(self, id_da_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_da_atividade == "{id_da_atividade}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_atividades(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.atividades = self.store.executar(codigo_sql=sql, colunas=cols)

    def cadastrar_atividade(self, atividade):
        tab, cols = self.tabela, self.colunas[1:]
        vals = [atividade['titulo'].capitalize(), atividade['desc']]

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_atividades()

    def remover_atividade(self, id_da_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_da_atividade = {id_da_atividade}'

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_atividades()

    def validar_campos(self, formulario):
        if formulario['titulo'] == '':
            return 'O campo "Titulo" não pode estar vazio'

        if formulario['desc'] == '':
            return 'O campo "Descrição" não pode estar vazio'

        return None

    def limpar_formulario(self, formulario):
        formulario['titulo'] = ''
        formulario['desc'] = ''
