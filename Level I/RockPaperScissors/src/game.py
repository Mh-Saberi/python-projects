import random


class RockPaperScissors :
    
    def __init__(self):
        self.game_rules = {'rock' : 'scissors', 'scissors' : 'paper', 'paper' : 'rock'}
    

    def get_computer_choice(self, game_list=['rock', 'paper', 'scissors']):
        return random.choice(game_list)
    

    def get_player_choice(self):
        print("Please choose:")
        print("1. rock")
        print("2. paper")
        print("3. scissors")
        player_choice = int(input("Choose your option (1 to 3): "))

        match player_choice:
            case 1:
                return 'rock'
            case 2:
                return 'paper'
            case 3:
                return 'scissors'
            case _:
                print("Invalid choice! Please choose a valid option.")
                return self.get_player_choice()

    def decide_who_wins(self, user_choice, computer_choice):
        
        if user_choice == computer_choice:
            return "same choice"

        if self.game_rules[user_choice] == computer_choice :
            return "you got a point"

        else:
            return " got a point"

    def show_scores(self, player_score, computer_score):
        print(f"Current Scores - You: {player_score}, Computer: {computer_score}")

    def play_game(self):
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        return self.decide_who_wins(player_choice, computer_choice)





