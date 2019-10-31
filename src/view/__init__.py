from src.utils.tk import UI

from src.view.navbar import Navbar


class View(UI.Window):

    def __init__(self, controller):
        super().__init__()

        self.__controller = controller

        self.title('EngSoft')
        self.geometry('800x600')

        self.navbar = None

    def start(self):
        self.create_navbar()

        self.mainloop()

    def create_navbar(self):
        self.navbar = Navbar(master=self)

        click_student_button = self.__controller.navbar.student_button
        click_activity_button = self.__controller.navbar.activity_button
        click_group_button = self.__controller.navbar.group_button

        self.navbar.student_button.configure(command=click_student_button)
        self.navbar.activity_button.configure(command=click_activity_button)
        self.navbar.group_button.configure(command=click_group_button)
