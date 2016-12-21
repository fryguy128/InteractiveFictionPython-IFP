'''This class defines a character object also used as a base for villains.'''


class Character:
    def __init__(self, wearing, health, armedWith):
        self._wearing = wearing
        self._health = health
        self._armedWith = armedWith
