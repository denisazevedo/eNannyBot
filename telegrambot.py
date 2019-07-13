import configparser
import logging
import audioplayer
from aiogram import Bot, Dispatcher, executor, types
from filters import RestrictUsersFilter, is_user_authorized #, restrict_users_filter

config = configparser.ConfigParser()
config.read('config/config.ini')
TOKEN = config['BOT']['TOKEN']
ALLOWED_USERS = [ el.strip() for el in config['BOT']['ALLOWED_USERS'].split(',') ]

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

# Initialize lullaby audio player
audioplayer.init()

# Register custom filter to restrict the access to message handlers
# dp.filters_factory.bind(AllowedUsersFilter)
dp.filters_factory.bind(RestrictUsersFilter, event_handlers=[dp.message_handlers])


@dp.message_handler(commands=['start'], is_restricted = False)
async def handle_start(message: types.Message):
    """ This handler will be called when client send `/start` command. """
    await message.reply(
        parse_mode = "HTML",
        text = ("Hello <b>{}</b>.\n"
            "I'm Lara electronic nanny.\n\n"
            "You can view list of my commands: /help.\n"
            "If you want to play a lullaby song for Lara: /play.\n"
            "You can stop the song at any time by sending /stop.").format(message.from_user.full_name))

@dp.message_handler(commands=['help'], is_restricted = False)
async def handle_help(message: types.Message):
    """ List the available commands when user send `/help`. """
    text = [
        "<b>Commands list:</b>\n",
        "/start - Send a list of all available commands",
        "/help - Bot help and available commands",
    ]
    if is_user_authorized(message):
        text.extend([
            "/play - Play the lullaby song",
            "/stop - Stop song",
            "/pause - Pause song",
            "/unpause - Resume playing",
        ])
    await message.reply(
        parse_mode = "HTML",
        text = '\n'.join(text))

# @dp.message_handler(lambda msg: msg.from_user.username in ALLOWED_USERS, commands = ['play'])
@dp.message_handler(commands=['play'])
async def handle_play(message: types.Message):
    """ Play the lullaby song. """
    audioplayer.start() # TODO Start it here?
    audioplayer.play()
    msg = "Playing..."
    # _keyboard = [
    #     [types.InlineKeyboardMarkup('/pause')], 
    #     [types.InlineKeyboardMarkup('/stop')],
    # ]
    # keyboard = types.InlineKeyboardMarkup(keyboard=_keyboard)
    # await message.reply(msg, reply_markup=keyboard)
    await bot.send_message(message.chat.id, msg)

@dp.message_handler(commands=['stop'])
async def handle_stop(message: types.Message):
    """ Stop the song. """
    msg = "Stopping..."
    await bot.send_message(message.chat.id, msg)
    audioplayer.stop()

@dp.message_handler(commands=['pause', 'unpause'])
async def handle_pause(message: types.Message):
    """ Pause/resume the song. """
    if message.get_command() == '/pause':
        msg = audioplayer.pause()
    elif message.get_command() == '/unpause':
        msg = audioplayer.unpause()
    await bot.send_message(message.chat.id, msg)

# @dp.message_handler(restrict_users_filter)
@dp.message_handler()
async def unknown(message: types.Message):
    """ Generic handler for unkown commands. """
    msg = "Please use a valid command (/help for available commands)."
    await bot.send_message(message.chat.id, msg)

@dp.message_handler(is_restricted = False)
async def handle(message: types.Message):
    await message.reply(
        f"Sorry {message.from_user.first_name}!\nOnly allowed users have access to this command.\n"
        "You can check the available commands here: /help")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
