#CALAMBRO | NAVAL | EISMA
#Group05

"""
This module has a class that 
generates a random number from (1-6)
which would represent a dice.
"""

from random import randint

class Die:
    
    def __init__(self):
        self.value = 1

    def roll(self):
        self.value = randint(1, 6)

    def getValue(self):
        return self.value

    def __str__(self):
        return str(self.getValue())