from src.utils import Utils


class Modelo(object):

    def __init__(self):
        pass

    def iniciar(self, model):
        self.model = model
        self.store = self.model.store

    def sortear(self, lista: list) -> dict or str or None:
        if isinstance(lista[0], dict):
            lista = list(filter(lambda valor: not valor['em_uso'], lista))

        if not lista:
            return None

        index = Utils.inteiro_aleatorio(inicio=0, fim=len(lista) - 1)

        return lista[index]

    def obter(self, _id):
        sql = self.store.sql.select(self.tabela, _id)
        resultado = self.store.executar(sql)

        return resultado[0] if resultado else None

    def carregar(self):
        sql = self.store.sql.select(self.tabela)

        return self.store.executar(sql)

    def cadastrar(self, vals):
        sql = self.store.sql.insert(self.tabela, valores=vals)
        self.store.executar(sql)

    def atualizar(self, _id, campos):
        sql = self.store.sql.update(self.tabela, _id, campos)
        self.store.executar(sql)

    def remover(self, _id, tipo):
        sql = self.store.sql.delete(self.tabela, _id)
        self.store.executar(sql)

        lista = getattr(self, tipo)
        for i, elemento in enumerate(lista):
            if elemento['_id'] == _id:
                del lista[i]
                break

    def validar_campos(self, formulario):
        for campo in formulario:
            if not formulario[campo]:
                return f'O campo "{campo}" não pode estar vazio!'

    def validar_data(self, data):
        if data[2] != '/' or data[5] != '/':
            return 'Formato invalido! Entre com o formato dd/mm/aaaa'

        dia, mes, ano = data.split('/')
        data_atual = Utils.data_e_hora_atual().split(' ')[0].split('/')

        try:
            dia, mes, ano = int(dia), int(mes), int(ano)
        except Exception as e:
            return 'Os valores em dd, mm e aaaa precisam ser numeros!'

        data_valida = False

        if data_atual[::-1] > data.split('/')[::-1]:
            return 'Data INVALIDA'

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
