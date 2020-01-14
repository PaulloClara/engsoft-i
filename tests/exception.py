class ExceptionNoTeste(Exception):

    def __init__(self, local: str, erro: str) -> None:
        self.msg_erro = f'{local}: {erro}'

    def __str__(self) -> str:
        return f'\n\t\033[1;33m {self.msg_erro}\033[0;0m'
