from enum import Enum
from random import shuffle

class Random:
    def __init__(self):
        self.indexes: list[int] = []
        self.__reset()

    @property
    def get_choice(self) -> int:
        if len(self.indexes) == 0:
            self.__reset()

        choice: int = self.indexes.pop()
        return choice

    def __reset(self):
        global choices
        self.indexes = [i for i in range(len(choices))]
        shuffle(self.indexes)

class Choice(Enum):
    STONE = 'Stone'
    PAPER = 'Paper'
    SCISSOR = 'Scissor'

# Game Variables
choices: list[Choice] = [Choice.STONE, Choice.PAPER, Choice.SCISSOR]
players: list[int] = [
    0,  # Human
    0   # AI
]
ai: Random = Random()
game_over: bool = False

def is_valid_choice(choice: int) -> bool:
    """ Function to check if the choice is valid or not """
    return 0 <= choice < len(choices)

def is_draw(human_choice: Choice, ai_choice: Choice) -> bool:
    """ Function to check for draw """
    return human_choice == ai_choice

def is_won(human_choice: Choice, ai_choice: Choice) -> bool:
    """ Function to check for winner """
    win_cases: list = [[Choice.STONE, Choice.SCISSOR],
                       [Choice.PAPER, Choice.STONE],
                       [Choice.SCISSOR, Choice.PAPER]]

    return [human_choice, ai_choice] in win_cases

def announce_results():
    print("\n********************** Results **********************")
    print("Human:", players[0], sep='\t')
    print("AI:", players[1], sep='\t')

if __name__ == '__main__':
    while not game_over:
        print("******************** Match ********************")
        ai_choice: Choice = choices[ai.get_choice]
        choice: int = 0
        while True:
            choice = int(input("0-End Game, 1-Stone, 2-Paper, 3-Scissor: "))
            if choice == 0:
                game_over = False
                announce_results()
                exit()

            choice -= 1
            if is_valid_choice(choice):
                break

            print("Invalid Choice!")

        human_choice: Choice = choices[choice]

        print(f"You choose '{human_choice.value}' and your opponent choose '{ai_choice.value}'.")

        draw: bool = is_draw(human_choice, ai_choice)
        if draw:
            print("Draw!")
            continue

        won: bool = is_won(human_choice, ai_choice)
        if won:
            print("Won!")
            players[0] += 1
        else:
            print("Lose!")
            players[1] += 1

    announce_results()
