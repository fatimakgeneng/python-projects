from typing import List, Optional
from enum import Enum
import random

class GameChoice(Enum):
    HIGHER = "higher"
    LOWER = "lower"

class GameResult:
    def __init__(self, player_number: int, computer_number: int, player_choice: GameChoice, is_correct: bool):
        self.player_number = player_number
        self.computer_number = computer_number
        self.player_choice = player_choice
        self.is_correct = is_correct

class Player:
    def __init__(self, name: str, age: int):
        self.name = name
        self.__score = 0
        self.age = age
        self.__game_history: List[GameResult] = []

    def update_score(self, points: int) -> None:
        self.__score += points

    @property
    def score(self) -> int:
        return self.__score

    def add_game_result(self, result: GameResult) -> None:
        self.__game_history.append(result)

    def game_history(self) -> List[GameResult]:
        return self.__game_history.copy()

class Game:
    MIN_NUMBER: int = 1
    MAX_NUMBER: int = 100

    def __init__(self, number_of_rounds: int):
        if number_of_rounds < 1:
            raise ValueError("Number of rounds must be positive.")
        self.number_of_rounds = number_of_rounds
        self.__attempts: int = 0
        self.__current_round: int = 1
        self.__win_or_loss: Optional[bool] = None

    @property
    def is_game_over(self) -> bool:
        return self.__attempts >= self.number_of_rounds

    def validate_choice(self, choice: str) -> GameChoice:
        try:
            return GameChoice(choice.lower())
        except ValueError:
            raise ValueError("Invalid choice. Please enter 'higher' or 'lower'.")

    def play_round(self, player: Player) -> None:
        player_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)
        computer_number = random.randint(self.MIN_NUMBER, self.MAX_NUMBER)

        print(f"\nRound {self.__current_round} of {self.number_of_rounds}")
        print(f"Your number is: {player_number}")

        while True:
            try:
                choice = self.validate_choice(
                    input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip()
                )
                break
            except ValueError as e:
                print(e)

        is_human_number_higher = player_number > computer_number
        is_correct = (choice == GameChoice.HIGHER and is_human_number_higher) or \
                    (choice == GameChoice.LOWER and not is_human_number_higher)

        result = GameResult(player_number, computer_number, choice, is_correct)
        player.add_game_result(result)

        if is_correct:
            print("Correct! You win this round.")
            player.update_score(1)
        else:
            print(f"Incorrect. The computer's number was: {computer_number}.")

        self.__attempts += 1
        self.__current_round += 1
        print("Your score is:", player.score)

    def display_game_statistics(self, player: Player) -> None:
        print("\n=== Game Statistics ===")
        print(f"Player: {player.name}")
        print(f"Total Rounds Played: {self.__attempts}")
        print(f"Final Score: {player.score}")

        correct_guesses = sum(1 for result in player.game_history() if result.is_correct)
        accuracy = (correct_guesses / self.number_of_rounds) * 100
        print(f"Accuracy: {accuracy:.2f}%")

    def play_game(self, player: Player) -> None:
        print("\nWelcome to the High-Low Game!")
        print("=" * 30)

        while not self.is_game_over:
            self.play_round(player)

        self.display_game_statistics(player)

if __name__ == "__main__":
    # Example usage
    player_name = input("Enter your name: ")
    player_age = int(input("Enter your age: "))
    rounds = int(input("How many rounds would you like to play? "))

    player = Player(player_name, player_age)
    game = Game(rounds)
    game.play_game(player)




         


