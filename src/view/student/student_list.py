from src.utils.tk import UI


class StudentList(UI.ScrollFrame):

    def __init__(self, master):
        configs, canvas_cnf, viewport_cnf, scrollbar_cnf = {}, {}, {}, {}

        configs['bd'] = 2
        configs['bg'] = 'grey'
        configs['relief'] = 'flat'

        canvas_cnf['width'] = 1200
        canvas_cnf['height'] = 520

        scrollbar_cnf['bd'] = 4
        scrollbar_cnf['relief'] = 'flat'
        scrollbar_cnf['bg'] = 'grey'

        super().__init__(
            master=master,
            cnf=configs,
            cs_cnf=canvas_cnf,
            vt_cnf=viewport_cnf,
            sr_cnf=scrollbar_cnf)
        self.pack(expand=True)

        self.label_list = []

        for i in range(10):
            self.create_student_label(student_name='Paulo Ricardo da Silva C.')
            self.create_student_label(student_name='Josivan Cabra Macho')
            self.create_student_label(student_name='Wesley Weslei Weslley')

    def create_student_label(self, student_name):
        # Container
        configs, pack = {}, {}

        configs['bd'] = 4
        configs['bg'] = 'green'
        configs['relief'] = 'ridge'

        label_container = UI.get_container(
            master=self.viewport, cnf=configs, pack=pack)

        # Label
        configs, pack = {}, {}

        configs['text'] = student_name
        configs['bg'] = 'blue'
        configs['fg'] = 'white'
        configs['width'] = 124
        configs['height'] = 2

        pack['side'] = 'left'

        label_container.label = UI.get_label(
            master=label_container, cnf=configs, pack=pack)

        # Button
        configs, pack = {}, {}

        configs['text'] = 'X'
        configs['bg'] = 'red'
        configs['relief'] = 'ridge'
        configs['width'] = 3

        pack['side'] = 'right'

        label_container.button = UI.get_button(
            master=label_container, cnf=configs, pack=pack)

        self.label_list.append(label_container)
