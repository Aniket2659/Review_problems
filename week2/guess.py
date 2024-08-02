import random

def get_valid_range():
    while True:
        lower_range = int(input("Enter the lower range: "))
        upper_range = int(input("Enter the upper range: "))
        if lower_range > upper_range:
            print(" Upper range should be greater than lower range.")
        else:
            return lower_range, upper_range

def guessing_game(lower_range, upper_range):
    backend_number = random.randint(lower_range, upper_range)

    while True:
        guess = int(input(f"Guess the number between {lower_range} and {upper_range}: "))
        print(f'backend number is {backend_number}')
        
        if lower_range <= guess <= upper_range:
            if guess == backend_number:
                print('Congrats! You win!')
                break
            else:
                print('Sorry, you lose.')
                if guess > backend_number:
                    print('Guess number is too high.')
                    upper_range = guess - 1
                else:
                    print('Guess number is too low.')
                    lower_range = guess + 1
        else:
            print(f'Guess number is not between {lower_range} and {upper_range}. Please try again.')

lower_range, upper_range = get_valid_range()

guessing_game(lower_range, upper_range)
