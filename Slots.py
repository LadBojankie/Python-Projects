import random

highscore = 100
win = 0
wager = 1
coins = 100
bank_1 = ['Lemon', 'Cherry', 'Diamond', 'Seven', 'Bell', 'Bar', 'Double Bar', 'Triple Bar']
bank_2 = ['Lemon', 'Cherry', 'Diamond', 'Seven', 'Bell', 'Bar', 'Double Bar', 'Triple Bar']
bank_3 = ['Lemon', 'Cherry', 'Diamond', 'Seven', 'Bell', 'Bar', 'Double Bar', 'Triple Bar']
jackpots = ["""                                                                
     ,--.  ,---.   ,-----.,--. ,--.,------.  ,-----. ,--------. 
     |  | /  O  \\ '  .--./|  .'   /|  .--. ''  .-.  ''--.  .--' 
,--. |  ||  .-.  ||  |    |  .   ' |  '--' ||  | |  |   |  |    
|  '-'  /|  | |  |'  '--'\\|  |\\   \\|  | --' '  '-'  '   |  |    
 `-----' `--' `--' `-----'`--' '--'`--'      `-----'    `--'    
""", """
     ___  _______  _______  ___   _  _______  _______  _______ 
    |   ||   _   ||       ||   | | ||       ||       ||       |
    |   ||  |_|  ||       ||   |_| ||    _  ||   _   ||_     _|
    |   ||       ||       ||      _||   |_| ||  | |  |  |   |  
 ___|   ||       ||      _||     |_ |    ___||  |_|  |  |   |  
|       ||   _   ||     |_ |    _  ||   |    |       |  |   |  
|_______||__| |__||_______||___| |_||___|    |_______|  |___|  
""", """
_________ _______  _______  _        _______  _______ _________
\\__    _/(  ___  )(  ____ \\| \\    /\\(  ____ )(  ___  )\\__   __/
   )  (  | (   ) || (    \\/|  \\  / /| (    )|| (   ) |   ) (   
   |  |  | (___) || |      |  (_/ / | (____)|| |   | |   | |   
   |  |  |  ___  || |      |   _ (  |  _____)| |   | |   | |   
   |  |  | (   ) || |      |  ( \\ \\ | (      | |   | |   | |   
|\\_)  )  | )   ( || (____/\\|  /  \\ \\| )      | (___) |   | |   
(____/   |/     \\|(_______/|_/    \\/|/       (_______)   )_(   
""", """
     .-./`)     ____        _______   .--.   .--.  .-------.     ,-----.  ,---------.  
     \\ '_ .') .'  __ `.    /   __  \\  |  | _/  /   \\  _(`)_ \\  .'  .-,  '.\\          \\ 
    (_ (_) _)/   '  \\  \\  | ,_/  \\__) | (`' ) /    | (_ o._)| / ,-.|  \\ _ \\`--.  ,---' 
      / .  \\ |___|  /  |,-./  )       |(_ ()_)     |  (_,_) /;  \\  '_ /  | :  |   \\    
 ___  |-'`|     _.-`   |\\  '_ '`)     | (_,_)   __ |   '-.-' |  _`,/ \\ _/  |  :_ _:    
|   | |   '  .'   _    | > (_)  )  __ |  |\\ \\  |  ||   |     : (  '\\_/ \\   ;  (_I_)    
|   `-'  /   |  _( )_  |(  .  .-'_/  )|  | \\ `'   /|   |      \\ `"/  \\  ) /  (_(=)_)   
 \\      /    \\ (_ o _) / `-'`-'     / |  |  \\    / /   )       '. \\_/``".'    (_I_)    
  `-..-'      '.(_,_).'    `._____.'  `--'   `'-'  `---'         '-----'      '---'    
"""]

print("""
   ___ _        __  __                          
  | _ |_)__ _  |  \\/  |___ _ _  ___ _  _        
  | _ \\ / _` | | |\\/| / _ \\ ' \\/ -_) || |       
  |___/_\\__, | |_|  |_\\___/_||_\\___|\\_, |       
 ___ _  |___/    __  __         _   |__/        
/ __| |___| |_  |  \\/  |__ _ __| |_ (_)_ _  ___ 
\\__ \\ / _ \\  _| | |\\/| / _` / _| ' \\| | ' \\/ -_)
|___/_\\___/\\__| |_|  |_\\__,_\\__|_||_|_|_||_\\___|
""")

while True:
    win = 0
    key = 0
    key_crazy = 0
    if highscore < coins:
        highscore = coins

    if coins <= 0:
        print('Out of money, you lose\n'
              f'You had a highscore of {highscore} Coins!')
        close = input('Press 9 to close')
        if close == '9':
            break

    print(f'\n'
          f'Your balance is {coins} Coins\n'
          f'Your wager is {wager} Coins')
    spin = input('Press enter to spin, or press 1 to change your wager')

    if spin == '1':
        wager_temp = input('Input your wager: ')
        wager_temp = int(wager_temp)
        if 0 < wager_temp <= coins:
            wager = wager_temp
            print('\n')
            continue
        else:
            print('Invalid amount\n'
                  '\n')

    if spin == '' and coins > 0:
        coins = coins - wager

        crazy = random.randint(1, 1000)
        if crazy == 13:
            print("""
              ____    ____  ________    ______       _                   
             |_   \\  /   _||_   __  | .' ___  |     / \\                  
               |   \\/   |    | |_ \\_|/ .'   \\_|    / _ \\                 
               | |\\  /| |    |  _| _ | |   ____   / ___ \\                
              _| |_\\/_| |_  _| |__/ |\\ `.___]  |_/ /   \\ \\_              
             |_____||_____||________| `._____.'|____| |____|             
    _____     _        ______  ___  ____   _______     ___    _________  
   |_   _|   / \\     .' ___  ||_  ||_  _| |_   __ \\  .'   `. |  _   _  | 
     | |    / _ \\   / .'   \\_|  | |_/ /     | |__) |/  .-.  \\|_/ | | \\_| 
 _   | |   / ___ \\  | |         |  __'.     |  ___/ | |   | |    | |     
| |__' | _/ /   \\ \\_\\ `.___.'\\ _| |  \\ \\_  _| |_    \\  `-'  /   _| |_    
`.____.'|____| |____|`.____ .'|____||____||_____|    `.___.'   |_____|                                                                           
            \n"""
                  'The slot machine starts blaring sirens, strobing lights, and shaking rapidly.\n'
                  'YOU WON 1 MILLION COINS!!!')
            coins = coins + wager + 1000000
            key_crazy = 1
        if crazy == 1000:
            print('The machine bursts into flames before exploding, the casino forces you to pay for the damages.\n'
                  'You lost all your coins.')
            coins = 0
            key_crazy = 1

        slot_1 = random.choice(bank_1)
        slot_2 = random.choice(bank_2)
        slot_3 = random.choice(bank_3)

        if key_crazy == 0:
            print(f'''
            {slot_1}
            {slot_2}
            {slot_3}
            ''')

        if key == 0 and key_crazy == 0:
            if slot_1 == 'Diamond' and slot_2 == 'Diamond' and slot_3 == 'Diamond':
                jackpot_message = random.choice(jackpots)
                win = wager * 100
                print(f"{jackpot_message}")
                print(f'You won {win} Coins!')
                coins = coins + win
                key = 1

        if key == 0 and key_crazy == 0:
            if slot_1 == slot_2 and slot_1 == slot_3 and slot_2 == slot_3:
                win = wager * 10
                print('Three of a Kind\n'
                      f'You won {win} Coins!')
                coins = coins + win
                key = 1

        if key == 0 and key_crazy == 0:
            if slot_1 == slot_2 or slot_1 == slot_3 or slot_2 == slot_3:
                win = wager * 3
                print('Pair\n'
                      f'You won {win} Coins!')
                coins = coins + win
                key = 1