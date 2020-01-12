from tkinter import Event
from sqlite3 import Cursor
from _io import TextIOWrapper


class Tipo(object):

    @staticmethod
    def arquivo() -> TextIOWrapper:
        return TextIOWrapper

    @staticmethod
    def evento_tk() -> Event:
        return Event

    @staticmethod
    def elemento_tk() -> object:
        return object

    @staticmethod
    def exc_sqlite() -> Cursor:
        return Cursor
