'''This class defines the inventory object and, its applicable methods'''
class Inventory:
    #This init function instantiates an inventory with given objects.
    #If a dictionary is not provided then, the character will start with a
    #dagger and three sandwiches.
    def __init__(self, starterInventory = {'Rusty Dagger': 1, 'Sandwich': 3}, maxSize = 10):
        self._inventory = starterInventory
        self._bagSize = maxSize

    #Returns number of items in inventory
    def __len__(self):
        returnValue = 0
        for key, value in self._inventory.items():
            returnValue += value
        return returnValue

    #Returns True if inventory has a length of 0
    def _is_empty(self):
        return len(self) == 0
    
    #Prints the inventory to the display
    def __str__(self):
        returnString = "You have " + str(len(self)) + " items and " + str(self._bagSize - len(self)) + " open spaces in your inventory"
        if self._is_empty():
            returnString += ".\n"
        else:
            returnString += ":\n------------------------------------------------------------\n"
            for key, value in self._inventory.items():
                returnString += (str(value) + 'x\t' + key + '\n')
        return returnString

    #Adds a number of an item to the inventory if the inventory is not full.
    def add(self, itemInput, number = 1):
        item = itemInput.title()
        addItems = True
        try:
           number < 0
        except TypeError:
            print("You have tried to pick up an invalid number of items. Please try again.")
            addItems = False
        if addItems == True:
            if number < 1:
                print("The number of an items to pick up must be greater than zero.")
            elif len(self) >= self._bagSize:
                print("Your bag is already full. Please drop or use something before you try to pick more up.")
            elif (len(self) + number) > self._bagSize:
                x = (self._bagSize - len(self))
                if item in self._inventory.keys():
                    self._inventory[item] += x
                else:
                    self._inventory[item] = x
                print("The number of items you tried to add would push your inventory over its limit. You were able to add " + str(x) + " items to your inventory though.")
            else:
                if item in self._inventory.keys():
                    self._inventory[item] += number
                else:
                    self._inventory[item] = number

    #This method will remove a number of items if there is enough in the inventory to be able to.
    def remove(self, itemInput, number = 1):
        item = itemInput.title()
        removeItems = True
        try:
           number < 0
        except TypeError:
            print("You have use or remove to an invalid number of items. Please try again.")
            removeItems = False
        if item not in self._inventory.keys():
            print("You can't use or remove an item you don't have. Please try again.")
            removeItems = False
        if removeItems == True:
            if number < 1:
                print("The number of an items used must be greater than zero.")
            elif number > self._inventory[item]:
                print("You don't have enough to do this.")
            else:
                self._inventory[item] -= number
        