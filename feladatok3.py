def feladat_2(n):
    paros = 0
    paratlan = 0
    for i in range(n):
        szam=int(input('Adj meg egy szamot:'))
        if szam%2==0:
            paros+=1
        else:
            paratlan+=1
    print(paros,'paros',':',paratlan, 'paratlan' )

def feladat_3(n):
    tomb=[]
    for i in range(n):
        szam=int(input('Adj meg egy szamot:'))
        if szam < 0:
            szam=(-szam)
        elif szam > 0:
            szam=szam
        tomb.append(szam)
    print(tomb)
    reszosszeg=0
    for i in range(n):
        reszosszeg+=tomb[i]
    atlag=reszosszeg/n
    return atlag

def feladat_4(n):
    s=1
    k=0
    db=0
    for i in range(n):
        szam=int(input('Adj meg egy szamot:'))
        if szam>0:
            s*=szam
        elif szam<0:
            k+=szam
            db+=1
    print(s)
    print(k/db)

def feladat_5(n):
    t=[]
    for i in range(n):
        szam=int(input('Adj meg egy szamot:'))
        t.append(szam)
    b=1
    c=0
    for i in range(n):
        if t[i]<7:
           b*=t[i]
        elif t[i]>10:
            c+=t[i]
    print(b,c)

def lnko(m,n):
    maradek=m%n
    if maradek==0:
        return n
    return lnko(n, maradek)

def feladat_9(tomb, n):
    for i in range(0, n-1):
        for j in range(i+1, n):
            if lnko(tomb[i], tomb[j])!=1:
                return 0
    return 1
def main():
    feladat_2(5)
    print(feladat_3(5))
    feladat_4(5)
    feladat_5(5)
    print(feladat_9([1, 2, 3], 3))
if __name__ == '__main__':
    main()

