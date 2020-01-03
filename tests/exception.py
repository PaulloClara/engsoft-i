class ExceptionNoTeste(Exception):

    def __init__(self, local, erro):
        self.msg_erro = f'{local}: {erro}'

    def __str__(self):
        print(f'\n\t\033[1;33m {self.msg_erro}')

        return '\033[0;0m'
