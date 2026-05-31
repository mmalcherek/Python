# kolekcje, listy, krotki, slowniki, zbiory
# lista = [1, 2, 3, 4, 5]
# krotka = (1, 2, 3, 4, 5)
# slownik = {"a": 1, "b": 2, "c": 3}
# zbior = {1, 2, 3, 4, 5}       

#lista to uporządkowana, indeksowana, mutowalna kolekcja elementów. Może zawierać duplikaty i różne typy danych.
#krotka to uporządkowana, indeksowana, niemutowalna kolekcja elementów. Może zawierać duplikaty i różne typy danych.
#slownik to nieuporządkowana, indeksowana, mutowalna kolekcja par klucz-wartość. Klucze muszą być unikalne i niemutowalne, a wartości mogą być dowolnego typu.
#zbiór to nieuporządkowana, niemutowalna kolekcja unikalnych elementów. Nie może zawierać duplikatów i może zawierać różne typy danych.

# Kolekcje te różnią się pod względem uporządkowania, mutowalności, indeksowania i możliwości przechowywania duplikatów, 
# co wpływa na ich zastosowanie w różnych sytuacjach programistycznych.

#podsumowując: którą i kiedy wybrać?
# - listy są idealne, gdy potrzebujemy uporządkowanej, mutowalnej kolekcji, która może zawierać duplikaty i różne typy danych.
# - krotki są idealne, gdy potrzebujemy uporządkowanej, niemutowalnej kolekcji, która może zawierać duplikaty i różne typy danych.
# - słowniki są idealne, gdy potrzebujemy nieuporządkowanej, mutowalnej kolekcji par klucz-wartość, gdzie klucze muszą być unikalne i niemutowalne.
# - zbiory są idealne, gdy potrzebujemy nieuporządkowanej, niemutowalnej kolekcji unikalnych elementów, bez duplikatów i różnych typów danych.


from datetime import date, timedelta   
reports = ["2026-01-01", "2026-01-02", "2026-01-04", "2026-01-05", "2026-01-08"]

def find_date(missing_date):
    first_date = date.fromisoformat(missing_date[0])
    last_date = date.fromisoformat(missing_date[-1])
    list_of_full_dates = {(first_date + timedelta(days=i)).isoformat() for i in range((last_date - first_date).days + 1)}
    return sorted(list_of_full_dates - set(missing_date))

print(find_date(reports))


# expected: ["2026-01-03", "2026-01-06", "2026-01-07"]