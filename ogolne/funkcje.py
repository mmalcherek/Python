def suma(a,b):
    return a+b
def roznica(a,b):
    return a-b

def iloczyn(a,b):
    return a*b

def iloraz(a,b):
    return a/b

def kalkulator(wybor,a,b):
    if wybor==1:
        print(suma(a,b))
    if wybor==2:
        print(roznica(a,b))
    if wybor==3:
        print(iloczyn(a,b))
    if wybor==4:
        print(suma(a,b))
kalkulator(2,5,3)