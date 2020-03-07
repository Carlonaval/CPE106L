#CALAMBRO | NAVAL | EISMA
#Group05
"""
File : craps.py
This file has a class Player
that contains method which
plays craps game
"""
from die import Die

class Player(object):

    """
    Initializing variables
    and creating a pair of dice
    """
    def __init__(self):
        self.die1 = Die()
        self.die2 = Die()
        self.roll = ""
        self.rollsCtr = 0
        self.atStartup = True
        self.winner = False
        self.loser = False

    def __str__(self):
        return self.roll
    
    """
    This method returns the number of rolls
    """
    def getRollsCount(self):
        return self.rollsCtr

    def rollDice(self):
        self.rollsCtr += 1
        self.die1.roll()
        self.die2.roll()
        (v1, v2) = (self.die1.getValue(),
                    self.die2.getValue())
        self.roll = str((v1, v2)) + " total = " + str(v1 + v2)
        if self.atStartup:
            self.initialSum = v1 + v2
            self.atStartup = False
            if self.initialSum in (2, 3, 12):
                self.loser = True
            elif self.initialSum in (7, 11):
                self.winner = True
        else:
            laterSum = v1 + v2
            if laterSum == 7:
                self.loser = True
            elif laterSum == self.initialSum:
                self.winner = True
        return (v1, v2)

    def isWinner(self):
        return self.winner
    
    def isLoser(self):
        return self.loser

    def play(self):
        while not self.isWinner() and not self.isLoser():
            self.rollDice()
        return self.isWinner()
    
    """ 
    Plays the first game and
    displays the result
    """
def playOneGame():
    
    player = Player()
    while not player.isWinner() and not player.isLoser():
        player.rollDice()
        print(player)
    if player.isWinner():
        print("Number of rolls: " + str(player.getRollsCount()))
        print("You win!")
    else:  
        print("Number of rolls: " + str(player.getRollsCount()))
        print("You Lose!")  

    """
    This is where the user is prompted and plays the game.
        The result is calculated and the average of the results
        are displayed
    """
def playManyGames(number):
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    for count in range(number):
        player = Player()
        hasWon = player.play()
        rolls = player.getRollsCount()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls
    print("The number of wins is", wins)
    print("The number of losses is", losses)
    print("The average number of rolls per win is %0.2f" % \
            (winRolls / wins))
    print("The average number of rolls per win is %0.2f" % \
            (lossRolls / losses))
    print("The winning percentage is %0.3f" % (wins / number))

def main():
    playOneGame()
    number = int(input("Enter number of games: "))
    playManyGames(number)

if __name__ == "__main__":
    main()
