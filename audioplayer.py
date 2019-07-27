#!/usr/bin/env python3

import configparser
import logging
import pygame

# TODO Convert to a Class???

config = configparser.ConfigParser()
config.read('./config/config.ini')
AUDIO_PATH = config['AUDIO']['FILE_PATH']
LOOPS = int(config['AUDIO']['LOOPS'])

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


def init():
    pygame.mixer.pre_init()
    pygame.mixer.init()
    # BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    # pygame.mixer.init(buffer=BUFFER)
    pygame.mixer.music.set_volume(0.7)


def start():
    logging.info(f"Loading audio file {AUDIO_PATH}...")
    pygame.mixer.music.load(AUDIO_PATH)


def play(busy=False):
    logging.info("Playing...")
    pygame.mixer.music.play(loops=LOOPS)
    if busy:
        while pygame.mixer.music.get_busy() is True:
            continue


def stop():
    logging.info("Stopping...")
    pygame.mixer.music.stop()


def pause():
    res = f"Pausing at {_get_current_time_position()}..."
    logging.debug(res)
    pygame.mixer.music.pause()
    return res


def unpause():
    res = f"Resuming at {_get_current_time_position()}..."
    logging.debug(res)
    pygame.mixer.music.unpause()
    return res


def quit_player():
    logging.info("Good bye!")
    pygame.quit()


# TODO implement get status function
def get_status() -> str:
    # TODO check if it is playing
    # if is_playing:
    # TODO get current position
    pos = pygame.mixer.music.get_pos()
    time = _convert_millis_to_human_time(pos)
    # TODO get volume
    # TODO get song name
    res = time  # FIXME
    return res


# TODO
def volume_up():
    v = pygame.mixer.music.get_volume()
    v = 1 if v > 0.9 else v+0.1
    pygame.mixer.music.set_volume(v)


# TODO
def volume_down():
    v = pygame.mixer.music.get_volume()
    v = 0 if v < 0.1 else v-0.1
    pygame.mixer.music.set_volume(v)


def _get_current_time_position() -> str:
    pos = pygame.mixer.music.get_pos()
    time = _convert_millis_to_human_time(pos)
    return time


def _convert_millis_to_human_time(ms: int) -> str:
    """ Convert milliseconds to the human readable format: hh:mm:ss. """
    seconds = (ms / 1000) % 60
    minutes = (ms / (1000 * 60)) % 60
    hours = (ms / (1000 * 60 * 60)) % 24
    # return int(hours), int(minutes), int(seconds)
    time = "{0:02d}:{1:02d}:{2:02d}".format(int(hours), int(minutes), int(seconds))
    return time


# clock = pygame.time.Clock()
# while pygame.mixer.music.get_busy():
#     clock.tick(1000)

if __name__ == '__main__':
    logging.info("Starting AudioPlayer...")
    init()
    start()
    play()
    while pygame.mixer.music.get_busy() is True:
        continue
    quit()
