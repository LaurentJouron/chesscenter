"""Management of chess player results."""
import time

from utils.constant import Constants


class MatchController:
    """Controls the organization of games and scores in real time."""
    def __init__(self):
        self.constant = Constants()

    def blitz(self):
        """The blitz gives a maximum of 5 minutes to each player"""
        blitz_time = self.constant.BLITZ
        blitz = blitz_time * 60
        while blitz:
            minutes, seconds = divmod(blitz_time, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            blitz_time -= 1
        print("The game is over")

    def bullet_countdown(self):
        """The bullet gives a maximum of 2 minutes to each player"""
        bullet = self.constant.BULLET
        bullet = bullet * 60
        while bullet:
            minutes, seconds = divmod(bullet, 60)
            timer = '{:02d}:{:02d}'.format(minutes, seconds)
            print(timer, end="\r")
            time.sleep(1)
            bullet -= 1
        print("The game is over")