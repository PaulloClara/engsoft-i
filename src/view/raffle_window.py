from src.utils.tk import TKUtils


class RaffleWindow(TKUtils.Window()):

    def __init__(self, student, activity):
        super().__init__()

        self.title('Grande Felizardo(a)')
        self.geometry(f'{len(student) * 18 + 100}x100')
        self.resizable(0, 0)

        self.student_name = student
        self.activity_title = activity

        self.container = None
        self.student_label = None
        self.activity_label = None
        self.confirm_button = None

        self._create_container()
        self._create_student_label()
        self._create_activity_label()

    def _create_container(self):
        self.container = TKUtils.get_container(master=self)

    def _create_student_label(self):
        cnf, pack = {}, {}

        cnf['text'] = f'Aluno: {self.student_name}'
        cnf['bd'] = 4
        cnf['fg'] = 'red'
        cnf['font'] = ('arial', 16, 'bold')

        self.student_label =\
            TKUtils.get_label(master=self.container, cnf=cnf, pack=pack)

    def _create_activity_label(self):
        cnf, pack = {}, {}

        cnf['text'] = f'Atividade: {self.activity_title}'
        cnf['bd'] = 4
        cnf['fg'] = 'blue'
        cnf['font'] = ('arial', 16, 'bold')

        self.activity_label =\
            TKUtils.get_label(master=self.container, cnf=cnf, pack=pack)
