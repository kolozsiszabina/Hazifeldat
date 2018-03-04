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
    feladat_10()

if __name__ == '__main__':
    main()

