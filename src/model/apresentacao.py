from src.utils import Utils


class Apresentacao:

    def __init__(self, model):
        self.model = model
        self.store = self.model.store
        self.controller = self.model.controller

        self.tabela = 'apresentacao'
        self.colunas = ['id_apresentacao', 'id_atividade', 'id_grupo',
                        'duracao', 'data_apresentacao', 'data_cadastro']

        self.apresentacoes = []

    def iniciar(self):
        self.obter_apresentacoes()
        self.ordenar()

    def obter_apresentacao(self, id_apresentacao):
        tab, cols = self.tabela, self.colunas
        con = f'id_apresentacao == "{id_apresentacao}"'

        sql = self.store.select(tabela=tab, colunas=cols, condicao=con)

        return self.store.executar(codigo_sql=sql, colunas=cols)

    def obter_apresentacoes(self):
        tab, cols = self.tabela, self.colunas

        sql = self.store.select(tabela=tab, colunas=cols)
        self.apresentacoes = self.store.executar(codigo_sql=sql, colunas=cols)

        for apresentacao in self.apresentacoes:
            id_grupo = apresentacao['id_grupo']
            grupo = self.model.grupo.obter_grupo(id_grupo=id_grupo)

            id_atividade = apresentacao['id_atividade']
            atividade =\
                self.model.atividade.obter_atividade(id_atividade=id_atividade)

            if grupo == []:
                grupo = [{'nome': 'GRUPO DELETADO'}]
            if atividade == []:
                atividade = [{'titulo': 'ATIVIDADE DELETADA'}]

            apresentacao['grupo'] = grupo[0]
            apresentacao['atividade'] = atividade[0]

            nome_do_grupo = apresentacao['grupo']['nome']
            titulo_da_atividade = apresentacao['atividade']['titulo']
            apresentacao['titulo'] = f'{nome_do_grupo} - {titulo_da_atividade}'

    def cadastrar_apresentacao(self, apresentacao):
        tab, cols, vals = self.tabela, self.colunas[1:], []

        vals.append(apresentacao['id_atividade'])
        vals.append(apresentacao['id_grupo'])
        vals.append(apresentacao['duracao'])
        vals.append(apresentacao['data_apresentacao'])
        vals.append(Utils.obter_data_e_hora_atual())

        sql = self.store.insert(tabela=tab, colunas=cols, valores=vals)
        self.store.executar(codigo_sql=sql)

        self.obter_apresentacoes()

    def remover_apresentacao(self, id_apr):
        tab, cols = self.tabela, self.colunas
        con = f'id_apresentacao = {id_apr}'

        apresentacao = self.obter_apresentacao(id_apresentacao=id_apr)[0]

        id_atividade = apresentacao['id_atividade']
        self.model.atividade.atualizar_uso(id_atividade=id_atividade, valor=0)

        id_grupo = apresentacao['id_grupo']
        self.model.grupo.atualizar_uso(id_grupo=id_grupo, valor=0)

        sql = self.store.delete(tabela=tab, condicao=con)
        self.store.executar(codigo_sql=sql)

        for i, apresentacao in enumerate(self.apresentacoes):
            if apresentacao['id_apresentacao'] == id_apr:
                del self.apresentacoes[i]

        return id_atividade, id_grupo

    def ordenar(self):
        self.apresentacoes.sort(
            key=lambda a: a['data_apresentacao'].split('/')[::-1])

    def validar_cadastro(self, formulario):
        data = formulario['data_apresentacao']
        duracao = formulario['duracao']

        if not self.model.atividade.atividades:
            return 'Lista de Atividades vazia'

        if not self.model.grupo.grupos:
            return 'Lista de Grupos vazia'

        if not data:
            return 'O campo "Apresentação" não pode estar vazio!'

        if not duracao:
            return 'O campo "Duração" não pode estar vazio!'

        if data[2] != '/' or data[5] != '/':
            return 'Formato invalido! Entre com o formato dd/mm/aaaa'

        dia, mes, ano = data.split('/')

        data_atual = Utils.obter_data_e_hora_atual().split(' ')[0].split('/')

        erro = 'Data INVALIDA'
        if data_atual[2] > ano:
            return erro
        elif data_atual[2] == ano and data_atual[1] > mes:
            return erro
        elif data_atual[2] == ano and data_atual[1] == mes and data_atual[0] > dia:
            return erro

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
