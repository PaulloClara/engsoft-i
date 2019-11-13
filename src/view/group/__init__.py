from src.utils.tk import TKUtils


class Group(TKUtils.Container()):

    def __init__(self, master):
        super().__init__(master=master)
        self.pack()

        label_temp = TKUtils.get_label(master=self, cnf={'text': 'Grupos'})
