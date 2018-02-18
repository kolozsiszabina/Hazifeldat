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
        
def feladat_8(a,b,c,d,x):
    def f_fuggveny():
        if x<5:
            return 3*x-5
        elif x>=5 and x<=10:
            return 10
        elif x>10:
            return 9*x+1
    def E():
        if a+c>2*d and b>0:
            return d-3*b
        elif a+c<2*d and b<0:
            return d+3*b
        else:
            return 4
    print('x=',f_fuggveny(), 'E=', E())
        
def feladat_10(a,b):
    ossz=b-a
    db=0
    for i in range(0,ossz):
        if i%100==0 and i%400==0 or i%100!=0 and i%4==0:
            db+=1
    print(db)

def feladat_12(max_pont, elert_pont):
    if elert_pont>=max_pont*0.60:
        print('Sikeres vizsga.')
    else:
        print('Sikertelen vizsga.')
        
def feladat_13(erdemjegy):
    if erdemjegy==1:
        print('Elegtelen')
    elif erdemjegy==2:
        print('Elegseges')
    elif erdemjegy==3:
        print('Kozepes')
    elif erdemjegy==4:
        print('Jo')
    elif erdemjegy==5:
        print('Jeles')
        
def feladat_14(honap_szama):
    if honap_szama==1:
        print('Januar')
    elif honap_szama==2:
        print('Februar')
    elif honap_szama==3:
        print('Marcius')
    elif honap_szama==4:
        print('Aprilis')
    elif honap_szama==5:
        print('Majus')
    elif honap_szama==6:
        print('Junius')
    elif honap_szama==7:
        print('Julius')
    elif honap_szama==8:
        print('Augusztus')
    elif honap_szama==9:
        print('Szeptember')
    elif honap_szama==10:
        print('Oktober')
    elif honap_szama==11:
        print('November')
    elif honap_szama==12:
        print('December')
        
def feladat_15(a,b):
    hanyados=0
    while a>=b:
        hanyados+=1
        a=a-b
    print(hanyados)
    

def main():
    feladat_1(5,2)
    feladat_2()
    print(feladat_3(1))
    feladat_4(2,-6,5)
    feladat_5(2,3,5,0)
    feladat_6(2,3,4)
    feladat_7(5,7,5)
    feladat_8(1,2,3,4,5)
    feladat_10(1998, 2018)
    feladat_12(100, 59)
    feladat_13(3)
    feladat_14(8)
    feladat_15(520,104)
if __name__ == '__main__':
    main()
