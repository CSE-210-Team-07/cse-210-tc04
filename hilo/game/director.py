from game.game import Game


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
		self.keep_playing = True
		self.game = Game()

	def start_game(self):
		"""Starts the game loop to control the sequence of play.
		
		Args:
			self (Director): an instance of Director.
		"""
		
		
		while self.keep_playing:
			print("The current card has a value of " + str(self.game.get_card()))
			guess = self.get_inputs()
			correct = self.do_updates(guess)
			self.do_outputs(correct)
			

	def get_inputs(self):
		"""Gets the inputs at the beginning of each round of play. In this case,
		that drawing a new card and recalling the old card.

		Args:
			self (Director): An instance of Director.
		"""
		# Get guess from user.
		guess = input("Higher or Lower (h/l)? ")
		
		# Account for differing answers and format them in a useable manner. 
		guess = guess.lower()[0]
		
		return guess
		
		

	def do_updates(self, guess):
		"""Updates the important game information for each round of play. In 
		this case, that means updating the score.

		Args:
			self (Director): An instance of Director.
		"""
		if(self.game.test_guess(guess)):
			self.game.add_points()
			return True
		else:
			self.game.sub_points()
			return False

	def do_outputs(self, correct):
		"""Outputs the important game information for each round of play. In 
		this case, that means the dice that were rolled and the score.

		Args:
			self (Director): An instance of Director.
		"""
		
		if(correct):
			print("Correct!")
			print("The card was a " + str(self.game.get_card()))
		else:
			print("Wrong!")
			print("The card was a " + str(self.game.get_card()))
		
		if not self.game.keep_playing():
			print("Your score dropped below 1\nGame Over!")
			self.keep_playing = False
			return
		
		print("You have a current score of: " + str(self.game.get_score()))
		print("Would you like to continue playing?")
		cont = input("(y/n): ")
		
		cont = cont.lower()[0]
		
		if(cont == "n"):
			self.keep_playing == False
