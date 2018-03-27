import numpy as np
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
def feladat_12(matrix):
    for i in range(1,len(matrix)):
        for j in range(0,len(matrix)):
            if matrix[i][j]%(i+j)==0:
                return matrix[i][j]
def feladat_15(matrix, meret):
    for i in range(len(matrix)):
        if matrix[i][i]!=0:
            return False
    return True
def feladat_16(m):
    er = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    print("\n")
    for tr in er:
        print(tr)
def hatos(n,m):
    hat=np.zeros((n,m))
    for i in range(n):
        for j in range(m):
            if i==0 or i==n-1 or i==n//2:
                hat[i][j]=42
            else:
                hat[i][j]=32
        hat[i][0]=42
        if i>n//2:
            hat[i][m-1]=42

    for i in range(n):
        for j in range(m):
            print(chr(int(hat[i][j])),end=' ')
        print('\n')
def vasarlas():
    s=0
    for i in range(1,100):
        osszeg=float(input('Adj meg egy szamot:'))
        if osszeg!=0:
            s+=osszeg
        elif osszeg==0:
            break
            print(s)
    print(s)
def main():
    feladat_2(5)
    print(feladat_3(5))
    feladat_4(5)
    feladat_5(5)
    print(feladat_9([1, 2, 3], 3))
    print(feladat_12([[1,2,1],[2,1,1]]))
    print(feladat_15([[0,1,2],[1,0,2],[1,2,0]],3))
    feladat_16([[4,9,2],[3,5,7],[8,1,6]])
    esetek = int(input())
    t=np.zeros(2*esetek,dtype='int')
    for i in range(0,2*esetek,2):
       sor=input()
       sor=sor.strip()
       sor=sor.split()
       t[i]=int(sor[0])
       t[i+1]=int(sor[1])
    for i in range(0,2*esetek,2):
       hatos(t[i],t[i+1])
    vasarlas()
if __name__ == '__main__':
    main()

