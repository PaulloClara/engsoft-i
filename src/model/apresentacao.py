class Apresentacao:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller

        self.tabela = 'apresentacao'
        self.colunas = ['id_da_apresentacao', 'id_da_atividade', 'id_do_grupo',
                        'data_de_apresentacao', 'data_de_cadastro', 'duracao']

        self.apresentacoes = []

        self.obter_apresentacoes()

    def cadastrar_apresetacao(self, evento):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

    def obter_apresentacao(self, id_da_apresentacao):
        tab, cols = self.tabela, self.colunas
        con = f'id_da_apresentacao == "{id_da_apresentacao}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_apresentacoes(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.apresentacoes = self.store.executar(codigo_sql=sql, colunas=cols)

        for apresentacao in self.apresentacoes:
            id_do_grupo = apresentacao['id_do_grupo']
            grupo = self.model.grupo.obter_grupo(id_do_grupo=id_do_grupo)

            id_da_atv = apresentacao['id_da_atividade']
            atividade =\
                self.model.atividade.obter_atividade(id_da_atividade=id_da_atv)

            if grupo == []:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            apresentacao['grupo'] = grupo[0]
            apresentacao['atividade'] = atividade[0]

            nome_do_grupo = apresentacao['grupo']['nome']
            titulo_da_atividade = apresentacao['atividade']['titulo']
            apresentacao['titulo'] = f'{nome_do_grupo} - {titulo_da_atividade}'
