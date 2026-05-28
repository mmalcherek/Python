# pierwszy problem: niepotrzebnie zrobiłem from random import random, przez co miałem problem z użyciem funkcji sample,
# która jest w module random, a nie jest importowana bezpośrednio.

import random

while True:
    # min_value = 1 - pierwszy pomysł do ograniczenia listy, ale potem wpadłem na ograniczenie już w range
    max_value = int(input("podaj największą możliwą liczbę:"))
    numbers = int(input("ile losowań?:"))

    # number_available = [] - pomysł, żeby najpierw stworzyć liste, ale po ostatnich zajęciach już wiem, że mogę to zrobić tak jak poniżej


    number_available = random.sample(list(range(1, max_value + 1)),numbers)
    #w range prawie się złapałem na zakres, bo jak podam max_value = 8  to != 8 bedzie ostatnia liczbą w range tylko 7. 
    # Dtaltego wrzucam + 1
    #random.choice - robi to samo co sample, ale z możliwościa powtórzeń

    print(sorted(number_available))

    choose = str(input("gramy dalej? [T/N]")).strip().upper()
    if choose == 'T':
        continue
    if choose == "N":
        print("Do zobaczenia!")
    break