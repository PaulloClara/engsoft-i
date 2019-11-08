class Activity:

    def __init__(self, controller):
        self.__controller = controller

    def register_button(self):
        view = self.__controller.view.activity

        view.create_register_window()

    def submit_form_button(self):
        pass

    def cancel_form_button(self):
        pass
