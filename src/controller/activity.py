class Activity:

    def __init__(self, controller):
        self.__controller = controller

    def register_button(self):
        view = self.__controller.view.activity

        view.create_register_window()

    def submit_form_button(self):
        view = self.__controller.view.activity
        model = self.__controller.model.activity

        form = view.register_window.get_form()

        form_status = model.check_form(form=form)
        if form_status != 'ok':
            view.register_window.create_error_window(error=form_status)
            return

        model.register_activity(activity=form)
        model.reset_form(form=form)
        view.destroy_register_window()

    def cancel_form_button(self):
        view = self.__controller.view.activity
        model = self.__controller.model.activity

        form = view.register_window.get_form()

        model.reset_form(form=form)
        view.destroy_register_window()
