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
        codigo_sql =\
            self.store.insert(
                tabela=self.tabela, colunas=self.colunas[1:], valores=valores)
        self.store.executar(codigo_sql=codigo_sql)

    def obter_apresentacoes(self):
        codigo_sql = self.store.select(tabela=self.tabela, colunas=self.colunas)
        self.apresentacoes =\
            self.store.executar(codigo_sql=codigo_sql, colunas=self.colunas)

        for apr in self.apresentacoes:
            grupo = self.model.grupo.obter_grupo(id_do_grupo=apr['id_do_grupo'])
            atividade =\
                self.model.atividade.obter_atividade(id_da_atividade=apr['id_da_atividade'])

            if grupo == []:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            apr['grupo'] = grupo[0]
            apr['atividade'] = atividade[0]

            apr['titulo'] = f'{apr["grupo"]["nome"]} - {apr["atividade"]["titulo"]}'
