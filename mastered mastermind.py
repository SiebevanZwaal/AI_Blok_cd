from random import randint





def menu():
    '''creates a menu and calls generate with the desired number corresponding to a algoritm'''

    print('If you want to play the game mastermind press 0')
    print('If you want to try the random strategy algorithm to see how efficient it works press 1')
    print('If you want to try the simple strategy algorithm to see how it performs press 2')
    print('If you want to try the worst case algorithm to see how it performs press 3')
    print('If you want to try the siebe algorithm to see how it performs press 4')
    press = int(input(''))
    generate(press)


def makeguesslist():
    '''returns a list with al possible combinations of "['A','B','C','D','E','F']"'''

    guesslist = []
    colorlist = ['A','B','C','D','E','F']

    for i0 in range(len(colorlist)):
        for i1 in range(len(colorlist)):
            for i2 in range(len(colorlist)):
                for i3 in range(len(colorlist)):
                    guesslist.append([colorlist[i0],colorlist[i1],colorlist[i2],colorlist[i3]])
    return guesslist


def generate_guesslist(possible_combinations:list,last_guess:list,feedback:tuple):
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
                    g = get_feedback(last_guess,combination)
                    if g == feed:
                        solutions.append(combination)
    return solutions


def generate_guesslist_worstcase(possible_combinations:list,last_guess:list,feedback:list):
    ''''eliminates not possible combinations
    last guess = a guess from which the feedback is known
    feedback = feedback on last guess
    returns biggest worst case (number of possibilities per feedback)
    '''

    lenworstcase =0
    for feed in feedback:
        solutions = 0

        for combination in possible_combinations:
            g = get_feedback(last_guess,combination)
            if g == feed:
                solutions+=1

        if solutions > lenworstcase:
            lenworstcase = solutions


    return lenworstcase







#*** probeer spaties tussen codes te zetten zodat het makkelijker te lezen is | ook meer annotations bij complexe codes  ***    
def generate(press:int):
    '''generates a random set of four letters representing colors
    calls function based on the number pressed
    press = number to select a certain algoritm or to play the game
    '''

    global colordict
    colordict = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E', 5:'F'}
    code = ''
    for i in range(4):  #maakt een random colorcode
        code += colordict[int(randint(0,5))]
    code = list(code)
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

            g=get_feedback(code,list(playerguess))
            print(g)

            if g == (4,0):
                print('Gewonnen!')
                again=input('type y if you want to play another match against the computer\ny/n:')
                if again == 'n':
                    break
                elif again == 'y':
                    code = ''
                    for i in range(4):  #maakt een random colorcode
                        code += colordict[int(randint(0,5))]

    elif press ==1:
        randomguess_strategy(code,guesslist)


    elif press == 2:
        totalamountoftries =0
        for i in range(1000):
            code = ''
            #maakt een random colorcode
            for x in range(4):
                 code += colordict[int(randint(0,5))]
            totalamountoftries +=simple_strategy(code,guesslist)
        with open('newfile.txt','a') as f:
            f.write(str(totalamountoftries/1000)+' tries for simple algoritm\n')


    elif press == 3:
        totalamountoftries =0
        for i in range(10):
            code = ''
            #maakt een random colorcode
            for x in range(4):
                code += colordict[int(randint(0,5))]
            totalamountoftries +=worst_case(code,guesslist)
        with open('newfile.txt','a') as f:
            f.write(str(totalamountoftries/10)+' tries for worst case algoritm\n')

    elif press ==4:

        totalamountoftries =0
        for i in range(500000):
            code = ''
            #maakt een random colorcode
            for x in range(4):
                code += colordict[int(randint(0,5))]
            totalamountoftries +=siebe_algorithm(list(code))
        with open('newfile.txt','a') as f:
            f.write(str(totalamountoftries/500000)+' tries for siebe algoritm\n')

# line 103, probeer die if statement in 2 te delen | ook meer annotations bij complexe codes
def get_feedback(code:list, guess:list):
    '''evaluates the guess compared to the code
    returns amount of white and black pins as a tuple
    '''

    pins = {'black':0,'white':0}
    dct = {0:True,1:True,2:True,3:True}
    lst = []
    blacklist = []

    i=0
    while i < len(guess):
        if guess[i] == code[i]:
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
    while playerindex < len(guess):
        codeindex =0

        if dct[playerindex]:
            while guess[playerindex] in code and codeindex <len(code):
                if guess[playerindex] == code[codeindex] and  codeindex not in blacklist and codeindex not in whitelist:
                    pins['white'] +=1
                    whitelist.append(codeindex)
                    break
                codeindex+=1

        playerindex+=1



    return (pins['black'],pins['white'])


# meer annotations bij complexe codes voor lezers
def randomguess_strategy(code:list,guesslist:list):
    '''algoritm to solve mastermind game by randomly guessing codes
    returns the average amount of guesses to get the code when tested 1000 times
    '''

    amountguessedlist = []

    # er wordt 100 keer gekeken naar het aantal guesses nodig om de code te kraken zodat er een beter beeld gemaakt kan worden van het gemiddeld aantal guesses
    for i in range(1000):
        amountguessed =0

        # er wordt binnen onderstaande loop gekeken hoevaak hij moet gokken tot de code is geraden
        while True:
            g = get_feedback(code,guesslist[int(randint(1,len(guesslist))-1)])
            if g[0] == 4:
                amountguessedlist.append(amountguessed)
                break
            amountguessed +=1

    total = 0

    for amountguessed in amountguessedlist:
        total +=amountguessed

    print(total/len(amountguessedlist),f'tries on average when tested a {len(amountguessedlist)} times')


def simple_strategy(code:str,guesslist:list):
    '''algoritm to solve mastermind game
    gets the code by checking which combinations are not valid with the feedback given so far
    returns amount of times guessed
    '''

    amountguessedlist = []
    code = list(code)
    total =0
    gl = guesslist
    amountguessed =0

    #eerste keuze zal altijd "['A','A','A','A']" zijn maar het scheelt best veel rekenkracht om het te hardcoden
    currentguess = ['A','A','A','A']
    lastguess =0

    while True:
        if amountguessed !=0:
            gl =generate_guesslist(gl,currentguess,currentfeedback)
            currentguess =gl[0]
            if lastguess in gl:
                gl.remove(lastguess)
        currentfeedback =get_feedback(code,currentguess)
        lastguess = currentguess

        if currentfeedback[0] == 4:
            amountguessedlist.append(amountguessed+1)
            break
        amountguessed +=1

    total+=(amountguessed+1)

    return total

def worst_case(code:str,guesslist:list):
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

    gl = guesslist
    amountguessed =0
    currentguess = ['A','A','B','B']
    allfeedback = [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(2,0),(2,1),(2,2),(3,0),(4,0)]
    minimal = 1296
    minimallist =[]
    while True:
        if amountguessed !=0:
            if lastguess in gl:
                gl.remove(lastguess)
            gl =generate_guesslist(gl,currentguess,currentfeedback)
            for guess_fl in gl:
                contestant = generate_guesslist_worstcase(gl,guess_fl,allfeedback)

                if contestant < minimal:
                    minimal = contestant
                    currentguess =guess_fl
                    minimallist = []
                elif contestant == minimal:
                    minimallist.append(guess_fl)

        print(len(gl),'--> length guess list')
        currentfeedback =get_feedback(code,currentguess)
        lastguess = currentguess

        if currentfeedback[0] == 4:
            amountguessedlist.append(amountguessed+1)
            break

        amountguessed +=1


    total+=(amountguessed+1)
    return total


def siebe_algorithm(code:list):
    '''algoritm to solve mastermind game'''
    indexlist = ['1234','1243','1324','1342','1432','1423' ,
                 '2134','2143','2314','2341','2413','2431' ,
                 '3124','3142','3214','3241','3412','3421' ,
                 '4123','4132','4213','4231','4312','4321']


    guess =''
    for letter in 'ABCDEF':
        feedback = get_feedback(code,list(letter*4))
        if feedback[0]+feedback[1]>0:
            for i in range(feedback[0]+feedback[1]):
                guess += letter
    amountofguesses =6
    for i in indexlist:
        f =get_feedback(code,list(guess[int(i[0])-1]+guess[int(i[1])-1]+guess[int(i[2])-1]+guess[int(i[3])-1]))
        amountofguesses+=1
        if f ==(4,0):
            break

    return amountofguesses


def main():
    '''driver code'''
    menu()


if __name__ == '__main__':
    main()
