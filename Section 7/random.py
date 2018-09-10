print('please guess a number between 1 and 10: ')
guess = int(input())

if guess != 5:
    if guess < 5:
        print('please guess higher')
    else:
        print('please guess lower')

    guess = int(input())
    if guess == 5:
        print('well done, you guessed it')
    else:
        print('sorry, you have not guessed correctly')
else:
    print('you got it the first time')
