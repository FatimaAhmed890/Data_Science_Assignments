class compatibility:
    def __init__(self) -> None:
        self.counter_1: int = 0
        self.counter_2: int = 0
        self.score: int = 0
        self.true: str = "TRUE"
        self.love: str = "LOVE"

    def love_compatibility(self, name: str, name_2: str) -> str:
        couple: str = (name + name_2).lower()
        # counter_1: int = len([x for x in couple if x in true.lower()])
        # counter_2: int = len([x for x in couple if x in love.lower()])

        for character in self.true.lower():
            self.counter_1 += couple.count(character)

        for character in self.love.lower():
            self.counter_2 += couple.count(character)

        self.score: int = int(str(self.counter_1) + str(self.counter_2))
        
        if self.score < 10 or self.score > 90:
            return f"Your score is {self.score}, you got together like coke and mentos."
        elif self.score > 40 and self.score < 50:
            return f"Your score is {self.score}, you  are alright together."
        else:
            return f"Your score is {self.score}."

if __name__ == "__main__":
    person_1: str = input("Enter your name: ")
    person_2: str = input("Enter your partner's name: ")

    check = compatibility()
    print(check.love_compatibility(person_1, person_2))