import os

def naglowek() -> None:
    wyczysc_ekran()
    print(30 * "*" + " Doradca " + 30 * "*")
    print(69 * "*" + "\n")
    return None

def funkcja_w_produkcji() -> None:
    wyczysc_ekran()
    naglowek()
    print("\nModuł programu jest jeszcze w produkcji !!!")
    nacisnij_enter_aby_kontynuowac()
    return None

def nacisnij_enter_aby_kontynuowac() -> None:
    input("\nNaciśnij Enter aby kontynuować")
    return None

def wyczysc_ekran() -> None:
    os.system("clear")
    return None
