from dealer import Dealer

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        dealer (Dealer): An instance of the class of objects known as Dealer.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.dealer = Dealer()

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.game.keep_playing():
            self.do_outputs()
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the dice that were rolled and the score.

        Args:
            self (Director): An instance of Director.
        """
        print(f"\nThe card is: {self.game.oldCard}")
        guess = input("Higher or lower? [h/l] ")
        correct = self.game.test_guess(guess)
        if correct:
            self.game.add_points()
        else:
            self.game.sub_points()
        print(f"\nThe card is: {self.game.oldCard}")
        print(f"Your score is: {self.game.getscore()}")
        playing = input("Keep playing? [y/n] ")
        if playing == "n":
            self.game.score = 0
                
        















