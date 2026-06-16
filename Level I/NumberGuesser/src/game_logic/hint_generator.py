
def hint_generator(random_number, guessed_number):

    if random_number < guessed_number:
        return "my number is lower"
    if random_number > guessed_number:
        return "my number is higher"
    