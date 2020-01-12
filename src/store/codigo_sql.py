from src.store.infos import Infos


class CodigoSql(object):

    @staticmethod
    def select(tabela: str, _id: str='') -> str:
        colunas = ', '.join(Infos.colunas_da(tabela))
        condicao = f'{Infos.colunas_da(tabela)[0]} == "{_id}"'

        codigo_sql = f'SELECT {colunas} FROM {tabela}'

        return f'{codigo_sql} WHERE {condicao}' if _id else codigo_sql

    @staticmethod
    def insert(tabela: str, valores: list) -> str:
        colunas = ', '.join(Infos.colunas_da(tabela)[1:])
        valores = ', '.join(map(lambda valor: f'"{valor}"', valores))

        return f'INSERT INTO {tabela}({colunas}) VALUES({valores})'

    @staticmethod
    def update(tabela: str, _id: str, campos: dict) -> str:
        condicao = f'{Infos.colunas_da(tabela)[0]} == "{_id}"'
        campos = ', '.join(map(
            lambda chave: f'{chave} = "{campos[chave]}"', campos))

        return f'UPDATE {tabela} SET {campos} WHERE {condicao}'

    @staticmethod
    def delete(tabela: str, _id: str) -> str:
        condicao = f'{Infos.colunas_da(tabela)[0]} == "{_id}"'

        return f'DELETE FROM {tabela} WHERE {condicao}'
