#zadanie_1
# a = 0.1
# b = 0.2
# def czy_blisko(x, y):
#     return abs(x - y) < 1e-9    
# print(czy_blisko(a + b, 0.3))

'''
#zadanie_2
name = "Anna"
score  = 12.34
procent = 0.756

print(f"{name.upper()} scored {score:.1f} ({procent:.1%})")
'''


# print(bool(0), bool(0.0), bool(""), bool([]), bool({}),
# bool(None))
# print(bool("False"), bool("0"), bool([0]), bool({0: 0}))
# print(0 == False, 1 == True, 2 == True)

#test dla zbioru n = 0, 11, 12, 13, , 25, 100
# ciastka = 100
# pojemnnosc= 12 
# ilosc_pojemnikow_pelne = ciastka // pojemnnosc
# pozostale_ciastka = ciastka % pojemnnosc
# print(f"ciastka: {ciastka}")
# print(f"ilosc_pojemnikow_pelne: {ilosc_pojemnikow_pelne}")
# print(f"pozostale_ciastka: {pozostale_ciastka}")
# print(f"calkowita_ilosc_pojemnikow: {ilosc_pojemnikow_pelne + (1 if pozostale_ciastka > 0 else 0)}  ")



# kolekcje, listy, krotki, slowniki, zbiory
# lista = [1, 2, 3, 4, 5]
# krotka = (1, 2, 3, 4, 5)
# slownik = {"a": 1, "b": 2, "c": 3}
# zbior = {1, 2, 3, 4, 5}       


from datetime import date, timedelta   
reports = ["2026-01-01", "2026-01-02", "2026-01-04", "2026-01-05", "2026-01-08"]

def find_date(missing_date):
    first_date = date.fromisoformat(missing_date[0])
    last_date = date.fromisoformat(missing_date[-1])
    list_of_full_dates = {(first_date + timedelta(days=i)).isoformat() for i in range((last_date - first_date).days + 1)}
    return sorted(list_of_full_dates - set(missing_date))

print(find_date(reports))


# expected: ["2026-01-03", "2026-01-06", "2026-01-07"]