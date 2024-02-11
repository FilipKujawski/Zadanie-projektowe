class KontoBankowe:
    def __init__(self, saldo=0):
        self.saldo = saldo
        self.historia = []

    def sprawdz_saldo(self):
        return self.saldo

    def wplac_pieniadze(self, kwota):
        self.saldo += kwota
        self.historia.append(f'Wpłata: +{kwota} PLN')
        print(f'Wpłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN.')

    def wyplac_pieniadze(self, kwota):
        if kwota > self.saldo:
            print('Brak wystarczających środków.')
        else:
            self.saldo -= kwota
            self.historia.append(f'Wypłata: -{kwota} PLN')
            print(f'Wypłacono {kwota} PLN. Aktualne saldo: {self.saldo} PLN.')


class Uzytkownik:
    def __init__(self, imie, nazwisko, saldo=0):
        self.imie = imie
        self.nazwisko = nazwisko
        self.konto = KontoBankowe(saldo)

    def sprawdz_stan_konta(self):
        print(f"Wpisz imię i nazwisko: {self.imie} {self.nazwisko}")
        print(f"Saldo: {self.konto.sprawdz_saldo()} PLN")

    def wykonaj_operacje(self):
        while True:
            print("\nWybierz operację:")
            print("1. Sprawdź stan konta")
            print("2. Wpłać pieniądze")
            print("3. Wypłać pieniądze")
            print("0. Zakończ")

            operacja = input("Wpisz numer operacji: ")

            if operacja == '1':
                self.sprawdz_stan_konta()
            elif operacja == '2':
                kwota = float(input("Wprowadź kwotę do wpłacenia: "))
                self.konto.wplac_pieniadze(kwota)
            elif operacja == '3':
                kwota = float(input("Wprowadź kwotę do wypłacenia: "))
                self.konto.wyplac_pieniadze(kwota)
            elif operacja == '0':
                print("Zakończono.")
                break
            else:
                print("Nieprawidłowa operacja. Spróbuj ponownie.")


class Bank:
    def __init__(self):
        self.uzytkownicy = [
            Uzytkownik("Maryla", "Rodowicz", 100),
            Uzytkownik("Robert", "Makłowicz", 2000000),
            Uzytkownik("Justyna", "Steczkowska", 6507)
        ]

    def dodaj_uzytkownika(self, imie, nazwisko):
        nowy_uzytkownik = Uzytkownik(imie, nazwisko)
        self.uzytkownicy.append(nowy_uzytkownik)
        return f'Dodano nowego użytkownika: {imie} {nazwisko}.'

    def wybierz_uzytkownika(self):
        print("Dostępni użytkownicy:")
        for i, uzytkownik in enumerate(self.uzytkownicy):
            print(f"{i + 1}. {uzytkownik.imie} {uzytkownik.nazwisko}")

        numer_uzytkownika = int(input("Wybierz numer użytkownika: ")) - 1
        if 0 <= numer_uzytkownika < len(self.uzytkownicy):
            return numer_uzytkownika
        else:
            print("Nieprawidłowy numer użytkownika. Spróbuj ponownie.")
            return self.wybierz_uzytkownika()

    def obsluga_banku(self):
        while True:
            print("\nWybierz operację:")
            print("1. Dodaj nowego użytkownika")
            print("2. Wybierz użytkownika")
            print("0. Zakończ")

            operacja = input("Wpisz numer operacji: ")

            if operacja == '1':
                imie = input("Wprowadź imię nowego użytkownika: ")
                nazwisko = input("Wprowadź nazwisko nowego użytkownika: ")
                print(self.dodaj_uzytkownika(imie, nazwisko))
            elif operacja == '2':
                numer_uzytkownika = self.wybierz_uzytkownika()
                self.uzytkownicy[numer_uzytkownika].wykonaj_operacje()
            elif operacja == '0':
                print("Zakończono.")
                break
            else:
                print("Nieprawidłowa operacja. Spróbuj ponownie.")


# Przykładowe użycie
bank = Bank()
bank.obsluga_banku()
