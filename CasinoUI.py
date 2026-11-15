# This is a work in-progress of a collection of casino/gambling games. I made it as an excuse to get more practice with
# tkinter, and as an opportunity to revamp my older casino games. I was focusing more on functionality before making it
# look good, so the UI is still a little barebones, but the two games that are currently implemented, Slots and Horse
# Racing, work well.

import tkinter as tk
import random
# import time

# Craps
# Three Card Poker
# Plinko
# Coin count changing in real time

coins = 100
highscore = 100
bidAct = 10

def bridge(game):
    game.destroy()
    main()

def bidCheck(bid,warn):
    global bidAct

    bidTemp = int(bid.get())
    if bidTemp > coins:
        warn.config(text="Your bid is higher than your current amount of Coins")
    elif bidTemp <= 0:
        warn.config(text="Your bid must be higher than 0")
    else:
        bidAct = bidTemp
        warn.config(text=f"Bid: {bidAct} Coins")

def loseCheck(win,game,warn):
    global coins,bidAct,highscore

    if game == slots:
        win.config(text="Lose")
    elif game == horse:
        win.config(text=f"The winner is {horseWinner}!")
    coins -= bidAct
    if coins <= 0:
        loseCon(game)
    elif bidAct > coins:
        bidAct = coins
        warn.config(text=f"Bid: {bidAct} Coins")
    if coins > highscore:
        highscore = coins

def loseCon(game):
    global lose
    game.destroy()

    lose = tk.Tk()
    lose.geometry("500x500")
    lose.title("Lose")

    loseTitle = tk.Label(lose, text="You Lose!")
    loseHigh = tk.Label(lose, text=f"You had a high score of {highscore} Coins!")
    loseRestart = tk.Button(lose, text="Play Again?", command=restart)

    loseTitle.pack()
    loseHigh.pack()
    loseRestart.pack()

    lose.mainloop()

def restart():
    global coins,highscore
    lose.destroy()

    coins = 100
    highscore = 100

    main()
#-----------------------------------------------------------------------------------------------------------------------
slotsList = ['Bullets', 'Knife', 'Pistol', 'Shotgun', 'SMG', 'Carbine', 'Rifle', 'Grenade', 'Atom Bomb']

def slotsSpin():
    global coins,highscore,bidAct

    for i in range(5):
        slotsOneRand = random.choice(slotsList)
        slotsTwoRand = random.choice(slotsList)
        slotsThreeRand = random.choice(slotsList)

        slotsOne.config(text=slotsOneRand)
        slotsTwo.config(text=slotsTwoRand)
        slotsThree.config(text=slotsThreeRand)
#        time.sleep(.2)

    slotsOneRand = random.choice(slotsList)
    slotsTwoRand = random.choice(slotsList)
    slotsThreeRand = random.choice(slotsList)

    slotsOne.config(text=slotsOneRand)
    slotsTwo.config(text=slotsTwoRand)
    slotsThree.config(text=slotsThreeRand)

    if slotsOneRand == 'Atom Bomb' and slotsTwoRand == 'Atom Bomb' and slotsThreeRand == 'Atom Bomb':
        slotsWin.config(text="Jackpot! You win " + str(bidAct * 100) + " Coins!")
        coins += bidAct * 100
    elif slotsOneRand == slotsTwoRand == slotsThreeRand:
        slotsWin.config(text="Three of a Kind! You win " + str(bidAct * 10) + " Coins!")
        coins += bidAct * 10
    elif slotsOneRand == slotsTwoRand or slotsOneRand == slotsThreeRand or slotsTwoRand == slotsThreeRand:
        slotsWin.config(text="Pair! You win " + str(bidAct * 3) + " Coins!")
        coins += bidAct * 3
    else:
        loseCheck(slotsWin,slots,slotsWarn)

    slotsMoney.config(text=f"You have {coins} Coins")

def slotsOpen():
    global slots,coins,slotsOne,slotsTwo,slotsThree,slotsBid,slotsWarn,slotsWin,slotsMoney

    root.destroy()

    slots = tk.Tk()
    slots.geometry("500x500")
    slots.title("Big Money Slots")

    slotsTitle = tk.Label(slots, text="Big Money Slots")
    slotsMoney = tk.Label(slots, text=f"You have {coins} Coins")

    slotsOne = tk.Label(slots, text="")
    slotsTwo = tk.Label(slots, text="")
    slotsThree = tk.Label(slots, text="")
    slotsWin = tk.Label(slots, text="")

    slotsWarn = tk.Label(slots, text=f"Bid: {bidAct} Coins")
    slotsWage = tk.Frame(slots)
    slotsBid = tk.Entry(slotsWage, width='10')
    slotsBid.grid(row=0,column=0)
    slotsSubmit = tk.Button(slotsWage, text='Set Bid', width='10', command=lambda: bidCheck(slotsBid,slotsWarn))
    slotsSubmit.grid(row=0,column=1)
    slotsPlay = tk.Button(slots, text='Spin', command=slotsSpin)

    slotsBack = tk.Button(slots, text='Home', width='20', command=lambda: bridge(slots))

    slotsTitle.pack(pady='10')
    slotsMoney.pack()
    slotsOne.pack()
    slotsTwo.pack()
    slotsThree.pack()
    slotsWin.pack()
    slotsWarn.pack(pady='5')
    slotsWage.pack(pady='5')
    slotsPlay.pack()
    slotsBack.pack(pady='10')

    slots.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
horseNameList = ['Agnes Tachyon','Haru Urara','Manhattan Cafe','Gold Ship','Diawa Scarlet','Daitaku Helios','Oguri Cap',
             'Rice Shower','Special Week','Matikanetannhauser','Silence Suzuka','El Condor Pasa','Vodka','Taiki Shuttle',
             'Sakura Bakushin O',"Bullet'n Board",'Superstitional Realism','Door Knob','Oob','Jovial Merryment',
             'Lightning Strikes Thrice','Downtown Skybox','Resolute Mind Afternoon','Comely Material Morning',
             'Ten Question Marks','D-Horse']

horseDistDict = {0:'|----------',
                 1:'-|---------',
                 2:'--|--------',
                 3:'---|-------',
                 4:'----|------',
                 5:'-----|-----',
                 6:'------|----',
                 7:'-------|---',
                 8:'--------|--',
                 9:'---------|-',
                 10:'----------|'}

horseKey = 0

def horseRace(x):
    global coins,horseMoney,bidAct,highscore,horseWinner

    horseDistOne = 0
    horseDistTwo = 0
    horseDistThree = 0
    horseDistFour = 0
    horseWinCon = False
    horseWinner = ''

    horseContenders = {1:horseDistOne,
                       2:horseDistTwo,
                       3:horseDistThree,
                       4:horseDistFour}

    horseTrackDict = {1:horseTrackOne,
                 2:horseTrackTwo,
                 3:horseTrackThree,
                 4:horseTrackFour}
    
    horseNameDict = {1:horseNameOne,
                     2:horseNameTwo,
                     3:horseNameThree,
                     4:horseNameFour}
    
    while not horseWinCon:
        horseMove = random.randint(1,4)
        horseContenders[horseMove] += 1
        horseTrackDict.get(horseMove).config(text=horseDistDict.get(horseContenders[horseMove]))
        if horseContenders[horseMove] == 10:
            horseWinCon = True
            horseWinner = horseNameDict.get(horseMove)
        print(horseMove, horseContenders[horseMove])
        print(horseContenders)
#        time.sleep(.5)

    if horseWinner == x:
        coins += bidAct * 4
        horseWin.config(text=f'The winner is {horseWinner}! You won ' + str(bidAct * 4) + ' Coins!')
    else:
        loseCheck(horseWin,horse,horseWarn)

    horseMoney.config(text=f"You have: {coins} Coins!")

def horseCycle():
    global horseNameOne,horseNameTwo,horseNameThree,horseNameFour,horseKey

    horseNameOne = random.choice(horseNameList)
    horseNameList.remove(horseNameOne)
    horseNameTwo = random.choice(horseNameList)
    horseNameList.remove(horseNameTwo)
    horseNameThree = random.choice(horseNameList)
    horseNameList.remove(horseNameThree)
    horseNameFour = random.choice(horseNameList)
    horseNameList.append(horseNameOne)
    horseNameList.append(horseNameTwo)
    horseNameList.append(horseNameThree)

    horseKey = horseKey + 1

def horseOpen():
    global coins,horse,horseMoney,horseTrackOne,horseTrackTwo,horseTrackThree,horseTrackFour,horseWin,horseWarn

    if horseKey == 0:
        horseCycle()

    root.destroy()

    horse = tk.Tk()
    horse.geometry("800x500")
    horse.title("Big Money Horse Racing")

    horseTitle = tk.Label(horse, justify='left', text="Big Money Horse Racing")
    horseMoney = tk.Label(horse, justify='left', text=f"You have: {coins} Coins!")

    horseCourse = tk.Frame(horse)

    horsePenOne = tk.Label(horseCourse, justify='center', width='20', text=horseNameOne)
    horsePenOne.grid(row=0,column=0)
    horsePenTwo = tk.Label(horseCourse, justify='center', width='20', text=horseNameTwo)
    horsePenTwo.grid(row=1,column=0)
    horsePenThree = tk.Label(horseCourse, justify='center', width='20', text=horseNameThree)
    horsePenThree.grid(row=2,column=0)
    horsePenFour = tk.Label(horseCourse, justify='center', width='20', text=horseNameFour)
    horsePenFour.grid(row=3,column=0)

    horseTrackOne = tk.Label(horseCourse, justify='center', width='30', text="|----------")
    horseTrackOne.grid(row=0,column=1)
    horseTrackTwo = tk.Label(horseCourse, justify='center', width='30',text="|----------")
    horseTrackTwo.grid(row=1,column=1)
    horseTrackThree = tk.Label(horseCourse, justify='center', width='30',text="|----------")
    horseTrackThree.grid(row=2,column=1)
    horseTrackFour = tk.Label(horseCourse, justify='center', width='30',text="|----------")
    horseTrackFour.grid(row=3,column=1)

    horseWin = tk.Label(horse, text='')
    horseWarn = tk.Label(horse, text=f"Bid: {bidAct} Coins")
    horseWage = tk.Frame(horse)
    horseBidOne = tk.Button(horseWage, width='20', text=horseNameOne, command=lambda: horseRace(horseNameOne))
    horseBidOne.grid(row=0,column=0)
    horseBidTwo = tk.Button(horseWage, width='20', text=horseNameTwo, command=lambda: horseRace(horseNameTwo))
    horseBidTwo.grid(row=0,column=1)
    horseBidThree = tk.Button(horseWage, width='20', text=horseNameThree, command=lambda: horseRace(horseNameThree))
    horseBidThree.grid(row=0,column=2)
    horseBidFour = tk.Button(horseWage, width='20', text=horseNameFour, command=lambda: horseRace(horseNameFour))
    horseBidFour.grid(row=0,column=3)
    horseBid = tk.Entry(horseWage, width='10')
    horseBid.grid(row=1, column=1)
    horseSubmit = tk.Button(horseWage, text='Set Bid', width='10', command=lambda: bidCheck(horseBid,horseWarn))
    horseSubmit.grid(row=1, column=2)

    horseBack = tk.Button(horse, text='Home', width='20', command=lambda: bridge(horse))

    horseTitle.pack(pady='20')
    horseMoney.pack(pady='20')
    horseCourse.pack(pady='10')
    horseWin.pack(pady='10')
    horseWarn.pack(pady='10')
    horseWage.pack(pady='10')
    horseBack.pack(pady='10')
#-----------------------------------------------------------------------------------------------------------------------
def rouletteOpen():
    root.destroy()

    roulette = tk.Tk()
    roulette.geometry('500x500')
    roulette.title('Big Money Roulette')

#-----------------------------------------------------------------------------------------------------------------------
def main():
    global root,coins,highscore

    root = tk.Tk()
    root.geometry("500x500")
    root.title("Lad Bojankie's Big Money Casino")

    rootTitle = tk.Label(root, justify='left', text="Lad Bojankie's Big Money Casino")
    rootMoney = tk.Label(root, justify='left', text=f"You have: {coins} Coins!")

    rootSlots = tk.Button(root, text='Slots', width='20', command=slotsOpen)
    rootRoulette = tk.Button(root, text='Roulette', width='20', command=rouletteOpen)
    rootBlackjack = tk.Button(root, text='Blackjack', width='20')
    rootHorse = tk.Button(root, text='Horse Races', width='20', command=horseOpen)

    rootExit = tk.Button(root, text='Exit', width='20', command=exit)

    rootTitle.pack(pady='20')
    rootMoney.pack(pady='20')
    rootSlots.pack(pady='5')
    rootRoulette.pack(pady='5')
    rootBlackjack.pack(pady='5')
    rootHorse.pack(pady='5')
    rootExit.pack(pady='10')

    root.mainloop()

main()