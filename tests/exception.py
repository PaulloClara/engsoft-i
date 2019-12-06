class ExceptionNoTeste(Exception):

    def __init__(self, local, erro):
        self.erro_msg = f'{local}: {erro}'

    def __str__(self):
        return self.erro_msg
