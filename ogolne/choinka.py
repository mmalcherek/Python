
a=int(input("Podaj liczbe:?"))

if a==1:
    print(' /\\')
    print('/__\\')
elif a==2:
    print('  /\\')
    print(' /__\\')
    print('/____\\')
elif a==3:
    print('   /\\')
    print('  /__\\')
    print(' /____\\')
    print('/______\\')
else:
    print("Błąd")
    
    
    
    import random

max_value = int(input("podaj największą możliwą liczbę:"))
rolls = int(input("ile losowań?:"))

number_available = list(range(1, max_value + 1))
rolled_numbers = random.sample(number_available, rolls)
print(sorted(rolled_numbers))
    


