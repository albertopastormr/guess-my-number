from random import randint

def guessing():
    number_to_guess = randint(0,1000)
    print (number_to_guess)
    print ('Okay, I thought a number between 0 and 1000, can you guess it? (type "-1" to exit)')
    guess = int(input('Type your guess: '))
    while((guess is not number_to_guess) and (guess is not -1)):
        if(guess > number_to_guess):
            print('Wrong ! Too high !')
            guess = int(input('Type another guess: '))
        elif (guess < number_to_guess):
            print('Wrong ! Too low !')
            guess = int(input('Type another guess: '))
    if(guess is number_to_guess):
        print('Correct ! How did you do it? :O')
    
if __name__ == '__main__':
    guessing()