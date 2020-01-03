"""Submodulo de Utils."""

from sys import argv


class Env(object):
    """Conjunto de informacoes relacionadas a execucao."""

    @staticmethod
    def parametros() -> list:
        """Retorna os parametros recebidos no momento da execucao."""
        return argv

    @staticmethod
    def modo_dev() -> bool:
        """Verifica se o app foi executado em modo de desenvolvimento."""
        return True if '--dev' in Env.parametros() else False

    @staticmethod
    def modo_teste() -> bool:
        """Verifica se o app foi executado em modo de testes."""
        return True if '--test' in Env.parametros() else False

    @staticmethod
    def modo_producao() -> bool:
        """Verifica se o app foi executado em modo de producao."""
        return True if not Env.modo_dev() and not Env.modo_teste() else False
