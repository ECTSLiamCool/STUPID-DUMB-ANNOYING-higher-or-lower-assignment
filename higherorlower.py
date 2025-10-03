import random



def get_user_input(min = 0, max = 100):


    try:
        user_in = int(input(f"Guess the number I'm thinking of between {min} and {max} >  "))
        
        return user_in
        return guess_number
    except ValueError:
        print("You didn't enter an int. Try again")

    

def play_again():
    while True:
        play_again = input("Play again? y/n > ").strip().lower()
        if play_again == "y":
            main()
        elif play_again == "n":
            print("Have a good day.")
            return False
        

def conditions(result, random_num, guess_number):

    if result < random_num:
        print("Too low!")
        #guess_number += 1
    elif result > random_num:
        print("Too high!")
        #guess_number += 1
    elif result == random_num:
            print(f"Congratulations! You guessed the number. You took {guess_number} tries.")
            play_again()


def main():
    guess_number = 0
    random_num = random.randint(1, 100)
    while True: #break this into a function "get_user_input" #user_input = get_user_input()
        result = get_user_input()
        guess_number += 1
        result = conditions(result, random_num, guess_number)
        
        
    
    


    
    
    
    
    
    
    """the computer will pick a random number between 1 and 100. it will prompt the user to guess the number. if the user guesses too high or too low,
        it will say whether it is too high or too low. if the user guesses the correct number, it will state that the user guessed correctly, and it will
        also state the number of guesses."""

if __name__ == "__main__":
    main()
        #get input from user. Break if the user says no to play again