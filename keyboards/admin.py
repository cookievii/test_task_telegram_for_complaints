from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from core.buttons import back_admin, permission, search_user, spam_msg


class KbAdmin:
    """Клавиатура и инлайн-кнопки администраторов."""

    @staticmethod
    def get_main():
        """Возвращает клавиатуру главного меню."""
        return ReplyKeyboardMarkup(
            keyboard=[[search_user], [spam_msg], [permission]],
            resize_keyboard=True,
            one_time_keyboard=True,
        )

    @staticmethod
    def get_back_and_permission():
        """Возвращает инлайн-кнопки "забанить/разбанить" и "назад"."""
        return InlineKeyboardMarkup().add(permission).add(back_admin)

    @staticmethod
    def get_back():
        """Возвращает инлайн-кнопку "назад"."""
        return InlineKeyboardMarkup().add(back_admin)
