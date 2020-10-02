import time

from actions import Utils
from assistant import ItsFriday


def driver():
    # sequence of commands to run the assistant
    friday = ItsFriday()
    utils = Utils()
    friday.speak(utils.wish())
    while True:
        action = friday.listen()
        friday.takeAction(action)
        time.sleep(1)
        time.sleep(1)
        friday.speak("Anything else sir")


driver()
