from src.game import *

def main():       
    
    My_RockPaperScissors = RockPaperScissors()
    
    

    while True:
        print("Welcome to Rock Paper Scissors!")
        print("First to 3 points wins the game!")
        print("Let's begin!")
        
        player_score = 0
        computer_score = 0  

        
        while player_score < 3 and computer_score < 3:
            who_wins_this_round = My_RockPaperScissors.play_game()

            if who_wins_this_round == 'you got a point':
                player_score += 1
                print("you got a point, well done")
                

                        
            elif who_wins_this_round == 'same choice':
                print("you both chose the same thing, no points awarded")
            

            else:
                computer_score += 1
                print("ahhh you've lost a point but that's ok the game isn't finished yet")

            My_RockPaperScissors.show_scores(player_score, computer_score)

        



        if player_score > computer_score:
            print ("Congratulations! You've won the game!")

        else:
            print("I'm so sorry but you've lost the game")

        try:
            play_again = input("wanna play again? (Y/N)")

            if play_again in ['y', 'Y', 'yes', 'Yes']:
                continue

            elif play_again in ['n', 'N', 'no', 'No']:
                print("Thanks for playing! Goodbye!")
                break

        except ValueError:
            print("Invalid input! Please enter Y or N.")


                

if __name__ == '__main__':
    main()
        


