# Another starter project I made alongside the slots game. The plan was to make a bunch of random casino games and compile them into one program but I honestly forgot about it after a while.

import random

number = 'placeholder'
prediction = 'placeholder'
win = 0
highscore = 20
wager = 1
coins = 20
bank_color = ['Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red',
         'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black', 'Black',
         'Green', 'Green']
bank_red_number = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
bank_black_number = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
bank_green_number = [0, 00]

print("""
  ____  _         __  __                        
 | __ )(_) __ _  |  \\/  | ___  _ __   ___ _   _ 
 |  _ \\| |/ _` | | |\\/| |/ _ \\| '_ \\ / _ \\ | | |
 | |_) | | (_| | | |  | | (_) | | | |  __/ |_| |
 |____/|_|\\__, | |_|  |_|\\___/|_| |_|\\___|\\__, |
     |  _ \\___/  _   _| | ___| |_| |_ ___ |___/ 
     | |_) / _ \\| | | | |/ _ \\ __| __/ _ \\      
     |  _ < (_) | |_| | |  __/ |_| ||  __/      
     |_| \\_\\___/ \\__,_|_|\\___|\\__|\\__\\___|                                                  
""")

while True:
    win = 0
    prediction_category = 0
    prediction = 0
    if highscore < coins:
        highscore = coins

    if coins <= 0:
        print('Out of money, you lose\n'
              f'You had a highscore of {highscore} Coins!')
        close = input('Press 9 to close')
        if close == '9':
            break

    print(f'Your balance is {coins} Coins\n'
          f'Your wager is {wager} Coins')
    prediction_category = input('1. Single\n'
                       '2. Dozen\n'
                       '3. Half\n'
                       '4. Column\n'
                       '5. Red or Black\n'
                       '6. Change Wager\n')

    print('')

    if prediction_category == '1':
        prediction = input('Enter a number: ')
        prediction = int(prediction)
        coins = coins - wager

    if prediction_category == '2':
        prediction = input('1. 1-12\n'
                           '2. 13-24\n'
                           '3. 25-36\n')
        coins = coins - wager

    if prediction_category == '3':
        prediction = input('1. 1-18\n'
                           '2. 19-36\n')
        coins = coins - wager

    if prediction_category == '4':
        prediction = input('1. Column 1 (1, 4, 7...)\n'
                           '2. Column 2 (2, 5, 8...)\n'
                           '3. Column 3 (3, 6, 9...)\n')
        coins = coins - wager

    if prediction_category == '5':
        prediction = input('1. Red\n'
                           '2. Black\n')
        coins = coins - wager

    if prediction_category == '6':
        wager_temp = input('Input your wager: ')
        wager_temp = int(wager_temp)
        if 0 < wager_temp <= coins:
            wager = wager_temp
            continue
        else:
            print('Invalid amount\n')

    if prediction_category == '1' or '2' or '3' or '4' or '5':
        color = random.choice(bank_color)
        if color == 'Red':
            number = random.choice(bank_red_number)
        if color == 'Black':
            number = random.choice(bank_black_number)
        if color == 'Green':
            number = random.choice(bank_green_number)

        print('\n'
            f'{color} {number}\n')

    if prediction_category == '1':
        if int(prediction) == number:
            win = (wager * 35) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')

    if prediction_category == '2':
        if prediction == '1' and 1 <= int(number) <= 12:
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '2' and 13 <= int(number) <= 24:
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '3' and 25 <= int(number) <= 36:
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')

    if prediction_category == '3':
        if prediction == '1' and 1 <= int(number) <= 18:
            win = wager * 2
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '2' and 19 <= int(number) <= 36:
            win = wager * 2
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')

    if prediction_category == '4':
        if prediction == '1' and (number == 1 or number == 4 or number == 7 or number == 10 or number == 13 or number == 16 or number == 19 or number == 22 or number == 25 or number == 28 or number == 31 or number == 34):
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '2' and (number == 2 or number == 5 or number == 8 or number == 11 or number == 14 or number == 17 or number == 20 or number == 23 or number == 26 or number == 29 or number == 32 or number == 35):
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '3' and (number == 3 or number == 6 or number == 9 or number == 12 or number == 15 or number == 18 or number == 21 or number == 24 or number == 27 or number == 30 or number == 33 or number == 36):
            win = (wager * 2) + wager
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')

    if prediction_category == '5':
        if prediction == '1' and (number == 1 or number == 3 or number == 5 or number == 7 or number == 9 or number == 12 or number == 14 or number == 16 or number == 18 or number == 21 or number == 23 or number == 25 or number == 27 or number == 28 or number == 30 or number == 32 or number == 34 or number == 36):
            win = wager * 2
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
        if prediction == '2' and (number == 2 or number == 4 or number == 6 or number == 8 or number == 10 or number == 11 or number == 13 or number == 15 or number == 17 or number == 19 or number == 20 or number == 22 or number == 24 or number == 26 or number == 29 or number == 31 or number == 33 or number == 35):
            win = wager * 2
            coins = coins + win
            print('Correct Prediction\n'
                  f'You win {win} Coins\n')
