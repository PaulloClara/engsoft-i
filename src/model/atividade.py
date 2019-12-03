class Atividade:

    def __init__(self, controller, store):
        self.__store = store
        self.__controller = controller

        self.tabela = 'atividade'
        self.colunas = ['id_da_atividade', 'titulo', 'desc']

        self.atividades = []

        self.obter_atividades()

    def obter_atividades(self):
        codigo_sql = self.__store.select(tabela=self.tabela, colunas=self.colunas)
        self.atividades =\
            self.__store.executar(codigo_sql=codigo_sql, colunas=self.colunas)

    def cadastrar_atividade(self, atividade):
        atividade['titulo'] = atividade['titulo'].capitalize()
        valores = [atividade['titulo'], atividade['desc']]

        codigo_sql =\
            self.__store.insert(
                tabela=self.tabela, colunas=self.colunas[1:], valores=valores)
        self.__store.executar(codigo_sql=codigo_sql)

        self.obter_atividades()

    def remover_atividade(self, id_da_atividade):
        condicao = f'id_da_atividade = {id_da_atividade}'
        codigo_sql = self.__store.delete(tabela=self.tabela, condicao=condicao)
        self.__store.executar(codigo_sql=codigo_sql)

        self.obter_atividades()

    def validar_campos(self, formulario):
        if formulario['titulo'] == '':
            return 'O campo "Titulo" não pode estar vazio'

        if formulario['desc'] == '':
            return 'O campo "Descrição" não pode estar vazio'

        return 'ok'

    def limpar_formulario(self, formulario):
        formulario['titulo'] = ''
        formulario['desc'] = ''
