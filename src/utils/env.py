from sys import argv


class Env(object):

    @staticmethod
    def parametros() -> list:
        return argv

    @staticmethod
    def modo_dev() -> bool:
        return True if '--dev' in Env.parametros() else False

    @staticmethod
    def modo_teste() -> bool:
        return True if '--test' in Env.parametros() else False

    @staticmethod
    def modo_producao() -> bool:
        return True if not Env.modo_dev() and not Env.modo_teste() else False
