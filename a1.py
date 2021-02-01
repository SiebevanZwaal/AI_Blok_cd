def pir0(len, reverse=False):
    if not reverse:
        for i in range(len):
            print(i*'*')
        for i in range(len,0,-1):
            print(i*'*')
    else:
        for i in range(len):
            print((len-i)*' '+i*'*')
        for i in range(len,0,-1):
            print((len-i)*' '+i*'*')


def pir1(len, reverse= False):
    if not reverse:
        i= 1
        while i <len:
            print(i*'*')
            i+=1
        while i > 0:
            print(i*'*')
            i-=1
    else:
        i= 1
        while i <len:
            print((len-i)*' '+i*'*')
            i+=1
        while i > 0:
            print((len-i)*' '+i*'*')
            i-=1


def strdiff():
    in0 = input('type a string')
    in1 = input('type a string')

    for i in range(len(in0)):
        if in0[i] != in1[i]:
            return i
    return -1


def count(lst,x):
    a=0
    for i in lst:
        if i == x:
            a+=1
    return a

lst0 = [1,1,2,2,2,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,899]

def condiff(lst):
    '''returns biggest consecutive difference'''
    mini = 0
    for i in range(len(lst)-1):
        x = ((lst[i]-lst[i+1])**2)**0.5
        if x > mini:
            mini = x
    return mini


def m1t0(lst):
    a0 = count(lst,0)
    return count(lst,1)>a0 and a0 <= 12


def pal(wrd):
    return wrd == wrd[::-1]


def pal1(wrd):
    return wrd == ''.join(reversed(wrd))


def qs(lst):
    if len(lst) <= 1:
        return lst
    p = lst.pop()
    s = []
    l = []
    for i in lst:
        if i >=p:
            l.append(i)
        else:
            s.append(i)
    return qs(s)+ [p]+qs(l)


def mean(lst):
    t = 0
    for i in lst:
        t+=i
    return t/len(lst)

def means(lst):
    l={}
    for i in lst:
        l[str(i)]=mean(i)
    return l

from random import randint

def random():
    x =int(input('Kies binnen welke range u een random getal wilt kiezen: '))
    r=  randint(1,x)
    while True:
        g = int(input('kies een getal tussen 0 en '+str(x)+': '))
        if g == r:
            print('Correct')
            break
        else:
            if g > r:
                print('Fout, lager')
            else:
                print('Fout, hoger')

def cp(fn):
    with open(fn, 'r') as f:
        for i in f.readlines():
            if i !='\n':
                for x in range(len(i)):
                    if i[x] != '\t' and i[x] !=' ':


def cycver(ch,n):
    '''deze functie verschuift bitjes, hij werkt ook als n groter is dan de lengte van ch en bij alle verschillende lengtes van ch'''
    ch = str(ch)
    l = len(ch)
    if n > l:
        n = n%l
    if n < -l:
        n = n%-l
    c = ''
    a = ''
    if n > 0:
        for i in range(n):
            c+=ch[i]
        for i in range(n-l,0):
            a+=ch[i]
        a+=c
        return a
    else:
        for i in range(n,0):
            c+=ch[i]
        for i in range(0,n+l):
            a+=ch[i]
        c+=a
        return c

#print(cycver(1011100101010010101010010101010,-74))


def Fib(f):
    return Fib2(f,0,1)


def Fib2(f,n0,n1):
    if f == 0:
        return n1
    t = n1
    n1+=n0
    n0 =t
    f-=1
    return Fib2(f,n0,n1)

#print(Fib(9))

def ceasar(s,r):
    a =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    sn=''
    r = r%len(a)
    print('r',r)
    for e in s:
        if e == ' ':
            sn+=' '
        else:
            i = a.index(e.lower())
            sn+=a[(i+r)%len(a)]
    return sn

# print(ceasar('help',-1))

def Fizzbuzz(getal):
    for i in range(1,getal+1):
        if i % 15 == 0:
            print('fizzbuzz')
        elif i % 5 == 0:
            print('buzz')
        elif i % 3 == 0:
            print('fizz')
        else:
            print(i)

# print(Fizzbuzz(99))