from obsluga import naglowek, nacisnij_enter_aby_kontynuowac, wyczysc_ekran

def analiza(verbose) -> None:
    if verbose:
        print("Uruchomiono moduł analizatora danych\n")
        nacisnij_enter_aby_kontynuowac()
    wyczysc_ekran()
    naglowek()
    print("Analizator spółek")
    nacisnij_enter_aby_kontynuowac()
    # pobranie danych surowych z API
    # zapis danych surowych do pliku
    # szukanie błędów
    # wyczyszczenie danych
    # zapis danych wyczyszczonych do pliku
    # uzupełnieni danych o wskaźniki
    # zapis danych uzupełnionych do pliku
    
    return 0
