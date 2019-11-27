from sys import argv
from os import getcwd
from random import randint


class Utils:

    @staticmethod
    def get_random_int(start, end):
        return randint(start, end)

    @staticmethod
    def get_current_path():
        return getcwd()

    @staticmethod
    def get_full_path(file_path):
        full_path = f'{Utils.get_current_path()}/{Utils.get_run_path()}'

        if Utils.check_prodmode():
            full_path = f'{full_path}/lib'

        full_path = f'{full_path}/{file_path}'

        return full_path

    @staticmethod
    def get_args():
        return argv

    @staticmethod
    def get_run_path():
        return '/'.join(argv[0].split('/')[:-1])

    @staticmethod
    def check_devmode():
        if '--dev' in argv:
            return True
        return False

    @staticmethod
    def check_testmode():
        if '--test' in argv:
            return True
        return False

    @staticmethod
    def check_prodmode():
        if not Utils.check_devmode() and not Utils.check_testmode():
            return True
        return False
