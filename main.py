"""
This program (higher or lower) is a color based text interface game that was made in a
singular software development and design class. It is not refined but i made it for the
purposes of outlining the python language and the process of adding docuementation correctly
to functions (and would be classes that aren't present here).

Email: joshuarose099@gmail.com
GitHub: https://github.com/users/JoshuaRoseGithub
"""

# Random is a module that allows random selections of variables and numbers
import random
# Colorama is a color module for the console
from colorama import Fore, init as cinit

# Define author for credibility purposes
__author__ = "Joshua Rose"

# Initialize the colorama module (allows color as a unicode console feature)
cinit()


# Choose the number
def choose():
    """ Function that chooses a number between 1 and 100"""
    return random.randint(1, 100)


def main():
    """ The main program"""

    # Set a variable to a random number (see line 9)
    number = choose()
    # Return the following message
    print(Fore.MAGENTA + "\nGuess a number between the range of 1 & 100 -->" + Fore.RESET)

    def try_again():

        """ The repeating function that queries a try again phase """

        try:
            # Ask for input
            play_again = int(input("$ "))
            # convert play_again to lowercase and decipher output
            if play_again.lower() == 'y' or 'yes':
                # Run the main function
                main()
            # convert play again to lowercase and decipher output
            elif play_again.lower() == 'n' or 'no':
                # Stop the function try_again() and returns to the main() function
                return
            # If input does not meet criteria define else statement
            else:
                # Return an error statement
                print(Fore.LIGHTYELLOW_EX + "Invalid symbol or character, Please enter y or n." + Fore.RESET)
                # Run the try_again sequence
                try_again()
        # If the try statement contains anything that's not a number
        except ValueError:
            # Return an error message
            print(Fore.LIGHTYELLOW_EX + "Invalid symbol or character, Please enter y or n." + Fore.RESET)
            # Repeat the whole function
            try_again()

    def start_loop():

        """
        Start loop is solely for the purposes of seperating the parts of main()
        to make the code easier to navigate and to execute parts of it when needed
        """

        # While function is in execution do the following
        while True:

            # exception handler
            try:
                # Ask for a number and convert the input to integer format
                guess = int(input("$ "))
            # If the guess is not a number or unrecognized number do the following
            except ValueError:
                # Return an error message
                print(Fore.RED + "Invalid symbol or character! Keep guessing." + Fore.RESET)
                # Repeat the function start_loop
                start_loop()

            # If the input guess, (see earlier) is greater than the number value
            if guess > number:
                # Return the following
                print("Number is lower")
            # IF the input guess, (see earlier) is less than the number value
            elif guess < number:
                # return the following
                print("Number is higher")
            # If the guess is equal to the number (AKA correct), do the following
            elif guess == number:
                # Return the following
                print(Fore.GREEN + "Correct! \n")
                print(Fore.RESET + "Play again?" + "\n")
                # Execute the try_again function
                try_again()

    # Evokes the start_loop function when while loop is called.
    start_loop()


# If the script file is valid do the following an execute the main() function
if __name__ == "__main__":
    # Executes the main() function and calls it once script file is validated
    main()
