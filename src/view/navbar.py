from src.utils.tk import TKUtils


class Navbar(TKUtils.Container()):

    def __init__(self, master, commands):
        super().__init__(master=master)
        self.pack()

        self.commands = commands

        self.group_button = None
        self.student_button = None
        self.activity_button = None

        self.create_student_button()
        self.create_activity_button()
        self.create_group_button()

    def create_student_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Alunos'
        cnf['bg'] = 'red'
        cnf['width'] = 14
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.commands['student']

        pack['side'] = 'left'

        self.student_button =\
            TKUtils.get_button(master=self, cnf=cnf, pack=pack)

    def create_activity_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Atividades'
        cnf['bg'] = 'blue'
        cnf['width'] = 24
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.commands['activity']

        pack['side'] = 'left'

        self.activity_button =\
            TKUtils.get_button(master=self, cnf=cnf, pack=pack)

    def create_group_button(self):
        cnf, pack = {}, {}

        cnf['text'] = 'Grupos'
        cnf['bg'] = 'green'
        cnf['width'] = 14
        cnf['font'] = ('arial', 16, 'bold')
        cnf['command'] = self.commands['group']

        pack['side'] = 'left'

        self.group_button = TKUtils.get_button(master=self, cnf=cnf, pack=pack)
