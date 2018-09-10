import random
highest = 10
answer = random.randint(1, highest)

print('please guess a number between 1 and {}:'.format(highest))
guess = int(input())
while guess != answer:
    guess = int(input())
    if guess < answer:
        print('please guess higher')
    elif guess > answer:
        print('please guess lower')
    else:
        print('well done,you guessed it')
