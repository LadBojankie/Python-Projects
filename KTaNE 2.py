# This is sort of my magnum opus when it comes to my python projects. This is an unfinished puzzle game I made based on a game I really like called Keep Talking and Nobody Explodes.
# One person has a manual (which I'll also upload to the github) and the other person has the game, the goal is to figure out the puzzles by talking to eachother.
# The python version of the game remains unfinished because I wanted to move the project to Unity. Unfortunetly, that didn't happen because C# is a major pain to learn.

import tkinter as tk
import random

# Alpha     |   Coshfru
# Bravo     |   Test
# Charlie   |   Folder Grid
# Delta     |   Hidden Password (Wall of numbers,two windows,random length password)
# Echo      |   Command Typer
# Foxtrot   |   Firewall

#   To-Do List
# Add timer
# Serial Number Value
# Find and replace ',' with ','/' = ' with '='/' == ' with '='/' + ' with '+'/' - ' with '-'

winkey = 0
failkey = 0
awin = 0
bwin = 0
cwin = 0
TestWinCon = 0
TestWinCount = 0
TestWinBlock = 0
evenkey = 0
oddkey = 0
#-----------------------------------------------------------------------------------------------------------------------
def WinCheck():
    global winkey,Win
    if winkey == 1:
        Timer.destroy()

        Win = tk.Tk()
        Win.geometry('300x300')
        Win.title('Win')

        WinTitle = tk.Label(Win,text='Bomb Defused',font=('Courier New',15))
        WinMenu = tk.Button(Win,text='Back to Menu',width='20',command=WinRestart)

        WinTitle.pack(pady='10')
        WinMenu.pack(pady='5')

# Hardcore mode with fewer fails
# if hardcore == 1:
#   if failkey == 1:
def FailCheck():
    global failkey,Fail
    if failkey == 2:
        Timer.destroy()
        Fail = tk.Tk()
        Fail.geometry('300x300')
        Fail.title('Fail')

        FailTitle = tk.Label(Fail,text='Fail',font=('Courier New',15))
        FailMenu = tk.Button(Fail,text='Back to Menu',width='20',command=FailRestart)

        FailTitle.pack(pady='10')
        FailMenu.pack(pady='5')

        Fail.mainloop()
    else:
        failkey = failkey + 1
        FailCount.config(text=failkey)
#-----------------------------------------------------------------------------------------------------------------------
def Exit():
    Front.destroy()

def Start():
    global Timer,FailCount
    Front.destroy()

    Timer = tk.Tk() # Load Bearing Window
    Timer.geometry('200x200')
    Timer.title('Panel')

    FailTitle = tk.Label(Timer,text='Strikes')
    FailCount = tk.Label(Timer,text=failkey)

    FailTitle.pack()
    FailCount.pack(pady='5')

    Info = tk.Toplevel() # Info for other puzzles (Serial No.,etc.)
    Info.geometry('200x500')
    Info.title('Info')

    OSSet = ['Windows','Linux','SteamOS','MacOS','ChromeOS']
    OpSys = random.choice(OSSet)

    List = tk.Frame(Info)

    SerialTemp = '111111111'
    Serial = 'Serial No.: ' + SerialTemp

    SerialLabel = tk.Label(List,text=Serial,justify='left')
    SerialLabel.grid(row=0,column=0,padx=10,pady=1)
    SerialValue = 0
    Date = tk.Label(List,text='Date: 1/1/2025',justify='left')
    Date.grid(row=1,column=0,padx=10,pady=1)
    OS = tk.Label(List,text=('Operating System: ' + OpSys),justify='left')
    OS.grid(row=2,column=0,padx=10,pady=1)

    List.pack()

    ModSet = [1,2,4] # Replace with randint?, Is it possible to have two of the same?
    ModSpawn = random.choice(ModSet)
#-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFRU-COSHFR
    if ModSpawn == 1:
        def aSqu():
            UserKey1 = 1
            if UserKey1 == ColorKey:
                Coshfru2()
            else:
                FailCheck()

        def aCirc():
            UserKey1 = 2
            if UserKey1 == ColorKey:
                Coshfru2()
            else:
                FailCheck()

        def aTri():
            UserKey1 = 3
            if UserKey1 == ColorKey:
                Coshfru2()
            else:
                FailCheck()

        def aRhom():
            UserKey1 = 4
            if UserKey1 == ColorKey:
                Coshfru2()
            else:
                FailCheck()

        def Coshfru2():
            global Fruit,Word,Color
            FruitSet = ("Apple","Kiwi","Mango","Blueberry","Grape","Banana")
            Fruit = random.choice(FruitSet)
            CoshfruDict = {
                'Red': {'Apple':'Desk','Kiwi':'Your','Mango':'Ring','Blueberry':'Pterodactyl','Grape': 'Pickle','Banana':'Chez'},
                'Orange': {'Apple':'Scientist','Kiwi':'Yogurt','Mango':'Capybara','Blueberry':'Locker','Grape':'Peanut','Banana':'Victory'},
                'Yellow': {'Apple':'Music','Kiwi':'Personification','Mango':'Jose','Blueberry':'Crazy','Grape':'Curly','Banana':'Window'},
                'Green': {'Apple':'Clock','Kiwi':'Trypophobia','Mango':'Acid','Blueberry':'Ghost','Grape':'Tablet','Banana':'Anteater'},
                'Blue': {'Apple':'Perezosa','Kiwi':'Oxidation','Mango':'Shoes','Blueberry':'Toes','Grape':'Exit','Banana':'Dinosaur'},
                'Purple': {'Apple':'Skeleton','Kiwi':'Bow','Mango':'Encyclopedia','Blueberry': 'There','Grape':'Coral','Banana':'Biscuit'}
            }

            Word = (CoshfruDict[Color][Fruit])

            Coshfru2 = tk.Toplevel(Coshfru)
            Coshfru2.geometry('300x300')
            Coshfru2.title('Coshfru')

            global CoshfruEntry
            CoshfruFruit = tk.Label(Coshfru2, text=Fruit)
            CoshfruEntry = tk.Entry(Coshfru2)
            CoshfruButton = tk.Button(Coshfru2, text='Check', command=Coshfru2Check)

            CoshfruFruit.pack()
            CoshfruEntry.pack()
            CoshfruButton.pack()

        def Coshfru2Check():
            CoshfruUserEntry = CoshfruEntry.get()
            if CoshfruUserEntry == Word:
                CoshfruWin()
            else:
                FailCheck()

        def CoshfruWin():
            global awin, winkey
            if awin == 0:
                awin = 1
                winkey = winkey + 1
                WinCheck()

        global ColorKey,Color
        ColorSet = ("Red","Orange","Yellow","Green","Blue","Purple")
        ColorKeyDict = {"Red":1,"Orange":2,"Yellow":3,"Green":1,"Blue":2,"Purple":4}
        Color = random.choice(ColorSet)
        ColorKey = ColorKeyDict.get(Color)

        global Coshfru
        Coshfru = tk.Toplevel(Timer)
        Coshfru.geometry('300x300')
        Coshfru.title('Coshfru')

        def Light(event):
            Coshfru.config(background=Color)
            AlphaTitle.config(text=Color,background=Color)

        def Unlight(event):
            Coshfru.config(background="white")
            AlphaTitle.config(text='',background="white")

        AlphaTitle = tk.Label(Coshfru,text='',font=('Courier New',15))
        CoshfruReveal = tk.Button(Coshfru,text="Reveal",font=('Courier New',15))
        CoshfruReveal.bind("<ButtonPress>",Light)
        CoshfruReveal.bind("<ButtonRelease>",Unlight)
        AlphaButton = tk.Button(Coshfru,text='Click me!',command=CoshfruWin)

        AlphaButtons = tk.Frame(Coshfru)

        AlphaSquare = tk.Button(AlphaButtons,text="Square",font=('Ariel',15),command=aSqu)
        AlphaSquare.grid(row=0,column=0,sticky=tk.W + tk.E)
        AlphaCircle = tk.Button(AlphaButtons,text="Circle",font=('Ariel',15),command=aCirc)
        AlphaCircle.grid(row=0,column=1,sticky=tk.W + tk.E)
        AlphaTriangle = tk.Button(AlphaButtons,text="Triangle",font=('Ariel',15),command=aTri)
        AlphaTriangle.grid(row=1,column=0)
        AlphaRhombus = tk.Button(AlphaButtons,text="Rhombus",font=('Ariel',15),command=aRhom)
        AlphaRhombus.grid(row=1,column=1)

        AlphaTitle.pack(pady="5")
#        AlphaButton.pack()
        CoshfruReveal.pack(pady="3")
        AlphaButtons.pack(pady="5")
#-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADER-TEST-GRADE
    if ModSpawn == 2:
        def TestWin():
            global bwin, winkey
            if bwin == 0:
                bwin = 1
                winkey = winkey + 1
                WinCheck()

        def TestWinCheck():
            print(f'Win Check: Count: {TestWinCount},Con: {TestWinCon},Block: {TestWinBlock}')
            if TestWinCount == TestWinCon and TestWinBlock == 0:
                TestWin()

        def Test1Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(1) != T1R and T1.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(1) == T1R and T1.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test2Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(2) != T2R and T2.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(2) == T2R and T2.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test3Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(3) != T3R and T3.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(3) == T3R and T3.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test4Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(4) != T4R and T4.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(4) == T4R and T4.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test5Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(5) != T5R and T5.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(5) == T5R and T5.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test6Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(6) != T6R and T6.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(1) == T6R and T6.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test7Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(7) != T7R and T7.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(7) == T7R and T7.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        def Test8Check():
            global TestWinCount, TestWinBlock
            if TestCheckDict.get(8) != T8R and T8.get() == 1:
                TestWinCount = TestWinCount + 1
                TestWinCheck()
            elif TestCheckDict.get(8) == T8R and T8.get() == 0:
                TestWinBlock = TestWinBlock - 1
                TestWinCheck()
            else:
                FailCheck()
                TestWinBlock = TestWinBlock + 1

        global TestCheckDict
        if OpSys == "SteamOS" or OpSys == 'MacOS' or OpSys == 'ChromeOS':
            if SerialValue <= 15:
                TestCheckDict = {1:'B',2:'A',3:'D',4:'C',5:'B',6:'D',7:'C',8:'D'}
            else:
                TestCheckDict = {1:'A',2:'D',3:'A',4:'C',5:'D',6:'A',7:'C',8:'B'}
        else:
            if SerialValue <= 15:
                TestCheckDict = {1:'D',2:'A',3:'B',4:'C',5:'A',6:'A',7:'B',8:'A'}
            else:
                TestCheckDict = {1:'C',2:'D',3:'A',4:'C',5:'B',6:'B',7:'B',8:'C'}

        TestAnswerSet = ('A','B','C','D')
        global T1R,T2R,T3R,T4R,T5R,T6R,T7R,T8R
        T1R = random.choice(TestAnswerSet)
        T2R = random.choice(TestAnswerSet)
        T3R = random.choice(TestAnswerSet)
        T4R = random.choice(TestAnswerSet)
        T5R = random.choice(TestAnswerSet)
        T6R = random.choice(TestAnswerSet)
        T7R = random.choice(TestAnswerSet)
        T8R = random.choice(TestAnswerSet)

        global TestWinCon
        if T1R != TestCheckDict.get(1):
            TestWinCon = TestWinCon + 1
        if T2R != TestCheckDict.get(2):
            TestWinCon = TestWinCon + 1
        if T3R != TestCheckDict.get(3):
            TestWinCon = TestWinCon + 1
        if T4R != TestCheckDict.get(4):
            TestWinCon = TestWinCon + 1
        if T5R != TestCheckDict.get(5):
            TestWinCon = TestWinCon + 1
        if T6R != TestCheckDict.get(6):
            TestWinCon = TestWinCon + 1
        if T7R != TestCheckDict.get(7):
            TestWinCon = TestWinCon + 1
        if T8R != TestCheckDict.get(8):
            TestWinCon = TestWinCon + 1

        global Test
        Test = tk.Toplevel(Timer)
        Test.geometry('300x300')
        Test.title('Test Grader')

        Sheet = tk.Frame(Test)

        BravoButton = tk.Button(Test,text='Click me!',command=TestWin)

        global T1,T2,T3,T4,T5,T6,T7,T8 # Left
        T1 = tk.IntVar()
        T2 = tk.IntVar()
        T3 = tk.IntVar()
        T4 = tk.IntVar()
        Test1 = tk.Checkbutton(Sheet,text=T1R,variable=T1,command=Test1Check)
        Test1.grid(row=0,column=0,padx=10,pady=10)
        Test2 = tk.Checkbutton(Sheet,text=T2R,variable=T2,command=Test2Check)
        Test2.grid(row=1,column=0,padx=10,pady=10)
        Test3 = tk.Checkbutton(Sheet,text=T3R,variable=T3,command=Test3Check)
        Test3.grid(row=2,column=0,padx=10,pady=10)
        Test4 = tk.Checkbutton(Sheet,text=T4R,variable=T4,command=Test4Check)
        Test4.grid(row=3,column=0,padx=10,pady=10)

        T5 = tk.IntVar() # Right
        T6 = tk.IntVar()
        T7 = tk.IntVar()
        T8 = tk.IntVar()
        Test5 = tk.Checkbutton(Sheet,text=T5R,variable=T5,command=Test5Check)
        Test5.grid(row=0,column=1,padx=10,pady=10)
        Test6 = tk.Checkbutton(Sheet,text=T6R,variable=T6,command=Test6Check)
        Test6.grid(row=1,column=1,padx=10,pady=10)
        Test7 = tk.Checkbutton(Sheet,text=T7R,variable=T7,command=Test7Check)
        Test7.grid(row=2,column=1,padx=10,pady=10)
        Test8 = tk.Checkbutton(Sheet,text=T8R,variable=T8,command=Test8Check)
        Test8.grid(row=3,column=1,padx=10,pady=10)

        BravoButton.pack()
        Sheet.pack()
#-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRID-FOLDER-GRI
    if ModSpawn == 3:
        Folder = tk.Toplevel(Timer)
        Folder.geometry('300x300')
        Folder.title('Folder Grid')
#-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN-PASSWORD-HIDDEN
    if ModSpawn == 4:
        def PassWinCheck():
            if PassEntry.get() == PassCheck:
                global cwin,winkey
                if cwin == 0:
                    cwin = 1
                    winkey = winkey + 1
                    WinCheck()
            else:
                FailCheck()

        NumSet = [4,5,5,5,6,6,7,7,8]
        PassPath = random.choice(NumSet)

        Pass1 = ''
        Pass2 = ''
        Pass3 = ''
        Pass4 = ''
        Pass5 = ''
        Pass6 = ''
        Pass7 = ''
        Pass8 = ''

        for i in range(PassPath):
            Pass1 += str(random.randint(0,9))
            Pass2 += str(random.randint(0,9))
            Pass3 += str(random.randint(0,9))
            Pass4 += str(random.randint(0,9))
            Pass5 += str(random.randint(0,9))
            Pass6 += str(random.randint(0,9))
            Pass7 += str(random.randint(0,9))
            Pass8 += str(random.randint(0,9))

        Password = tk.Toplevel(Timer)
        Password.geometry('300x300')
        Password.title('Hidden Password')

        PassL1 = tk.Label(Password,text=Pass1)
        PassL2 = tk.Label(Password,text=Pass2)
        PassL3 = tk.Label(Password,text=Pass3)
        PassL4 = tk.Label(Password,text=Pass4)
        PassL5 = tk.Label(Password,text=Pass5)
        PassL6 = tk.Label(Password,text=Pass6)
        PassL7 = tk.Label(Password,text=Pass7)
        PassL8 = tk.Label(Password,text=Pass8)
        PassEntry = tk.Entry(Password)
        PassButton = tk.Button(Password,text='Enter',command=PassWinCheck)

        if PassPath == 4:
            if Pass1[0] == '8':
                PassCheck = Pass8
            elif 10 < sum([int(i) for i in Pass5]) < 20:
                PassCheck = Pass2
            elif sum([int(i) for i in Pass2]) % 2:
                PassCheck = Pass3
            else:
                PassCheck = Pass4

        if PassPath == 5:
            if sum([int(i) for i in Pass7]) % 2 == 0:
                PassCheck = Pass1
            elif int(Pass8[2]) % 2 == 0:
                PassCheck = Pass6
            elif sum([int(i) for i in Pass5]) > SerialValue:
                PassCheck = Pass3
            elif Pass4[0] == '7' or Pass4[1] == '7' or Pass4[2] == '7' or Pass4[3] == '7' or Pass4[4] == '7':
                PassCheck = Pass5
            else:
                PassCheck = Pass7

        if PassPath == 6:
            if sum([int(i) for i in Pass7]) > 23:
                PassCheck = Pass3
            elif sum([int(i) for i in Pass5[0]]) % 2 or sum([int(i) for i in Pass2[2]]) % 2:
                PassCheck = Pass7
            elif sum([int(i) for i in Pass4]) % 2:
                PassCheck = Pass8
            elif sum([int(i) for i in Pass6]) % 2:
                PassCheck = Pass1
            else:
                PassCheck = Pass2

        if PassPath == 7:
            if Pass7[3] == '3' or Pass7[3] == '5' or Pass7[3] == '7':
                PassCheck = Pass1
            elif sum([int(i) for i in Pass4]) % 2 == 0:
                PassCheck = Pass4
            elif Pass6[0] <  Pass1[5]:
                PassCheck = Pass8
            elif sum([int(i) for i in Pass2[1]]) % 2:
                PassCheck = Pass3
            else:
                PassCheck = Pass6

        if PassPath == 8:
            if Pass8[0] < Pass6[3]:
                PassCheck = Pass3
            elif sum([int(i) for i in Pass2]) % 2 == 0:
                PassCheck = Pass6
            elif sum([int(i) for i in Pass1]) == 36 or sum([int(i) for i in Pass2]) == 36 or sum([int(i) for i in Pass3]) == 36 or sum([int(i) for i in Pass4]) == 36 or sum([int(i) for i in Pass5]) == 36 or sum([int(i) for i in Pass6]) == 36 or sum([int(i) for i in Pass7]) == 36 or sum([int(i) for i in Pass8]) == 36:
                PassCheck = Pass7
            elif Pass7[0] == '1' or Pass7[0] == '4' or Pass7[0] == '6' or Pass7[0] == '8' or Pass7[0] == '9':
                PassCheck = Pass8
            elif sum([int(i) for i in Pass4]) > sum([int(i) for i in Pass8]):
                PassCheck = Pass2
            elif Pass5[4] == '3':
                PassCheck = Pass1
            else:
                PassCheck = Pass1
#        print(PassCheck)

        PassL1.pack()
        PassL2.pack()
        PassL3.pack()
        PassL4.pack()
        PassL5.pack()
        PassL6.pack()
        PassL7.pack()
        PassL8.pack()
# Add a gap here
        PassEntry.pack()
        PassButton.pack()
#-----------------------------------------------------------------------------------------------------------------------
    Timer.mainloop()
#-----------------------------------------------------------------------------------------------------------------------
def WinRestart():
    global winkey,awin,bwin,cwin,failkey,TestWinCon,TestWinCount,TestWinBlock
    winkey = 0
    awin = 0
    bwin = 0
    cwin = 0
    failkey = 0
    TestWinCon = 0
    TestWinCount = 0
    TestWinBlock = 0
    Win.destroy()
    Main()

def FailRestart():
    global winkey,awin,bwin,cwin,failkey,TestWinCon,TestWinCount,TestWinBlock
    winkey = 0
    awin = 0
    bwin = 0
    cwin = 0
    failkey = 0
    TestWinCon = 0
    TestWinCount = 0
    TestWinBlock = 0
    Fail.destroy()
    Main()
#-----------------------------------------------------------------------------------------------------------------------
def Main():
    global Front
    Front = tk.Tk()
    Front.geometry("500x500")
    Front.title("Defusal Game")

    FrontTitle = tk.Label(Front,text="Defusal Game",justify='center',font=('Courier New',15))
    FrontStart = tk.Button(Front,text='Start',width='20',command=Start)
    FrontClose = tk.Button(Front,text='Exit',width='20',command=Exit)

    FrontTitle.pack(pady='10')
    FrontStart.pack(pady='5')
    FrontClose.pack(pady='5')

    Front.mainloop()

Main()
