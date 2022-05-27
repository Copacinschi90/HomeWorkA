import random
number = random.randint(1, 49)

player_name = input("Hi! May I know your name?")
number_of_guesses = 0
print('of course! '+ player_name+ ' guess a number between 1 and 49:')

while number_of_guesses < 7:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('The value is too low')
    if guess > number:
        print('The value is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed correctly ' + str(number_of_guesses) + ' tries!')
