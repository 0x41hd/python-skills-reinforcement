from typing import List, Tuple, Dict
import random


class RockPaperScissors:
    """ Main class for the game Rock, Paper, Scissor """

    def __init__(self, name: str) -> str:
        self.choice = ["rock", "paper", "scissors"]
        self.player_name = name
        self.user_score = 0
        self.bot_score = 0

    def get_player_choice(self) -> str:
        """Method to get the user's choice."""
        player_choice = input(f"{self.choice} \n").lower()
        if player_choice in self.choice:
            return player_choice
        else:
            print(f"Invalid choice, you must select from \n {self.choice}")
            self.get_player_choice()

    def get_computer_choies(self) -> str:
        """ Method to select the computer's choice. """
        bot_choice = self.choice[random.randrange(0, 3)]
        return bot_choice

    def winner(self) -> str:
        """ Method to find winner with 3 point. """
        if self.user_score == 3:
            return self.player_name
        elif self.bot_score == 3:
            return "Computer"
        else:
            self.play()

    def decide_win(self, user: str, bot: str):
        """ Method to decide match winner based on the rules. """
        if user == bot:
            print("It's a tie!")
            self.play()
        elif (user == "rock" and bot == "scissors") or \
             (user == "scissors" and bot == "paper") or \
             (user == "paper" and bot == "rock"):
            self.user_score += 1
            print(
                f"{self.player_name} win. You: {self.user_score} - Bot:{self.bot_score}")
            self.winner()
        else:
            self.bot_score += 1
            print(f"Bot win. You: {self.user_score} - Bot:{self.bot_score}")
            self.winner()

    def play(self):
        """ Main method to play Rock, Paper, Scissors """
        user_choice = self.get_player_choice()
        bot_choice = self.get_computer_choies()
        print(f"Computer choice: {bot_choice}")
        play = self.decide_win(user_choice, bot_choice)
        winner = self.winner()
        print(
            f"{winner} is winner !! \n Score: \n computer:{self.bot_score} - {self.player_name}:{self.user_score}")


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()
