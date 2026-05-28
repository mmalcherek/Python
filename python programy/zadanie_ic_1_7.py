try:
    # Pobranie temperatury od użytkownika i konwersja na liczbę zmiennoprzecinkową
    celsius = float(input("Podaj temperaturę w stopniach Celsjusza: "))
    
    # Stopnie Celciusza na Farenthite
    fahrenheit = celsius * 9/5 + 32
    
    # Wyświetlenie wyniku
    print(f"{celsius}°C to {fahrenheit:.1f} K")
    
except ValueError:
    print("Błąd! Podana wartość nie jest poprawną liczbą.")
    
    
    
