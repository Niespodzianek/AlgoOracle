from obsluga import naglowek, nacisnij_enter_aby_kontynuowac, wyczysc_ekran
from lista_spolek import wig

def analiza(verbose) -> None:
    if verbose:
        print("Uruchomiono moduł analizatora danych\n")
        nacisnij_enter_aby_kontynuowac()
    wyczysc_ekran()
    naglowek()
    print("Analizator spółek")
    
    # pobranie danych surowych z API
    print(wig)
    # zapis danych surowych do pliku
    # szukanie błędów
    # wyczyszczenie danych
    # zapis danych wyczyszczonych do pliku
    # uzupełnieni danych o wskaźniki
    # zapis danych uzupełnionych do pliku
    nacisnij_enter_aby_kontynuowac()
    return 0
