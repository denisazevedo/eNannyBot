import configparser
import logging
from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

config = configparser.ConfigParser()
config.read('config/config.ini')
ALLOWED_USERS = [el.strip() for el in config['BOT']['ALLOWED_USERS'].split(',')]


def is_user_authorized(message: types.Message) -> bool:
    return message.from_user.username in ALLOWED_USERS

# async def restrict_users_filter(message: types.Message):
#     valid = message.from_user.username in ALLOWED_USERS
#     print(f"Filter function -> {message.from_user.username}, valid: {valid}")
#     return valid


class RestrictUsersFilter(BoundFilter):
    """
    Restrict all the message handlers (unless `is_restricted` was set to `false`)
    to allow only the Telegram usernames provided in config.ini.
    """

    key = 'is_restricted'
    required = True # Required for all message handlers

    def __init__(self, is_restricted: bool):
        if is_restricted == None:
            is_restricted = True
        self.is_restricted = is_restricted

    async def check(self, message: types.Message) -> bool:
        valid = (not self.is_restricted) or (message.from_user.username in ALLOWED_USERS)
        logging.debug(f"Filter: is_restricted={self.is_restricted} -> {message.from_user.username}, valid: {valid}")
        return valid
