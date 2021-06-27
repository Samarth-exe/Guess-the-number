import random
randNo = random.randint(1,20)
print('Guess the number between 1 and 20')
while True:
    a = int(input('Guess the number: '))
    
    if a>randNo:
        print('The number you guessed was too high')
    elif a<randNo:
        print('Your guess was too low')
    elif a==randNo:
        print(f'Good game, I was thinking of number {randNo}')
        break
    
    