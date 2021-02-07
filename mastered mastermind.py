from random import randint

def generate():
    '''generates a random set of four letters representing colors'''
    colordict = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F'}
    code = ''
    for i in range(4):
        code += colordict[int(randint(0,5))]
    guess(list(code))

def guess(code, amount_guess=0):
    '''lets the player guess and returns amount of white and black pins'''
    playerguess = input('Guess a combination of uppercase letters between A to and with F\n')
    playerguesslist = list(playerguess)
    pins = {'black':0,'white':0}
    #print(code)
    dct = {1:True,2:True,3:True,4:True}
    if playerguesslist== code:
        return 'U heeft gewonnen'
    i=0
    while i < len(playerguesslist):
        print(i)
        if playerguesslist[i] == code[i]:
            pins['black'] +=1
            dct[i] = False

        i+=1
    i = 0
    while i < len(playerguesslist):
        j =0
        while linear_search_recursive(code,playerguesslist[i]) and j <len(code):#for j in range(len(code1)):
            if dct[i]:
                if playerguesslist[i] == code[j]:
                    pins['white'] +=1
                    break
            j+=1
        i+=1

    print(pins)
    guess(code)

def linear_search_recursive(lst, target):
    if lst == []:
        return False
    if lst[0] == target:
        return True
    else:
        return linear_search_recursive(lst[1:],target)


def simple_strategy():
    '''algoritm to solve mastermind game'''


def looking_ahead():
    '''algoritm to solve mastermind game'''


def worst_case():
    '''algoritm to solve mastermind game'''


def expected_size():
    '''algoritm to solve mastermind game'''


def main():
    '''driver code'''
    guess(['D', 'F', 'D', 'B'])



if __name__ == '__main__':
    main()