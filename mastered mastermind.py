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
    pins = {'black':0,'white':0}
    code1=[]
    j=0
    for i in code:
        code1.append(i)
    print(code1)
    if list(playerguess) == code:
        return 'U heeft gewonnen'
    for i in range(len(playerguess)):
        if playerguess[i] == code[i]:
            pins['black'] +=1
            code1.remove(code1[i])
    for i in range(len(playerguess)):
        while code1 !=[] and j <len(code1):#for j in range(len(code1)):
            #print(code1)
            if playerguess[i] == code1[j]:
                pins['white'] +=1
                code1.remove(code1[j])
            j+=1

    print(pins)
    guess(code)


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
    print(generate())



if __name__ == '__main__':
    main()