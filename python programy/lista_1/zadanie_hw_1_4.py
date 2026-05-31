
def to_roman(number):
    
    lookup = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    result = ""
    for value, romans in lookup:    # number to liczba która chce zamienić, romans to odpowiednik rzymski
        while number >= value:      # sprawdzam liczbe np 94 czy jest większa lub równa liczbie w tabeli lookup. 
            result += romans        # 94 jest mniejsze niz 1000,900,500,400,100 więc jest pomijane, ale 94 >= 90 więc wchodzi do pętli 
            number -= value         # skoro 94 spelnia warunek to bierzemy rzymską licze dla 90 czyli XC odejmujemy od 94 wartość 90 i zostaje nam 4, 
                                    # sprawdzamy dalej czy 4 >= 1000,900,500,400,100,90,50,40,10,9,5 - nie jest,
                                    # więc pomijane ale 4 >= 4 więc wchodzi do pętli i dodajemy IV do wyniku.  Odejmujemy od 4 wartość 4 i zostaje nam 0. 
                                    # Sprawdzamy dalej czy 0 >= 1000,900,500,400,100,90,50,40,10,9,5,4 - nie jest, 
                                    # więc pomijane ale 0 >= 1 - nie jest więc pomijane i kończymy pętle
    return result        

print(f'(1) # "{to_roman(1)}"')
print(f'(4) # "{to_roman(4)}"')
print(f'(9) # "{to_roman(9)}"')
print(f'(40) # "{to_roman(40)}"')
print(f'(94) # "{to_roman(94)}"')
print(f'(1994) # "{to_roman(1994)}"')
print(f'(3999) # "{to_roman(3999)}"')
