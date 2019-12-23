# Lara's Telegram Bot

This is the Telegram Bot we use for our little baby Lara.

## Configuration

Configuration file is located in `config` folder.  
Rename the file `config.ini.example` to `config.ini` and configure it.

### Telegram configuration

#### Bot name

```json
Lara's eNannyBot
```

#### Description and About

```json
An electronic nanny for our daughter Lara. It plays a lullaby as its only feature so far.
```

#### List of commands

```sh
# Generic commands
start - Send a list of all available commands
help - Bot help and available commands

# Audio player
play - Play the lullaby song
stop - Stop song
pause/unpause - Pause/resume playing
volume - Turn up/down the volume

# Camera
pic - Take a picture
```

## Usage

```shell
pip install pipenv
pipenv install
python telegrambot.py
```

## Authors

- Denis de Azevedo <denis.azevedo@gmail.com>

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
