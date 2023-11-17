import random
import os

class bank:
    def __init__(self, fornavn: str, etternavn: str, saldo:int=0):
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.saldo = saldo
        self.kontonummer = random.randint(10000000,999999999999)
        #self.kontonummer = random.randint(1,3) # for testing
    
    def __str__(self):
        return(f"""
                Etternavn: {self.etternavn}
                Fornavn: {self.fornavn}
                Kontonummer: {self.kontonummer}
                Saldo: {self.saldo}
              """)

    def setteInn(self, x):
        self.saldo += x
    
    def taUt(self, x):
        self.saldo -= x

# -- BSU --
class BSU(bank):
    """
    Klasse som arver fra bank, sørger for at BSU kontoer har maks innskudd
    """
    def __init__(self, fornavn: str, etternavn: str, maksInnskudd: int, saldo: int):
        super().__init__(fornavn, etternavn, saldo)
        self.maksInnskudd = maksInnskudd
    
    def innskudd(self, x): # x er hvor mye som skal settes inn
        if x > self.maksInnskudd: x = self.maksInnskudd
        self.setteInn(x)

    """
    def setteInn(self, x):
        if x > self.maksInnskudd: x = self.maksInnskudd
        self.saldo += x
    """

# -- SPAREKONTO --
class Sparekonto(bank):
    """
    Klasse som arver fra bank, sørger for at sparekontoer har maks uttak
    """
    def __init__(self, fornavn: str, etternavn: str, maksUttak: int, saldo: int):
        super().__init__(fornavn, etternavn, saldo)
        self.maksUttak = maksUttak

    def uttak(self, x): # x er hvor mye som skal tas ut
        if x > self.maksUttak: x = self.maksUttak
        self.taUt(x)



def _intInput(out: str, valid: list) -> int:
    while True:
        try:
            valg = int(input(out))
            if valg in valid:
                return valg
            elif len(valid) == 0:
                return valg
            else: print("Skriv inn noe gyldig!")
        except: print("Skriv inn noe gyldig!")

def nyKonto(kontoer):
    os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
    type = _intInput("""
                    Hva slags konto?
                    1: BSU
                    2: Sparekonto
                    > """, [1, 2])
    if type == 1:
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        maksInnskudd = _intInput("Maks Innskudd: ", [])
        startSaldo = _intInput("Startsaldo: ", [])
        nyKonto = BSU(fornavn, etternavn, maksInnskudd, startSaldo)
        kontoer[nyKonto.kontonummer] = nyKonto

    if type == 2:
        fornavn = input("Fornavn: ")
        etternavn = input("Etternavn: ")
        maksUttak = _intInput("Maks Uttak: ")
        startSaldo = _intInput("Startsaldo: ")
        nyKonto = Sparekonto(fornavn, etternavn, maksUttak, startSaldo)
        kontoer[nyKonto.kontonummer] = nyKonto
    
    print(nyKonto)
    return kontoer

def main():
    kontoer = {"123": BSU("adi", "bardari", 100, 10)}
    assert kontoer["123"].saldo == 10, "Feil ved opprettelse"

    while True:
        os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
        valg = _intInput("""
                            Hva vil du gjøre?
                            1: Legge til ny konto
                            2: Se konto
                            3: Innskudd/Uttak
                            4: Avslutt
                            > """, [1, 2, 3, 4])
        
        # -- NY KONTO --
        if valg == 1:
            kontoer = nyKonto(kontoer)
            if (len(input("Skriv inn noe for å fortsette: ")) > 0): continue

        # -- SE KONTO --
        if valg == 2:
            try:
                os.system('cls' if os.name == 'nt' else 'clear') #clear terminal
                konto = _intInput("Kontonummer: ", [])
                print(kontoer[konto])
            except: print("Fant ikke konto.")
            if (len(input("Skriv inn noe for å fortsette: ")) > 0): continue

        # -- INNSKUDD/UTTAK --
        if valg == 3: # ikke ferdig
            continue

        # -- AVSLUTT --
        if valg == 4:
            break

if __name__ == "__main__":
    main()