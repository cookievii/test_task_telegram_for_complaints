from aiogram.types import InlineKeyboardMarkup

from core.buttons import back, set_name, set_phone


class KbSetUser:
    @staticmethod
    def get_main():
        return InlineKeyboardMarkup().add(set_name, set_phone).add(back)
