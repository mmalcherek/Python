def make_change(cents: int):
    # Lista dostępnych nominałów od największego do najmniejszego
    denominations = [200, 100, 50, 20, 10, 5, 2, 1]
    result = {}
    
    for coin in denominations:
        if cents >= coin:
            count = cents // coin   # Obliczanie liczby sztuk danego nominału
            result[coin] = count    # Dodanie do słownika wynikowego
            cents %= coin           # Obliczanie pozostałej reszty
            
    return result

# Przykład użycia dla kwoty 367 centów
amount = 367
output = make_change(amount)

print(f"Kwota {amount} centów rozbija się na:")
print(output)

