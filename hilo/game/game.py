class game:
    def __init__(self):
        self.newCard = 0
        self.oldCard = 0

    def keep_playing(score):
        if score == 0:
            return False
        else:
            return True

    def test_guess(self, guess):
        if guess == 'h' and self.newCard > self.oldCard:
            return True
        else:
            return False

        if guess == 'l' and self.newCard < self.oldCard:
            return True
        else: 
            return False