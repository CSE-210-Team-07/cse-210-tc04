
class game:
	def __init__(self):
		self.newCard = 0
		self.oldCard = 0
		self.score = 0

	def keep_playing(self):
		if self.score <= 0:
			return False
		else:
			return True

	def test_guess(self, guess):
		if guess == 'h' and self.newCard > self.oldCard:
			return True
		else:
			return False
	
	def add_points(self):
		self.score += 100
	
	def sub_points(self):
		self.score -= 75
	
	def get_points(self):
		return self.score