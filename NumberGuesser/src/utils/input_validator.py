
def get_valid_input(start, end):
    
    while True:

        user_input = input("Enter your number between 1 to 100: ")

        if user_input.lower() in ['q', 'quit']:
            return None

        if not user_input.isdigit() :
            print("Broooo!!! you're playing a number guesser... "
                  "a FUCKING NUMBER guesser. use your MIND")
            continue
        
        
        
        if int(user_input) not in range (start, end + 1):
            print ("Are you an IDIOT ?!"
                   "I told you betwee 1 to 100")
            continue
        
        

        
        return user_input
    
