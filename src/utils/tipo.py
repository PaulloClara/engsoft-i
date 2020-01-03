"""Submodulo de Utils."""

from sqlite3 import Cursor
from _io import TextIOWrapper


class Tipo(object):
    """Conjunto de tipos para ajudar com a tipagem estatica."""

    @staticmethod
    def arquivo() -> TextIOWrapper:
        """Tipo arquivo padrao do python: tipo=open('arquivo.txt')."""
        return TextIOWrapper

    @staticmethod
    def exc_sqlite() -> Cursor:
        """Tipo de objeto retornado apos operacoes no banco de dados."""
        return Cursor
