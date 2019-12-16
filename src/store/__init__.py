import sqlite3
from src.utils import Utils


class Store:

    def __init__(self):
        self.conexao = None
        self.conectado = False
        self.caminho = Utils.obter_caminho('src/store/banco_de_dados.sqlite')

    def obter_arquivo(self, caminho, modo):
        return open(Utils.obter_caminho(caminho), mode=modo)

    def executar(self, codigo_sql, converter=True, colunas=[]):
        if self.conectado:
            self.fechar_conexao()

        self.conexao = self.conectar()

        resultado = self.conexao.cursor().execute(codigo_sql)

        if 'SELECT' in codigo_sql and converter:
            resultado = self.converter(tabela=resultado, colunas=colunas)

        self.salvar()

        return resultado

    def salvar(self, fechar_conexao=True):
        if not self.conectado:
            return

        self.conexao.commit()

        if fechar_conexao:
            self.fechar_conexao()

    def fechar_conexao(self):
        if not self.conectado:
            return

        self.conexao.close()
        self.conectado = False

    def conectar(self):
        self.conectado = True

        return sqlite3.connect(self.caminho)

    def converter(self, tabela, colunas):
        resultado, resultado_parcial = [], {}

        for linha in tabela:
            for i, valor in enumerate(linha):
                resultado_parcial[colunas[i]] = valor

            resultado.append(resultado_parcial)
            resultado_parcial = {}

        return resultado

    def select(self, tabela, colunas, condicao=None):
        colunas = ', '.join(colunas)

        codigo = f'SELECT {colunas} FROM {tabela}'

        if condicao:
            codigo = f'{codigo} WHERE {condicao}'

        return codigo

    def insert(self, tabela, colunas, valores):
        valores = map(lambda valor: f'"{valor}"', valores)
        valores = ', '.join(valores)
        colunas = ', '.join(colunas)

        return f'INSERT INTO {tabela}({colunas}) VALUES({valores})'

    def update(self, tabela, campos, condicao):
        return f'UPDATE {tabela} SET {campos} WHERE {condicao}'

    def delete(self, tabela, condicao):
        return f'DELETE FROM {tabela} WHERE {condicao}'
