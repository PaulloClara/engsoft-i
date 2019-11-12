class Activity:

    def __init__(self, controller):
        self.__controller = controller

    def raffle_button(self):
        view = self.__controller.view.activity

    def register_button(self):
        view = self.__controller.view.activity

        if not view.register_window:
            view.create_register_window()

    def remove_activity_button(self, activity_id):
        view = self.__controller.view.activity
        model = self.__controller.model.activity

        model.remove_activity(activity_id=activity_id)

        view.destroy_activities_list()
        self.load_activities_list()

    def raffle_activity_button(self):
        pass

    def submit_form_button(self):
        view = self.__controller.view.activity
        model = self.__controller.model.activity

        form = view.register_window.get_form()

        form_status = model.check_form(form=form)
        if form_status != 'ok':
            self.__controller.view.create_error_window(error=form_status)
            return

        model.register_activity(activity=form)
        view.destroy_register_window()

        view.destroy_activities_list()
        self.load_activities_list()

    def cancel_form_button(self):
        view = self.__controller.view.activity
        view.destroy_register_window()

    def load_activities_list(self):
        view = self.__controller.view.activity
        model = self.__controller.model.activity

        for activity in model.activities:
            view.activities_list.create_activity_label(activity=activity)

    def mounted(self):
        self.load_activities_list()
