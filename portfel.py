from obsluga import naglowek, nacisnij_enter_aby_kontynuowac, wyczysc_ekran

def konto(verbose) -> None:
    if verbose:
        print("Uruchomiono moduł obsługi portfela\n")
        nacisnij_enter_aby_kontynuowac()
    naglowek()
    print("Portfel")
    nacisnij_enter_aby_kontynuowac()
    return 0
