class Cadastro(object):

    def __init__(self):
        pass

    def confirmar(self, evt=None):
        formulario = self.view.home.cadastro_tarefa.obter_campos()

        erro = self.model.tarefa.validar(formulario)
        if erro:
            return self.view.janela_erro.iniciar(erro)

        erro = 'Todas as atividades já estão em uso'
        atividade = self.model.atividade.sortear()
        if not atividade:
            return self.view.janela_erro.iniciar(erro)

        erro = 'Lista de alunos vazia'
        aluno = self.model.aluno.sortear()
        if not aluno:
            return self.view.janela_erro.iniciar(erro)

        id_atividade = atividade['id_atividade']

        formulario['aluno'] = aluno
        formulario['id_atividade'] = id_atividade

        tarefa = self.model.tarefa.cadastrar(formulario)

        elemento = self.view.home.listagem.adicionar(tarefa=tarefa)
        self.configurar_(elemento)

        self.model.atividade.atualizar(id_atividade, campos={'em_uso': 1})
        self.view.atividade.listagem.desativar(id_atividade)

        self.view.home.cadastro_tarefa.fechar()

    def cancelar(self, evt=None):
        self.view.home.cadastro_tarefa.fechar()

    def configurar(self):
        tarefa = self.view.home.cadastro_tarefa.subelemento

        tarefa.data.input.evento['<Return>'] = self.confirmar
        tarefa.duracao.input.evento['<Return>'] = self.confirmar

        tarefa.cancelar.defs.mcnf['command'] = self.cancelar
        tarefa.confirmar.defs.mcnf['command'] = self.confirmar

        self.view.home.cadastro_tarefa.carregar_eventos()
