from random import randint
from datetime import datetime, timedelta


class Utils(object):

    @staticmethod
    def inteiro_aleatorio(inicio: int, fim: int) -> int:
        return randint(inicio, fim)

    @staticmethod
    def data_e_hora_atual() -> str:
        return datetime.now().strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def data_e_hora_em_(dias: int) -> str:
        data_e_hora = datetime.now() + timedelta(days=dias)

        return data_e_hora.strftime('%d/%m/%Y %H:%M')

    @staticmethod
    def comparar_(data1: str, data2: str) -> bool or None:
        data1 = ''.join(data1.split('/')[::-1])
        data2 = ''.join(data2.split('/')[::-1])

        return 1 if data1 > data2 else -1 if data1 < data2 else 0
