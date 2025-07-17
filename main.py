from obsluga import naglowek, nacisnij_enter_aby_kontynuowac
from lista_spolek import wig
import yfinance as yf

def pobranie_surowych_danych(lista, verbose) -> list:
    lista_surowych_danych_spolek: list = []
    if verbose:
        print("Uruchomiono moduł pobierania surowych danych\n")
        nacisnij_enter_aby_kontynuowac()
    for spolka in lista:
        notowania = yf.Ticker(spolka)
        dane_surowe = notowania.history(period="1mo")
        lista_surowych_danych_spolek.append(dane_surowe)
        if verbose:
            print(f"Pobrano dane surowych dla spółki {spolka}. Oto pierwsze 5 wierszy:\n{dane_surowe.head()}")
            nacisnij_enter_aby_kontynuowac()
    # todo - zapis danych surowych do pliku
    return lista_surowych_danych_spolek
    

def analiza(verbose) -> None:
    if verbose:
        print("Uruchomiono moduł analizatora danych\n")
        nacisnij_enter_aby_kontynuowac()
    naglowek()
    print("Analizator spółek")
    surowe_dane: list = pobranie_surowych_danych(wig, verbose)
    print(surowe_dane)
    # szukanie błędów
    # wyczyszczenie danych
    # raport o błędach
    # zapis danych wyczyszczonych do pliku
    # uzupełnieni danych o wskaźniki
    # zapis danych uzupełnionych do pliku
    nacisnij_enter_aby_kontynuowac()
    return None

analiza(verbose=True)
