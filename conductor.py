from word_gen import word_gen
from player import Player
from display import Display


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
        self._word_completion = "_" * len(self._word)

    def start(self):

        self.play = True
        gen = word_gen()
        self._word = gen.generate_word()
        display = Display()
        while self.play:
            print(display.display_parachute(self._tries))
            self.get_guess()
            self.do_guess_logic()
        self.game_end()
        # return self._word

    def get_guess(self):
        """
        This function retrieves the player's guess (a letter) as a result of the Player input
        """
        player = Player()
        self._guess = player.guess_letter()
        return self._guess

    def do_guess_logic(self):
        """
        This function  receives necessary data to process
        """
        player = Player()
        display = Display()
        while not self._guessed and self._tries > 0:
            self._guess = player.guess_letter()
            if len(self._guess) == 1 and self._guess.isalpha():
                if self._guess in self._guessed_letters:
                    print("You already guessed that letter", self._guess)
                elif self._guess not in self._word:
                    print(self._guess, "is not in the word.")
                    self._tries -= 1
                    self._guessed_letters.append(self._guess)
                else:
                    print("Good job,", self._guess, "is in the word!")
                    self._guessed_letters.append(self._guess)
                    word_as_list = list(self._word_completion)
                    indices = [i for i, letter in enumerate(
                        self._word) if letter == self._guess]
                    for index in indices:
                        word_as_list[index] = self._guess
                    self._word_completion = "".join(word_as_list)
                    if "_" not in self._word_completion:
                        self._guessed = True
            elif len(self._guess) == len(self._word) and self._guess.isalpha():
                if self._guess in self._guessed_words:
                    print("You already guessed the word", self._guess)
                elif self._guess != self._word:
                    print(self._guess, "is not the word.")
                    self._tries -= 1
                    self._guessed_words.append(self._guess)
                else:
                    self._guessed = True
                    self._word_completion = self._word
            else:
                print("Not a valid guess.")
            print(display.display_parachute(self._tries))
            print(self._word_completion)
            print("\n")

    def game_end(self):
        if self._guessed:
            print("Congrats, you guessed the word! You win!")
        else:
            print("Sorry, you ran out of tries. The word was " +
                  self._word + ". Maybe next time!")

        while input("Play Again? (Y/N) ").upper() == "Y":
            # gen = word_gen()
            # self._word = gen.generate_word()
            # self.get_guess(self._word)
            # self.do_guess_logic(self._word)
            self.start()

# def main():
#     guess = get_guess()
#     print(guess)

# if __name__ == "__main__":
#     main()
