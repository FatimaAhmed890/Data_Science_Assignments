import random
from words import word_list

class Hangman:
    def __init__(self):
        self.chosen_word: str = ""
        self.guess: str = ""
        self.display: str = []
        self.words_list: str = word_list
        self.lives: int = 6
        self.word_guessed: bool = False
        self.indices: int = []
        self.stages: str = [
            """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,

            """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,

            """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,

            """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,

            """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,

            """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,

            """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
        ]

    def display_stages(self, lives):
        return self.stages[lives]

    @property
    def get_word(self):
        chosen_word = random.choice(self.words_list)
        return chosen_word

    def play_hangman(self):
        print("LET'S PLAY HANGMAN!\n")
        self.chosen_word = self.get_word
        self.display = ["_" for _ in self.chosen_word]
        
        while not self.word_guessed and self.lives > 0:
            print(self.display_stages(self.lives))
            print(*self.display, sep=" ")
            self.guess = input("\nGuess a letter for the word: ").lower()
            
            if len(self.guess) == 1 and self.guess.isalpha():
                if self.guess in self.chosen_word:
                    self.indices = [i for  i, letter in enumerate(self.chosen_word) if letter == self.guess]
                    for index in self.indices:
                        self.display[index] = self.guess
                    
                    if "_" not in self.display:
                        self.word_guessed = True
                        print("\nWohoo you have correctly guessed the word")
                        print(f"\nThe word is \"{self.chosen_word}\"")
                else:
                    print("\nNot a valid guess :(\n")
                    self.lives -= 1
            else:
                print("\nNot a valid guess :(")
            
            if self.word_guessed:
                print("\nYou Won!")
            elif self.lives <= 0:
                print(self.display_stages(self.lives))
                print(f"\nThe word was \"{self.chosen_word}\"")
                print("\nYou Lost :(")