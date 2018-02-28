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

def feladat_16(a,b):
    while True:
        r=a%b
        a=b
        b=r
        if r==0:
            break
    return a

def feladat_17(x):
    masolat=x
    uj_szam=0
    while x!=0:
        szamjegy=x%10
        uj_szam=(uj_szam*10)+szamjegy
        x=x//10
    return uj_szam==masolat

def feladat_19(n):
    if n<2:
        return False
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True

def feladat_20(n):
    a=1
    b=1
    k=1
    while k<n:
        print('%.4f'%(a/b), end=', ')
        a=a+b
        b=a-b
        k+=1
        
def feladat_21(n):
    ujszam=0
    while n!=0:
        maradek=n%10
        ujszam=(ujszam*10)+maradek
        n=n//10
    return ujszam

def feladat_24():
    s=0
    k=0
    szam = int(input('Adj meg egy szamot:'))
    while szam!=0:
        szam=int(input('Adj meg egy szamot:'))
        if szam%7==5:
            s+=1
        elif szam%13==7:
            k+=1
    print('s=', s, 'k=', k)
    
def feladat_25():
    lakossag=input('A lakkosag szama (fo):')
    terulet=('Az orszag terulete negyzet kilometerben:')
    suruseg=lakossag/terulet
    if suruseg<50:
        print('Ritkan lakott.')
    elif suruseg<300 and suruseg>50:
        print('Atlagos lakossag.')
    elif suruseg>300:
        print('Surun lakott.')
        
def feladat_26():
   s=0
   negativdb=0
   pozitivdb=0
   szam = float(input('Adj meg egy szamot:'))
   while szam!=0:
       szam=float(input('Adj meg egy szamot:'))
       s += szam
       print(s)
       if szam<0:
           negativdb+=1
       elif szam>0:
           pozitivdb+=1
   print(('Pozitiv:', pozitivdb, ('Negativ:', negativdb)))

def feladat_27():
    negativdb=0
    pozitivdb=0
    while True:
        szam=int(input('Adj meg egy szamot:'))
        szam1=int(input('Adj meg egy szamot:'))
        if szam<0 and szam1>0 or szam>0 and szam1<0:
            if szam>0 or szam1>0:
                pozitivdb+=1
            elif szam<0 or szam1<0:
                negativdb+=1
        else:
            break
    print('Negativ:', negativdb, 'Pozitiv:', pozitivdb)
    
def feladat_28(n):
    li=[]
    for i in range(n):
        ertek=i**2
        if ertek<n:
            li.append(ertek)
    print(li[-1])

def feladat_29(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    return n*feladat_29(n-1)

def feladat_30():
    ev=int(input('Add meg az evet:'))
    honap=int(input('Add meg a honap szamat:'))
    nap=int(input('Add meg a napot:'))
    osszeg=(honap*30)+nap
    print(osszeg)
    
def feladat_31(n):
    li=[]
    for i in range(1,n+1):
        if n/i==0:
            li.append(i)
    print(li)
    
def feladat_32(k):
    lista1=[]
    n1=int(input('Adj meg egy also korlatot:'))
    n2=int(input('Adj meg egy felso korlatot:'))
    for i in range(n1,n2+1):
        if (i/k==0):
            lista1.append(i)
    print(lista1)
    
def feladat_35(n):
    def Prim(szam1):
        oszt = 2
        while oszt <= szam1 / 2:
            if szam1 % oszt == 0:
                return False
            oszt += 1
        return True
    for i in range(0, n):
        szam1 = i
        szam2 = i + 2
        if Prim(szam1) and Prim(szam2):
            print("(", szam1, ",", szam2, ")")
            
def feladat_38():
    s=0
    szamjegy=(input('Adj meg egy kilenc szambol allo szamjegyet:'))
    szam=(input('Adj meg egy szamot:'))
    for szam in szamjegy:
        if szam in szamjegy:
            s+=1

def main():
    feladat_1(5,2)
    feladat_2()
    print(feladat_3(1))
    feladat_4(2,-6,5)
    feladat_5(2,3,5,0)
    feladat_6(2,3,4)
    feladat_7(5,7,5)
    feladat_8(1, 2, 3, 4, 5)
    feladat_10(1998, 2018)
    feladat_12(100, 60)
    feladat_13(3)
    feladat_14(5)
    feladat_15(520, 104)
    print(feladat_16(360, 225))
    print(feladat_17(353))
    print(feladat_19(5))
    feladat_20(5)
    print(feladat_21(3659824157))
    feladat_24()
    feladat_25()
    feladat_26()
    feladat_27()
    (feladat_28(25))
    print(feladat_29(5))
    feladat_30()
    feladat_31(100)
    print(feladat_32(5))
    feladat_35(5)
    print(feladat_38())
if __name__ == '__main__':
    main()
