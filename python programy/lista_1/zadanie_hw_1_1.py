import random

#max_value = int(input("podaj zakres:"))
values_available = [15,21,35,105,8]
#values_available = random.sample(list(range(1, max_value + 1)), max_value)
print((values_available))

for i in values_available:

    if i %3 == 0 and i % 5 == 0 and i % 7 == 0:
        print('FizzBuzzBang')
    elif i % 3 == 0 and i % 5 == 0:
        print('FizzBuzz')
    elif i % 7 == 0: 
        print('Bang')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0: 
        print('Buzz')
    else: 
        print(i) 