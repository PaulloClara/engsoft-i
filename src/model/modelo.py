from src.utils import Utils


class Modelo(object):

    def __init__(self):
        pass

    def iniciar(self, model):
        self.model = model
        self.store = self.model.store

    def sortear(self, lista: list) -> dict or str or None:
        if isinstance(lista[0], dict):
            lista = list(filter(lambda valor: not valor['em_uso'], lista))

        if not lista:
            return None

        index = Utils.inteiro_aleatorio(inicio=0, fim=len(lista) - 1)

        return lista[index]

    def obter(self, _id):
        sql = self.store.sql.select(self.tabela, _id)

        return self.store.executar(sql)

    def carregar(self):
        sql = self.store.sql.select(self.tabela)

        return self.store.executar(sql)

    def cadastrar(self, vals):
        sql = self.store.sql.insert(self.tabela, valores=vals)
        self.store.executar(sql)

    def atualizar(self, _id, campos):
        sql = self.store.sql.update(self.tabela, _id, campos)
        self.store.executar(sql)

    def remover(self, _id):
        sql = self.store.sql.delete(self.tabela, _id)
        self.store.executar(sql)
