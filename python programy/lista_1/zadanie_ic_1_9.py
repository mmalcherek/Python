
a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))
operator = input("Podaj operator (+, -, *, /): ")
if operator == "+": 
    print(a + b)
elif operator == "-":
    print(a - b)
elif operator == "*" and a != 0 and b != 0:
    print(a * b)
elif operator == "/" and a != 0 and b != 0:
    print(a / b)
else:
    print("zły operator!")
