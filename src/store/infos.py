"""."""


class Infos(object):
    """."""

    @staticmethod
    def tabelas() -> list:
        """."""
        return 'atividade', 'grupo', 'apresentacao', 'tarefa', 'evento'

    @staticmethod
    def colunas_da(tabela: str) -> list:
        """."""
        return getattr(Infos, f'colunas_{tabela}')()

    @staticmethod
    def colunas_atividade() -> list:
        """."""
        return '_id', 'titulo', 'descricao', 'em_uso', 'cadastro'

    @staticmethod
    def colunas_grupo() -> list:
        """."""
        return '_id', 'nome', 'integrantes', 'em_uso', 'cadastro'

    @staticmethod
    def colunas_tarefa() -> list:
        """."""
        return '_id', 'id_atividade', 'aluno', 'duracao', 'data', 'cadastro'

    @staticmethod
    def colunas_apresentacao() -> list:
        """."""
        return '_id', 'id_atividade', 'id_grupo', 'duracao', 'data', 'cadastro'

    @staticmethod
    def colunas_evento() -> list:
        """."""
        return '_id', 'titulo', 'duracao', 'data', 'cadastro'

    @staticmethod
    def colunas_sobre() -> list:
        """."""
        return []
