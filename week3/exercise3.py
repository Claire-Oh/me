"""Week 3, Exercise 3.

Steps on the way to making your own guessing game.
"""

import random


def advancedGuessingGame():
    """Play a guessing game with a user.

    The exercise here is to rewrite the exampleGuessingGame() function
    from exercise 3, but to allow for:
    * a lower bound to be entered, e.g. guess numbers between 10 and 20
    * ask for a better input if the user gives a non integer value anywhere.
      I.e. throw away inputs like "ten" or "8!" but instead of crashing
      ask for another value.
    * chastise them if they pick a number outside the bounds.
    * see if you can find the other failure modes.
      There are three that I can think of. (They are tested for.)

    NOTE: whilst you CAN write this from scratch, and it'd be good for you to
    be able to eventually, it'd be better to take the code from exercise 2 and
    merge it with code from excercise 1.
    Remember to think modular. Try to keep your functions small and single
    purpose if you can!
    """

    print("\nWelcome to the guessing game!")
    print("A number between _ and _ ?")
    upperBound = False
    while type(upperBound) is not int:
        try:
            upperBound=int(input("Enter an upper bound value: "))
        except ValueError:
            print('This is not an integer!')

    lowerBound = False
    while type(lowerBound) is not int:
        try:
            lowerBound = int(input("Enter a lower bound value: "))
        except ValueError:
            print('This is not an integer!')

    
    upperBound = int(upperBound)
    lowerBound = int(lowerBound)

    if lowerBound > upperBound:
        temp = lowerBound
        lowerBound = upperBound
        upperBound = temp
        print('Please pick a number between the bounds')

    print("Pick a number between " + str(lowerBound) + " and {} ?".format(upperBound))    

    actualNumber = random.randint(lowerBound, upperBound)

    guessed = False

    while not guessed:
        guessedNumber = False
        while type(guessedNumber) is not int:
            try:
                guessedNumber = int(input("Guess a number: "))
            except ValueError:
                print('Please try again with an integer')

        print("You guessed {},".format(guessedNumber),)
        if guessedNumber == actualNumber:
            print('You got it!')
            guessed = True
        elif guessedNumber < actualNumber:
            print("Too small, try again")
        else:
            print("Too big, try again")
        if guessedNumber < lowerBound:
            print('That is the lower bound try again please')
        elif guessedNumber > upperBound:
          print('That is the upper bound try again please')
    return "You got it!"

    


if __name__ == "__main__":
    print(advancedGuessingGame())
