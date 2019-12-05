class Grupo:

    def __init__(self, controller, store):
        self.__store = store
        self.__controller = controller

        self.tabela = 'grupo'
        self.colunas = ['id_do_grupo', 'nome', 'tamanho', 'integrantes']

        self.grupos = []

        self.obter_grupos()

    def obter_grupos(self):
        codigo_sql = self.__store.select(tabela=self.tabela, colunas=self.colunas)
        self.grupos =\
            self.__store.executar(codigo_sql=codigo_sql, colunas=self.colunas)

    def cadastrar_grupo(self, grupo):
        grupo['nome'] = grupo['nome'].capitalize()
        tamanho = len(grupo['integrantes'])
        valores = [grupo['nome'], tamanho, grupo['integrantes']]

        codigo_sql =\
            self.__store.insert(
                tabela=self.tabela, colunas=self.colunas[1:], valores=valores)
        self.__store.executar(codigo_sql=codigo_sql)

        self.obter_grupos()

    def remover_grupo(self, id_do_grupo):
        condicao = f'id_do_grupo = {id_do_grupo}'
        codigo_sql = self.__store.delete(tabela=self.tabela, condicao=condicao)
        self.__store.executar(codigo_sql=codigo_sql)

        self.obter_grupos()

    def validar_campos(self, formulario):
        return 'ok'

    def limpar_formulario(self, formulario):
        formulario['nome'] = ''
        formulario['quantidade'] = ''
