'''This class defines a character object also used as a base for villains.'''


class Character:
    def __init__(self, wearing, health, weapon, shield):
        self._wearing = wearing
        self._health = health
        self._weapon = weapon
        self._shield = shield

    # This method causes damage to be applied to a player by decreasing their health
    def injured(self, damage):
        injure = True
        try:
            if damage < 0:
                print("Negative damage is not possible!")
                injure = False
        except ValueError:
            print("That much damage is not possible!")
            injure = False
        if injure:
            self._health -= damage

    # This method will heal a character a specified amount
    def heal(self, healed):
        canHeal = True
        try:
            if healed < 0:
                print("Negative healing is not possible!")
                canHeal = False
        except ValueError:
            print("That much healing is not possible!")
            canHeal = False
        if canHeal:
            self._health += healed

    # Returns the amount of health a player has remaining
    def getHP(self):
        return self._health
