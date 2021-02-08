from random import randint

def menu():
    print('If you want to play the game mastermind press 0')
    print('If you want to try the random strategy algorithm to see how efficient it works press 1')
    print('If you want to try the simple strategy algorithm to see how it performs press 2')
    press = int(input(''))
    generate(press)

#*** probeer de for loops te verminderen | ook meer annotations bij complexe codes***    
def makeguesslist(exclude = '',include=''):
    colorlist = []

    for color in colordict.values():
        if exclude !=' ':
            if color not in exclude:
                colorlist.append(color)
        elif include != ' ':
            if color in include:
                colorlist.append(color)

    guesslist = []
    for i0 in range(len(colorlist)):
        for i1 in range(len(colorlist)):
            for i2 in range(len(colorlist)):
                for i3 in range(len(colorlist)):
                    guesslist.append([colorlist[i0],colorlist[i1],colorlist[i2],colorlist[i3]])
    return guesslist

#*** probeer spaties tussen codes te zetten zodat het makkelijker te lezen is | ook meer annotations bij complexe codes  ***    
def generate(press):
    '''generates a random set of four letters representing colors'''
    global colordict
    colordict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
    playercode = ''
    for i in range(4):
        playercode += colordict[int(randint(0,5))]

    guesslist = makeguesslist()


    if press == 0:

        while True:
            print('Guess a 4 letter code of the first 6 letters of the alphabet')
            while True:
                playerguess = input('\t\t').upper()
                if len(playerguess) > 4:
                    print('too long try again')
                # elif playerguess not in colordict.values():
                #     print('enter a combination of \'A B C D E F\'')
                else:
                    break
            print(guess(playercode,playerguess))

    #print(press)

    elif press ==1:
        randomguess_strategy(playercode,guesslist)

    #print(press)

    elif press == 2:
        simple_strategy(playercode,guesslist)

# line 103, probeer die if statement in 2 te delen | ook meer annotations bij complexe codes
def guess(code,  playerguess ):
    '''lets the player guess and returns amount of white and black pins'''

    pins = {'black':0,'white':0}
    dct = {0:True,1:True,2:True,3:True}
    lst = []
    blacklist = []


    if playerguess == code:
        print('congrats you won')

    i=0
    while i < len(playerguess):
        if playerguess[i] == code[i]:
            pins['black'] +=1
            dct[i] = False

        i+=1

    for k,v in dct.items():
        lst.append(k)
        lst.append(v)

    for i in range(1,len(lst),2):
        if not lst[i]:
            blacklist.append(lst[i-1])

    playerindex = 0
    whitelist = []
    while playerindex < len(playerguess):
        #print('playerguess [playerindex] ',playerguess[playerindex])           [A,B,A,B]   gok = [B,F,F,F]
        codeindex =0
        if dct[playerindex]:

            while playerguess[playerindex] in code and codeindex <len(code):
                if playerguess[playerindex] == code[codeindex] and  codeindex not in blacklist and codeindex not in whitelist:
                    pins['white'] +=1
                    whitelist.append(codeindex)
                    break
                codeindex+=1
        playerindex+=1


    # print('blacklist',blacklist)
    # print('whitelist',whitelist)
    # print('pins',pins)
    return (pins['black'],pins['white'])

    #return guess(code,playerguess,amount_guess)

# meer annotations bij complexe codes voor lezers
def randomguess_strategy(code,guesslist):
    '''algoritm to solve mastermind game'''
    amountguessedlist = []
    for i in range(100):
        amountguessed =0
        while True:
            g = guess(code,guesslist[int(randint(0,len(guesslist)-1))])
            if g[0] == 4:
                amountguessedlist.append(amountguessed)
                break
            amountguessed +=1
    total = 0
    for amountguessed in amountguessedlist:
        total +=amountguessed

    print(total/len(amountguessedlist),'tries on average when tested a 100 times')

# meer enters tussen je code zodat het meer leesbaar is
def simple_strategy(code,guesslist):
    '''algoritm to solve mastermind game'''
    amountguessedlist = []
    mogelijke_feedback = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]
    mogelijke_combinaties=makeguesslist
    mogelijke_oplossingen=makeguesslist
    for j in range(3):
        for i in range(1000):
            amountguessed =0
            while True:
                guessed =guesslist[int(randint(0,len(guesslist)-1))]
                g = guess(code,guessed)
                #
                # for comb in mogelijke_combinaties:
                #     for oplossing in mogelijke_oplossingen:
                #         for feedback in mogelijke_feedback:
                #             if guess(comb, oplossing) == feedback:
                #                 mogelijke_oplossingen.append(comb)


                if g == (0,0):
                    guesslist=makeguesslist(guessed,' ')

                if g ==(1,3) or g ==(2,2):
                    guesslist=makeguesslist(' ',guessed)
                if g[0] == 4:
                    amountguessedlist.append(amountguessed)
                    break
                amountguessed +=1
        total = 0
        for amountguessed in amountguessedlist:
            total +=amountguessed
        print(total/len(amountguessedlist),'tries on average when tested a 1000 times')
    print(code)

def looking_ahead():
    '''algoritm to solve mastermind game'''


def worst_case():
    '''algoritm to solve mastermind game'''


def expected_size():
    '''algoritm to solve mastermind game'''


def main():
    '''driver code'''
    menu()





if __name__ == '__main__':
    main()
