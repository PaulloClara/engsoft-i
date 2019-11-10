class Navbar:

    def __init__(self, controller):
        self.__controller = controller

    def student_button(self):
        if (self.__controller.view.active_container == 'student'):
            return

        self.__controller.view.destroy_active_container()
        self.__controller.view.create_student_container()

    def activity_button(self):
        if (self.__controller.view.active_container == 'activity'):
            return

        self.__controller.view.destroy_active_container()
        self.__controller.view.create_activity_container()

    def group_button(self):
        if (self.__controller.view.active_container == 'group'):
            return

        self.__controller.view.destroy_active_container()
        self.__controller.view.create_group_container()
