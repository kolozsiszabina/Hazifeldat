def feladat_1(n):
    while True:
        s=0
        for i in range(1,n+1):
            if n%i==0:
                s=s+1
        if s==4:
            return True
        else:
            return False
def feladat_2(n):
    for i in range(n+1):
        s=0
        for j in range(1,n+1):
            if i%j==0:
                s+=1
        if s==2:
            print(i, end=',')
def feladat_8(n):
    m = 0
    db = 0
    for i in range(1, n):
        m += i
        db += 1
        if m > n:
            break
    if m >= n:
        print(db)
def feladat_10():
    try:
        fajl=open('be.txt', mode='r')
        max=0
        for sor in fajl:
            sor=sor.split()
            if (sor[0].isupper() and len(sor)>max):
                max=len(sor)
        print(max)
        fajl.close()
    except Exception as e:
        print(e)




def main():
    print(feladat_1(8))
    feladat_2(11)
    feladat_8(8)
    feladat_10()

if __name__ == '__main__':
    main()

