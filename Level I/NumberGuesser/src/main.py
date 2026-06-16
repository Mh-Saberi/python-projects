from utils.input_validator import get_valid_input
from game_logic.number_generator import generate_random_number
from game_logic.hint_generator import hint_generator
from game_logic.scorer import scorer
from game_logic.quit import wanna_quit


def main():
    
    random_num = generate_random_number(1,100)
    score = scorer(100)
    
    while True:

        guessed_number = get_valid_input(1,100)

                    
        if guessed_number is None:
            print("Thanks for playinh. Byeee!!!")
            break

        elif random_num == int(guessed_number):
            print("OMG!! You WON :))) congrats")
            print(f"youe score is {score.get_score()}")
            break

        else:
            print(hint_generator(random_num, int(guessed_number)))
            score.Decrement_score()
            continue


    

if __name__ == '__main__':
    main()