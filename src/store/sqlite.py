from src import BANCO_DE_DADOS
import sqlite3

from src.store.infos import Infos
from src.store.codigo_sql import CodigoSql

from src.utils.tipo import Tipo


class MSqLite(object):

    def __init__(self) -> None:
        self.sql = CodigoSql

        self.conexao = None
        self.conectado = False

    def executar(self, codigo_sql: str) -> Tipo.exc_sqlite:
        if self.conectado:
            self.fechar_conexao()

        self.conectar()
        resultado = self.conexao.cursor().execute(codigo_sql)

        self.salvar(fechar_conexao=False)

        return resultado

    def salvar(self, fechar_conexao: bool=True) -> None:
        if not self.conectado:
            return

        self.conexao.commit()

        if fechar_conexao:
            self.fechar_conexao()

    def fechar_conexao(self) -> None:
        if not self.conectado:
            return

        self.conexao.close()
        self.conectado = False

    def conectar(self) -> None:
        self.conexao = sqlite3.connect(BANCO_DE_DADOS)
        self.conectado = True
