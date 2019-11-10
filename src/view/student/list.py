from src.utils.tk import UI


class StudentList(UI.ScrollFrame):

    def __init__(self, master):
        cnf, canvas_cnf, viewport_cnf, scrollbar_cnf = {}, {}, {}, {}

        cnf['bd'] = 2
        cnf['bg'] = 'grey'
        cnf['relief'] = 'flat'

        canvas_cnf['width'] = 1200
        canvas_cnf['height'] = 460

        scrollbar_cnf['bd'] = 4
        scrollbar_cnf['bg'] = 'grey'
        scrollbar_cnf['relief'] = 'flat'

        super().__init__(master=master, cnf=cnf, cs_cnf=canvas_cnf,
                         vt_cnf=viewport_cnf, sr_cnf=scrollbar_cnf)
        self.pack(expand=True)

        self.label_list = []

        for i in range(10):
            self.create_student_label(student_name='Paulo Ricardo da Silva C.')
            self.create_student_label(student_name='Josivan Cabra Macho')
            self.create_student_label(student_name='Wesley Weslei Weslley')

    def create_student_label(self, student_name):
        # Container
        cnf, pack = {}, {}

        cnf['bd'] = 4
        cnf['bg'] = 'green'
        cnf['relief'] = 'ridge'

        label_container =\
            UI.get_container(master=self.viewport, cnf=cnf, pack=pack)

        # Label
        cnf, pack = {}, {}

        cnf['text'] = student_name
        cnf['bg'] = 'red'
        cnf['fg'] = 'white'
        cnf['width'] = 124
        cnf['height'] = 2

        pack['side'] = 'left'

        label_container.label =\
            UI.get_label(master=label_container, cnf=cnf, pack=pack)

        # Raffle Button
        cnf, pack = {}, {}

        cnf['text'] = 'O'
        cnf['bg'] = 'orange'
        cnf['width'] = 2

        pack['side'] = 'right'

        label_container.button =\
            UI.get_button(master=label_container, cnf=cnf, pack=pack)

        self.label_list.append(label_container)
