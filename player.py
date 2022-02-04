class Player():
    def __init__(self):
        self.chosen_letters = []

    def guess_letter(self):
        guess = str(input("Guess your letter a-z! ")).lower()
        while len(guess) != 1 or guess in self.chosen_letters:
            guess = str(input("Guess your letter a-z! "))
        self.chosen_letters.append(guess.lower())  
        return guess