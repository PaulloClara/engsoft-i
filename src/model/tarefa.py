from src.utils import Utils


class Tarefa:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller

        self.tabela = 'tarefa'
        self.colunas = ['id_tarefa', 'id_atividade', 'aluno', 'data_tarefa',
                        'data_cadastro']

        self.tarefas = []

    def iniciar(self):
        self.obter_tarefas()

    def obter_tarefa(self, id_grupo_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_grupo_atividade == "{id_grupo_atividade}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_tarefas(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.tarefas = self.store.executar(codigo_sql=sql, colunas=cols)

        for tarefa in self.tarefas:
            aluno = tarefa['aluno']
            grupo = self.model.grupo.obter_grupo(aluno=aluno)

            id_atividade = tarefa['id_atividade']
            atividade =\
                self.model.atividade.obter_atividade(id_atividade=id_atividade)

            if grupo == []:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            tarefa['grupo'] = grupo[0]
            tarefa['atividade'] = atividade[0]

            nome_do_grupo = tarefa['grupo']['nome']
            titulo_da_atividade = tarefa['atividade']['titulo']
            tarefa['titulo'] = f'{nome_do_grupo} - {titulo_da_atividade}'

    def cadastrar_apresentacao(self, tarefa):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        vals.append(tarefa['id_atividade'])
        vals.append(tarefa['aluno'])
        vals.append(tarefa['duracao'])
        vals.append(tarefa['data_tarefa'])
        vals.append(Utils.obter_data_e_hora_atual())

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_tarefas()

    def remover_apresentacao(self, id_grupo_atividade):
        tab, cols = self.tabela, self.colunas
        con = f'id_grupo_atividade = {id_grupo_atividade}'

        tarefa =\
            self.obter_tarefa(id_grupo_atividade=id_grupo_atividade)[0]

        id_atividade = tarefa['id_atividade']
        self.model.atividade.atualizar_uso(id_atividade=id_atividade, valor=0)

        aluno = tarefa['aluno']
        self.model.grupo.atualizar_uso(aluno=aluno, valor=0)

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        self.obter_tarefas()

    def validar_campos(self, formulario):
        data = formulario['data_tarefa']
        duracao = formulario['duracao']

        if not data:
            return 'O campo "Apresentação" não pode estar vazio!'

        if not duracao:
            return 'O campo "Duração" não pode estar vazio!'

        if data[2] != '/' or data[5] != '/':
            return 'Formato invalido! Entre com o formato dd/mm/aaaa'

        dia, mes, ano = data.split('/')

        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except Exception as e:
            return 'Os valores em dd, mm e aaaa precisam ser numeros!'

        data_valida = False

        meses_com_ate_31_dias = [1, 3, 5, 7, 8, 10, 12]
        if mes in meses_com_ate_31_dias:
            if dia <= 31:
                data_valida = True

        meses_com_ate_30_dias = [4, 6, 9, 11]
        if mes in meses_com_ate_30_dias:
            if dia <= 30:
                data_valida = True

        if mes == 2:
            if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
                # Ano Bisexto! Fevereiro com possíveis 29 dias
                if dia <= 29:
                    data_valida = True

            if dia <= 28:
                data_valida = True

        if not data_valida:
            return 'Data INVALIDA!'

        try:
            duracao = int(duracao)
        except Exception as e:
            return 'O campo "Duração" só aceita valor inteiro!'

        if duracao < 5:
            return 'O tempo mínimo da apresentação é 5 min!'

        if duracao > 60:
            return 'Duração máxima de cada apresentação é 60 min!'

        return None
