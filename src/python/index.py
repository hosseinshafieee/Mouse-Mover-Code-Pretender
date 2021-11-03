import argparse
import time
from pynput.mouse import Controller as MouseController
mouse = MouseController()

PIXELS = 50
AFK_TIME = 120
RANDOM_WRITING_TIMER = 60

KEYBOARD = False
MOUSE = False

BOTH = False


def start(mouseFile, keyboardFile):
    global KEYBOARD, MOUSE, PIXELS, AFK_TIME, RANDOM_WRITING_TIMER, BOTH

    parser = argparse.ArgumentParser(
        description="Author: Mohammad H. Shafiee  |     This is a mouse mover and coding pretender for the times that you are not coding.  |     for example, eating a meal or thinking in restroom.  |     This is a small script to deceive some tracing applications or extensions that installed to monitor your coding activity for any organization, but this is a game changer.  |     Warning: we not recommend to use this for cheating at work, this is just a fun project.")

    parser.add_argument(
        "-s", "--seconds", type=int,
        help="This command is for choosing the time to detect your AFK -- the default value is 2 min")

    parser.add_argument(
        "-p", "--pixels", type=int,
        help="This command is for the number of moving pixels -- the default value is 50px")

    parser.add_argument(
        "-r", "--random", type=int,
        help="This command is for random coding time -- the default value is 60 and do not choose a value more than 60 otherwise it takes a lot of time to pretend |    ")

    parser.add_argument(
        "-m", "--mode",
        help="This command is for choosing to move your mouse, pretend to code or use both of them ...  |    "
             "These things will activate only when you get AFK:   |    "
             "keyboard === just writing code  |    "
             "mouse === just moving the mouse  |    "
             "both === move mouse and pretend coding  |    ")

    args = parser.parse_args()
    mode = args.mode

    if args.seconds:
        AFK_TIME = int(args.seconds)

    if args.pixels:
        PIXELS = int(args.pixels)

    if args.random:
        RANDOM_WRITING_TIMER = int(args.random)

    BOTH = 'both' == mode
    KEYBOARD = 'keyboard' == mode
    MOUSE = 'mouse' == mode

    lastSavePosition = (0, 0)

    i = 0
    while 1:
        i += 1

        currentPosition = mouse.position
        is_user_away = currentPosition == lastSavePosition
        
        if is_user_away:
            if (KEYBOARD and MOUSE == False):
                print('\n       KEYBOARD MODE ENABLED \n')
                keyboardFile.start(RANDOM_WRITING_TIMER, i)

            if((MOUSE and KEYBOARD == False) or (MOUSE == False and KEYBOARD == False and BOTH == False)):
                print('\n       MOUSE MODE ENABLED \n')
                mouseFile.start(currentPosition, PIXELS)
                currentPosition = mouse.position

            if (BOTH):
                print('\n        BOTH MODE ENABLED \n')
                keyboardFile.start(RANDOM_WRITING_TIMER, i)
                mouseFile.start(currentPosition, PIXELS)
                currentPosition = mouse.position

        if not is_user_away:
            print('=============== \n \n USER IS AWAKE  \n \n===============')

        lastSavePosition = currentPosition

        time.sleep(AFK_TIME)
