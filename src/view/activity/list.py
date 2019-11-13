from src.utils.tk import TKUtils


class ActivitiesList(TKUtils.ScrollFrame()):

    def __init__(self, master, commands):
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

        self.commands = commands
        self.label_list = []

    def create_activity_label(self, activity):
        # Container
        cnf, pack = {}, {}

        cnf['bd'] = 4
        cnf['bg'] = 'green'
        cnf['relief'] = 'ridge'

        label_container =\
            TKUtils.get_container(master=self.viewport, cnf=cnf, pack=pack)

        # Label
        cnf, pack = {}, {}

        cnf['text'] = activity['title']
        cnf['bg'] = 'blue'
        cnf['fg'] = 'white'
        cnf['width'] = 120
        cnf['height'] = 2

        pack['side'] = 'left'

        label_container.label =\
            TKUtils.get_label(master=label_container, cnf=cnf, pack=pack)

        # Raffle Button
        cnf, pack, defs = {}, {}, {}

        defs['type'] = 'activity'
        defs['value'] = activity

        cnf['text'] = 'O'
        cnf['bg'] = 'orange'
        cnf['width'] = 2
        cnf['command'] = lambda evt=None: self.commands['raffle'](defs=defs)

        pack['side'] = 'left'

        label_container.button =\
            TKUtils.get_button(master=label_container, cnf=cnf, pack=pack)

        # Remove Button
        cnf, pack = {}, {}

        cnf['text'] = 'X'
        cnf['bg'] = 'red'
        cnf['width'] = 2

        pack['side'] = 'right'

        label_container.button =\
            TKUtils.get_button(master=label_container, cnf=cnf, pack=pack)

        activity_id = activity['activity_id']
        label_container.button.bind(
            "<Button-1>", lambda a: self.commands['remove'](activity_id))

        self.label_list.append(label_container)
