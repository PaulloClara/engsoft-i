"""Conjunto de codigo reaproveitavel."""

from random import randint
from datetime import datetime, timedelta


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

    @staticmethod
    def data_e_hora_em_(dias: int) -> str:
        """Devolve uma data em string no formato: dd/mm/aaaa hh:mm + dd."""
        data_e_hora = datetime.now() + timedelta(days=dias)

        return data_e_hora.strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def comparar_(data1: str, data2: str) -> bool or None:
        data1 = ''.join(data1.split('/')[::-1])
        data2 = ''.join(data2.split('/')[::-1])

        if data1 > data2:
            return True
        if data1 < data2:
            return False
