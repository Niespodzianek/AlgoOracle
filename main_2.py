from obsluga import naglowek, nacisnij_enter_aby_kontynuowac, wyczysc_ekran
from portfel import konto
from analizator import analiza
import sys

wynik: bool
komentarz: str

def program(verbose=False) -> tuple:
    if verbose:
        print("Program Wita Michasia !!!\nProgram uruchomiony, wyświetla nagłówek i główne menu")
        nacisnij_enter_aby_kontynuowac()
    program_pracuje = True
    while program_pracuje:
        naglowek()
        menu = input("Wybierz opcję głównego menu:\n\n(1) Analizator spółek\n(2) Obsługa portfela\n(9) Pomoc\n(Q) Koniec\n\nTwój wybór to: ")
        if menu == "1":
            if verbose:
                print("\nUruchamiam moduł analizatora danych")
                nacisnij_enter_aby_kontynuowac()
            analiza(verbose=verbose)
        elif menu == "2":
            if verbose:
                print("\nUruchamiam moduł obsługi portfela")
                nacisnij_enter_aby_kontynuowac()
            konto(verbose=verbose)
        elif menu == "Q" or menu == "q":
            program_pracuje = False
        else:
            print("\nCoś poszło nie tak !!!")
            nacisnij_enter_aby_kontynuowac()
    return True, "Program żegna Michasia !!!\nDo zobaczenia !!!"

if __name__ == "__main__":
    wynik, komentarz = program(verbose=True)
    if wynik:
        wyczysc_ekran()
        print(komentarz)
        sys.exit()
    else:
        print("Coś poszło nie tak !!! Do zobaczenia")
        sys.exit()
