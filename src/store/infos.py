"""."""


class Infos(object):
    """."""

    @staticmethod
    def tabelas() -> list:
        """."""
        return ['atividade', 'grupo', 'apresentacao', 'tarefa', 'evento']

    @staticmethod
    def colunas_da(tabela: str) -> list:
        """."""
        return getattr(Infos, f'colunas_{tabela}')()

    @staticmethod
    def colunas_atividade() -> list:
        """."""
        return ['id_atividade', 'titulo', 'descricao', 'em_uso',
                'data_cadastro']

    @staticmethod
    def colunas_grupo() -> list:
        """."""
        return ['id_grupo', 'nome', 'integrantes', 'em_uso', 'data_cadastro']

    @staticmethod
    def colunas_tarefa() -> list:
        """."""
        return ['id_tarefa', 'id_atividade', 'aluno', 'duracao', 'data_tarefa',
                'data_cadastro']

    @staticmethod
    def colunas_apresentacao() -> list:
        """."""
        return ['id_apresentacao', 'id_atividade', 'id_grupo', 'duracao',
                'data_apresentacao', 'data_cadastro']

    @staticmethod
    def colunas_evento() -> list:
        """."""
        return []

    @staticmethod
    def colunas_sobre() -> list:
        """."""
        return []
