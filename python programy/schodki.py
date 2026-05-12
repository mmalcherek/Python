ile = int(input('ile razy?:'))
def pattern(ile):
    for i in range(0,ile):
        for j in range(0,i+1):
            print('*', end='')
        print('\r')
pattern(ile)
