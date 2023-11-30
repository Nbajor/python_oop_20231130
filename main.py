from datetime import datetime, timedelta

class Szoba:
    def __init__(self, szobaszam, ar):
        self.szobaszam = szobaszam
        self.ar = ar

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 100)

    def __str__(self):
        return f"Egyagyas Szoba {self.szobaszam}"

class KetagyasSzoba(Szoba):
    def __init__(self, szobaszam):
        super().__init__(szobaszam, 150)

    def __str__(self):
        return f"Kétágyas Szoba {self.szobaszam}"

class Szalloda:
    def __init__(self, nev):
        self.nev = nev
        self.szobak = []

    def hozzaad_szoba(self, szoba):
        self.szobak.append(szoba)

class Foglalas:
    def __init__(self, szoba, datum):
        self.szoba = szoba
        self.datum = datum

class FoglalasKezelo:
    def __init__(self, szalloda):
        self.szalloda = szalloda
        self.foglalasok = []

    def foglalas(self, szoba, datum):
        if ellenoriz_datum(datum) and szoba not in [f.szoba for f in self.foglalasok]:
            foglalas = Foglalas(szoba, datum)
            self.foglalasok.append(foglalas)
            return f"Foglalás elkészült a szobára {szoba.szobaszam} dátummal {datum}. Ár: {szoba.ar}"
        elif not ellenoriz_datum(datum):
            return "Érvénytelen dátum!"
        else:
            return "A szoba már foglalt!"

    def lemondas(self, foglalas):
        if foglalas in self.foglalasok:
            self.foglalasok.remove(foglalas)
            return "Foglalás sikeresen lemondva."
        else:
            return "Érvénytelen foglalás."

    def listaz_foglalasok(self):
        return [f"Foglalás a szobára {foglalas.szoba.szobaszam} dátummal {foglalas.datum}" for foglalas in self.foglalasok]

def ellenoriz_datum(datum):
    return datum >= datetime.now()

def main():
    hotel = Szalloda("Lux Hotel")
    szoba1 = EgyagyasSzoba(101)
    szoba2 = KetagyasSzoba(201)
    szoba3 = EgyagyasSzoba(301)

    hotel.hozzaad_szoba(szoba1)
    hotel.hozzaad_szoba(szoba2)
    hotel.hozzaad_szoba(szoba3)

    foglalas_kezelo = FoglalasKezelo(hotel)

    # Foglalások feltöltése
    foglalas_kezelo.foglalas(szoba1, datetime(2023, 12, 1))
    foglalas_kezelo.foglalas(szoba2, datetime(2023, 12, 5))
    foglalas_kezelo.foglalas(szoba3, datetime(2023, 12, 8))


    #foglalas_kezelo.foglalas(szoba2, datetime(2023, 12, 9))
    #foglalas_kezelo.foglalas(szoba3, datetime(2023, 12, 16))

    while True:
        print("\n1. Foglalás")
        print("2. Lemondás")
        print("3. Foglalások listázása")
        print("0. Kilépés")

        valasztas = input("Válassz egy műveletet: ")

        if valasztas == "1":
            szoba_szam = input("Adja meg a foglalni kívánt szoba számát: ")
            datum_input = input("Adja meg a foglalás dátumát (YYYY-MM-DD): ")
            datum = datetime.strptime(datum_input, "%Y-%m-%d")

            szoba = next((sz for sz in hotel.szobak if sz.szobaszam == int(szoba_szam)), None)
            print(szoba)
            if szoba:
                eredmeny = foglalas_kezelo.foglalas(szoba, datum)
                print(eredmeny)
            else:
                print("Érvénytelen szoba szám.")

        elif valasztas == "2":
            foglalasok = foglalas_kezelo.listaz_foglalasok()
            for i, foglalas in enumerate(foglalasok, start=1):
                print(f"{i}. {foglalas}")

            lemondas_idx = int(input("Válassz foglalást lemondáshoz (sorszám): ")) - 1

            if 0 <= lemondas_idx < len(foglalasok):
                eredmeny = foglalas_kezelo.lemondas(foglalas_kezelo.foglalasok[lemondas_idx])
                print(eredmeny)
            else:
                print("Érvénytelen sorszám.")

        elif valasztas == "3":
            foglalasok = foglalas_kezelo.listaz_foglalasok()
            for foglalas in foglalasok:
                print(foglalas)

        elif valasztas == "0":
            break

        else:
            print("Érvénytelen választás. Kérlek, válassz újra.")

if __name__ == "__main__":
    main()
