"""."""

from src.store.sqlite import MSqLite

from src.utils.tipo import Tipo
from src.utils.caminho import Caminho


class Store(MSqLite):
    """."""

    def __init__(self) -> None:
        """."""
        super().__init__()

    def arquivo(self, arquivo: str, modo: str='r') -> Tipo.arquivo:
        """."""
        return open(arquivo, mode=modo)

    def executar(self, codigo_sql: str) -> list or None:
        """."""
        resultado = super().executar(codigo_sql)

        if 'SELECT' in codigo_sql:
            return self.converter(cursor=resultado)

    def converter(self, cursor: Tipo.exc_sqlite) -> list:
        """."""
        tabela = cursor.fetchall()
        colunas = [linha[0] for linha in cursor.description]

        nova_tabela, nova_linha = [], {}

        for linha in tabela:
            for i, valor in enumerate(linha):
                nova_linha[colunas[i]] = valor

            nova_tabela.append(nova_linha)
            nova_linha = {}

        return nova_tabela
