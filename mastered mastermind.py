from random import randint

#annotations
#enter
#nested for loops



def menu():
    print('If you want to play the game mastermind press 0')
    print('If you want to try the random strategy algorithm to see how efficient it works press 1')
    print('If you want to try the simple strategy algorithm to see how it performs press 2')
    press = int(input(''))
    generate(press)

#*** probeer de for loops te verminderen | ook meer annotations bij complexe codes***    
def makeguesslist(exclude = '',include=''):
    # colorlist = []
    #
    # for color in colordict.values():
    #     if exclude !=' ':
    #         if color not in exclude:
    #             colorlist.append(color)
    #     elif include != '':
    #         if color in include:
    #             colorlist.append(color)

    guesslist = []
    colorlist = ['A','B','C','D','E','F']

    for i0 in range(len(colorlist)):
        for i1 in range(len(colorlist)):
            for i2 in range(len(colorlist)):
                for i3 in range(len(colorlist)):
                    guesslist.append([colorlist[i0],colorlist[i1],colorlist[i2],colorlist[i3]])
    return guesslist

def generate_guesslist(possible_combinations,last_guess,feedback):
    ''''eliminates not possible combinations
    last guess = a guess from which the feedback is known
    feedback = feedback on last guess
    returns combinations which could be the secret code based on
    '''
    if type(feedback) == type((0,0)) :
        feedback = [feedback]

    solutions = []
    for combination in possible_combinations:
                for feed in feedback:
                    g = guess(last_guess,combination)
                    if g == feed:
                        solutions.append(combination)
    return solutions


def generate_guesslist_worstcase(possible_combinations,last_guess,feedback):
    ''''eliminates not possible combinations
    last guess = a guess from which the feedback is known
    feedback = feedback on last guess
    returns biggest worst case (number of possibilities per feedback)
    '''

    lenworstcase =0
    for feed in feedback:
        solutions = 0

        for combination in possible_combinations:
            g = guess(last_guess,combination)
            if g == feed:
                solutions+=1

        if solutions > lenworstcase:
            lenworstcase = solutions


    return lenworstcase







#*** probeer spaties tussen codes te zetten zodat het makkelijker te lezen is | ook meer annotations bij complexe codes  ***    
def generate(press):
    '''generates a random set of four letters representing colors
    calls function based on the number pressed
    press = number to select a certain algoritm or to play the game
    '''
    global colordict
    colordict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F'}
    playercode = ''
    for i in range(4):  #maakt een random colorcode
        playercode += colordict[int(randint(0,5))]

    guesslist = makeguesslist()


    if press == 0:
        while True:
            print('Guess a 4 letter code of the first 6 letters of the alphabet')
            while True:
                playerguess = input('\t\t').upper()
                if len(playerguess) > 4:
                    print('too long try again')
                else:
                    break
            g=guess(playercode,playerguess)
            print(g,playercode)
            if g == (4,0):
                print('Gewonnen!')
                again=input('type y if you want to play another match against the computer\ny/n:')
                if again == 'n':
                    break
                elif again == 'y':
                    playercode = ''
                    for i in range(4):  #maakt een random colorcode
                        playercode += colordict[int(randint(0,5))]

    elif press ==1:
        randomguess_strategy(playercode,guesslist)

    elif press == 2:
        totalamountoftries =0
        for i in range(1000):
            playercode = ''
            #maakt een random colorcode
            for x in range(4):
                 playercode += colordict[int(randint(0,5))]
            totalamountoftries +=simple_strategy(playercode,guesslist)
        with open('newfile.txt','a') as f:
            f.write(str(totalamountoftries/1000)+' tries for simple algoritm\n')
    elif press == 3:
        print(worst_case(playercode,guesslist))
        # totalamountoftries =0
        # for i in range(500):
        #     playercode = ''
        #     #maakt een random colorcode
        #     for x in range(4):
        #         playercode += colordict[int(randint(0,5))]
        #     totalamountoftries +=looking_ahead(playercode,guesslist)
        # with open('newfile.txt','a') as f:
        #     f.write(str(totalamountoftries/500)+' tries for looking one step ahead algoritm\n')

# line 103, probeer die if statement in 2 te delen | ook meer annotations bij complexe codes
def guess(code, playerguess):
    '''lets the player guess and returns amount of white and black pins'''

    pins = {'black':0,'white':0}
    dct = {0:True,1:True,2:True,3:True}
    lst = []
    blacklist = []


    # if playerguess == code:
    #     print('congrats you won')
    #print(playerguess)


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
            blacklist.append(lst[i-1])  #blacklist is gemaakt zodat als er een zwarte pin is dat de bij behorende letter in codeindex niet ook meteen wit wordt

    playerindex = 0
    whitelist = []
    while playerindex < len(playerguess):
        codeindex =0
        if dct[playerindex]:

            while playerguess[playerindex] in code and codeindex <len(code):
                if playerguess[playerindex] == code[codeindex] and  codeindex not in blacklist and codeindex not in whitelist:
                    pins['white'] +=1
                    whitelist.append(codeindex)
                    break
                codeindex+=1
        playerindex+=1



    return (pins['black'],pins['white'])


# meer annotations bij complexe codes voor lezers
def randomguess_strategy(code,guesslist):
    '''algoritm to solve mastermind game'''

    amountguessedlist = []

    # er wordt 100 keer gekeken naar het aantal guesses nodig om de code te kraken zodat er een beter beeld gemaakt kan worden van het gemiddeld aantal guesses
    for i in range(100):
        amountguessed =0

        # er wordt binnen onderstaande loop gekeken hoevaak hij moet gokken tot de code is geraden
        while True:
            g = guess(code,guesslist[int(randint(1,len(guesslist))-1)])
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
    code = list(code)
    total =0

    for j in range(1):
        for i in range(1):
            gl = guesslist
            amountguessed =0
            currentguess = ['A','A','A','A']
            currentfeedback = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]
            lastguess =0
            while True:
                if amountguessed !=0:
                    gl =generate_guesslist(gl,currentguess,currentfeedback)
                    currentguess =gl[0]     #int(randint(0,len(gl))-1)]
                    if lastguess in gl:
                        gl.remove(lastguess)
                #print(len(gl))

                #randomly guessing from possible guesses in gl(guesslist

                currentfeedback =guess(code,currentguess)

                lastguess = currentguess


                if currentfeedback[0] == 4:
                    amountguessedlist.append(amountguessed+1)
                    break
                amountguessed +=1
            total+=(amountguessed+1)

    return total

def worst_case(code,guesslist):
    '''algoritm to solve mastermind game
    works by calculating the amount of possibilities and determend the guess with the lowest worst case
    until the answer is found
    code = the secret code which has to be guessed
    guesslist = a list of all possible combinations
    returns the amount of tries it took to guess the secret code
    '''

    amountguessedlist = []
    code = list(code)
    total =0

    for j in range(1):
        for i in range(1):
            gl = guesslist
            amountguessed =0
            currentguess = ['A','A','B','B']
            allfeedback = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]
            minimal = 1296
            while True:
                if amountguessed !=0:
                    if lastguess in gl:
                        gl.remove(lastguess)
                    gl =generate_guesslist(gl,currentguess,currentfeedback)
                    for guess_fl in gl:
                        contestant = generate_guesslist_worstcase(gl,guess_fl,allfeedback)
                        print(contestant,'--> contestant',guess_fl,'-->guess_fl')

                        if contestant < minimal:
                            minimal = contestant
                            currentguess =guess_fl

                print(minimal,'--> minimal',currentguess,'--> currentguess',code,'--> code')
                currentfeedback =guess(code,currentguess)
                lastguess = currentguess
                if currentfeedback[0] == 4:
                    amountguessedlist.append(amountguessed+1)
                    break
                amountguessed +=1
            total+=(amountguessed+1)
    return total



def expected_size():
    '''algoritm to solve mastermind game'''


def merge_sort(arr, l,r):
    if l<r:
        m = (l+r)//2
        merge_sort(arr, l,m)
        merge_sort(arr, m+1,r)
        merge(arr,l,m,r)

def merge(arr,l,m,r):
    Larr = arr[l:m+1]
    Rarr =arr[m+1:r+1]

    j = i = 0

    for e in range(l,r+1):
        if Larr[i] <= Rarr[j]:
            arr[e]= Larr[i]
            i+=1
        else:
            arr[e]= Rarr[j]
            j+=1


def main():
    '''driver code'''
    menu()





if __name__ == '__main__':
    main()
