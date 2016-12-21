'''This class defines a character object also used as a base for villains.'''
# from Inventory import Inventory


class Character:
    def __init__(self, name, wearing, health, weapon, shield, startingInventory):
        self._name = name
        self._wearing = wearing
        self._health = health
        self._weapon = weapon
        self._shield = shield
        self._maxHP = health
        self._inventory = startingInventory

    # This method causes damage to be applied to a player by decreasing their health
    def injured(self, damage):
        injure = True
        try:
            if damage < 0:
                print("Negative damage is not possible!")
                injure = False
        except TypeError:
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
        except TypeError:
            print("That much healing is not possible!")
            canHeal = False
        if canHeal and self._maxHP < self._health + healed:
            self._health = self._maxHP
        elif canHeal:
            self._health += healed

    # Returns the amount of health a player has remaining
    def getHP(self):
        return self._health

    # This method allows for clothing to be changed
    def setClothing(self, item, article):
        if item in self._wearing.keys():
            self._wearing[item] = article
        else:
            print("Sorry you can't wear a " + item + ".")

    # Removes a clothing item and puts it in the character's inventory if it's not full
    def removeClothing(self, item):
        if item in self._wearing.keys() and self._wearing[item] is not None:
            if self._inventory.isFull():
                print("You don't have space in your inventory to take your " + item + " off.")
            else:
                self._inventory.add(self._wearing[item])
                self._wearing[item] = None
        else:
            print("Sorry, you can't take off something you aren't wearing.")
