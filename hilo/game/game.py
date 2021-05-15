import random

class Game:
	def __init__(self):
		self.oldCard = random.randint(1,13)
		self.score = 0

	def keep_playing(self):
		if self.score <= 0:
			return False
		else:
			return True

	def test_guess(self, guess):
		correct = False
		newCard = random.randint(1,13)
		if guess == 'h' and newCard >= self.oldCard:
			correct = True
		elif guess == 'l' and newCard <= self.oldCard:
			correct = True
		
		self.oldCard = newCard
		
		return correct
	
	def add_points(self):
		self.score += 100
	
	def sub_points(self):
		self.score -= 75
	
	def get_score(self):
		return self.score
	
	def get_card(self):
		return self.oldCard
