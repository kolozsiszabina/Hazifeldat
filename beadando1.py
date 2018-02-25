import math
def feladat_1(a,b):
    a=a+b
    b=a-b
    a=a-b
    print(a,b)

def feladat_2():
    lista=[]
    for i in range(3):
        lista.append(float(input('Adjon meg egy sazmot:')))
    for i in range(len(lista)-1):
        for j in range(i+1, len(lista)):
            if lista[i]>lista[j]:
                lista[i], lista[j]= lista[j], lista[i]
    print(lista)

def feladat_3(x):
    if x>-2 and x<0:
        return 2*x
    elif x>=0 and x<2:
        return x*x
    elif x>2:
        return 10
    else:
        print('A fugveny nem ertelmezett.')

def feladat_4(a,b,c):
    m=min(a,b,c)
    ma=max(abs(a), abs(b), abs(c))
    print('A minimum:', m, 'A maximum:', ma)

def feladat_5(a,b,c,d):
    print(a,b,c,d)
    if d>=0:
        print(a,c,b,d)
    else:
        print(a,b,d,c)

def feladat_6(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        p=(a+b+c)/2
        T=math.sqrt(p*(p-a)*(p-b)*(p-c))
        r=T/p
        R=(a*b*c)/(4*T)
        print('r=', r, 'R=', R)

def feladat_7(a,b, dh):
    Kt=(a+b)*2
    if dh>=Kt:
        maradek=dh-Kt
        print(maradek, 'meter drot maradt.')
    else:
        kell_meg=Kt-dh
        print('Meg', kell_meg, 'meter hosszu drot kell.')


def main():
    feladat_1(5,2)
    feladat_2()
    print(feladat_3(1))
    feladat_4(2,-6,5)
    feladat_5(2,3,5,0)
    feladat_6(2,3,4)
    feladat_7(5,7,5)
if __name__ == '__main__':
    main()