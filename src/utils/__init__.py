"""Conjunto de codigo reaproveitavel."""

from random import randint
from datetime import datetime


class Utils(object):
    """Conjunto de “atalhos” para funcionalidades uteis."""

    @staticmethod
    def inteiro_aleatorio(inicio: int, fim: int) -> int:
        """Devolve um inteiro aleatorio: inicio=1 e fim=3 saida=1 ou 2 ou 3."""
        return randint(inicio, fim)

    @staticmethod
    def data_e_hora_atual() -> str:
        """Devolve uma data em string no formato: dd/mm/aaaa hh:mm."""
        return datetime.now().strftime('%d/%m/%Y %H:%M')
