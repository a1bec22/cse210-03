class Player():
    def __init__(self):
        self._chosen_letters = []

    def guess_letter(self):
        _guess = str(input("Guess your letter A-Z! ")).lower()
        while len(_guess) != 1 or _guess in self._chosen_letters:
            _guess = str(input("Guess your letter A-Z! "))
        self._chosen_letters.append(_guess.lower())  
        return _guess