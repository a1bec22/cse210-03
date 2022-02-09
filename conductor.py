from word_gen import word_gen
from player import Player
from display import * # Create a class Display in display.py

class Conductor():
    # print(word)

    def __init__(self):
        guessed = False
        self._guessed = guessed
        self._guessed_letters = []
        self._guessed_words = []
        self._tries = 4
        gen = word_gen()
        self._word = gen.generate_word()

    def get_guess():
        """
        This function retrieves the player's guess (a letter) as a result of the Player input
        """
        player = Player()
        _guess = player.guess_letter()
        return _guess

    def do_guess_logic(self):
        """
        This function  receives necessary data to process
        """
        player = Player()
        display = Display()
        while not self._guessed and self._tries > 0:
            guess = player.guess_letter()
            if len(guess) == 1 and guess.isalpha():
                if guess in self._guessed_letters:
                    print("You already guessed that letter", guess)
                elif guess not in self._word:
                    print(guess, "is not in the word.")
                    self._tries -= 1
                    self._guessed_letters.append(guess)
                else:
                    print("Good job,", guess, "is in the word!")
                    self._guessed_letters.append(guess)
                    word_as_list = list(word_completion)
                    indices = [i for i, letter in enumerate(
                        self._word) if letter == guess]
                    for index in indices:
                        word_as_list[index] = guess
                    word_completion = "".join(word_as_list)
                    if "_" not in word_completion:
                        guessed = True
            elif len(guess) == len(self._word) and guess.isalpha():
                if guess in self._guessed_words:
                    print("You already guessed the word", guess)
                elif guess != self._word:
                    print(guess, "is not the word.")
                    self._tries -= 1
                    self._guessed_words.append(guess)
                else:
                    _guessed = True
                    word_completion = self._word
            else:
                print("Not a valid guess.")
            print(display.display_parachute(self._tries))
            print(word_completion)
            print("\n")

# def main():
#     guess = get_guess()
#     print(guess)

# if __name__ == "__main__":
#     main()