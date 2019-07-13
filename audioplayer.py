import configparser
import pygame

# TODO Convert to a Class???

config = configparser.ConfigParser()
config.read('config/config.ini')
AUDIO_PATH = config['AUDIO']['FILE_PATH']
LOOPS = int(config['AUDIO']['LOOPS'])

def init():
    # pygame.mixer.init()
    BUFFER = 3072  # audio buffer size, number of samples since pygame 1.8.
    pygame.mixer.init(buffer=BUFFER)
    pygame.mixer.music.set_volume(0.5)

def start():
    print(f"Loading audio file {AUDIO_PATH}...")
    pygame.mixer.music.load(AUDIO_PATH)

def play(busy=False):
    print("Playing...")
    pygame.mixer.music.play(loops=LOOPS)
    if busy:
        while pygame.mixer.music.get_busy() == True:
            continue

def stop():
    print("Stopping...")
    pygame.mixer.music.stop()

def pause():
    # res = "Pausing at {}...".format(getCurrentTimePosition())
    res = f"Pausing at {getCurrentTimePosition()}..."
    print(res)
    pygame.mixer.music.pause()
    return res

def unpause():
    res = f"Resuming at {getCurrentTimePosition()}..."
    print(res)
    pygame.mixer.music.unpause()
    return res

def quit():
    print("Good bye!")
    pygame.quit()

# def volume_up():
#     v = pygame.mixer.music.get_volume()
#     v = 1 if v > 0.9 else v+0.1
#     pygame.mixer.music.set_volume(v)

# def volume_down():
#     v = pygame.mixer.music.get_volume()
#     v = 0 if v < 0.1 else v-0.1
#     pygame.mixer.music.set_volume(v)

def getCurrentTimePosition() -> str:
    pos = pygame.mixer.music.get_pos()
    time = convertMillisToHumanTime(pos)
    return time

def convertMillisToHumanTime(ms: int) -> str:
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
    print("Starting AudioPlayer with {}...".format(AUDIO_PATH))
    init()
    start()
    play()
    while pygame.mixer.music.get_busy() == True:
        continue
    quit()