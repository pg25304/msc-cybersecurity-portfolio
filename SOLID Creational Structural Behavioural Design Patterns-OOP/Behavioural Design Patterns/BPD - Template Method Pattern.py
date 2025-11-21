from abc import ABC, abstractmethod
#Template Method Pattern
#Defines a new class Game that inherits from ABC — so Game is an abstract base class.
#You cannot (should not) create a useful Game instance directly because it has abstract
# methods that subclasses must implement.

#You cannot create a useful Game instance directly because it has abstract methods that subclasses must implement.
#play(self) is a concrete method on the base class that defines the fixed algorithm /
# sequence of steps for playing any game.It calls three methods in order:
class Game(ABC):
    def play(self):
        self.initialize() #set up the game
        self.start_play() #begin the game play
        self.end_play() #wrap up the game
#Important: play() is not abstract. It provides the template (the invariant order) that all games share.
    @abstractmethod
    #Declares initialize as an abstract method — subclasses must provide an implementation.
    def initialize(self):
        #pass is a placeholder; this base version does nothing.
        pass
    def start_play(self):
        pass
    def end_play(self):
        pass
#Concrete subclass Criket that implements the abstract methods from Game.
#Defines a concrete subclass Cricket that inherits from Game.
#Because Game had abstract methods, Cricket must override them or Cricket itself would remain abstract.
class Cricket(Game):
    #Implements the required initialize method for Cricket.
#When called, it prints a message — in a real program this could set players, toss coin, prepare pitch, etc.
    def initialize(self):
        print("Cricket Game Initialized! Start playing.")
    def start_play(self):
        print("Cricket Game Started. Enjoy the game!")
    def end_play(self):
        print("Cricket Game Finished!")

#client code
if __name__ == "__main__":
    #Creates an instance of Cricket.
    game = Cricket()
    #Calls the play() method on the Cricket instance.
    # This runs the full sequence: initialize, start_play, end_play.
    game.play()
#Output:
#Cricket Game Initialized! Start playing.
#Cricket Game Started. Enjoy the game!
#Cricket Game Finished!

