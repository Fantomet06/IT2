import datetime
import random

class Person:
    """
    Klasse for å representere en person.
    """

    def __init__(self, fornavn, etternavn, fødselsår: int):
        """
        Attributer:
            fornavn (str): The first name of the person.
            etternavn (str): The last name of the person.
            fødselsår (int): The birth year of the person.
        """
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fødselsår = fødselsår

    def beregnAlder(self):
        return datetime.datetime.now().year - self.fødselsår
    
    def visInfo(self):
        return f"{self.fornavn} {self.etternavn} er {self.beregnAlder()} år gammel."
    
    def __str__(self):
        return self.visInfo()

class Elev(Person):
    """Klasse som lager en elev"""
    def __init__(self, fornavn, etternavn, fødselsår: int):
        super().__init__(fornavn, etternavn, fødselsår)

    def finnTrinn(self):
        trinn = {16: "vg 1", 17: "vg 2", 18: "vg 3"}
        try:
            return trinn[self.beregnAlder()]
        except:
            return "ukjent trinn"
    
    def visInfo(self):
        return super().visInfo() + f" Han/hun går i {self.finnTrinn()}."
    
    def __str__(self):
        return self.visInfo()
    
class Lærer(Person):
    """Klasse som lager en lærer"""
    def __init__(self, fornavn, etternavn, fødselsår: int, fag: list = []):
        super().__init__(fornavn, etternavn, fødselsår)
        self.fag = [x.lower() for x in fag]
    
    def sjekkFag(self, _fag):
        return _fag.lower() in self.fag
    
    def visInfo(self):
        return super().visInfo() + f" Han/hun underviser i {self.fag}."
    
class Klasse():
    """Klasse som lager en skoleklasse"""
    def __init__(self, navn: str, kontaktlærer: str):
        self.klassenavn = navn
        self.kontaktlærer = kontaktlærer
        self.elever = []

    def leggTilKontaktlærer(self, nylærer):
        self.kontaktlærer = nylærer
        return "Oppdatert kontaktlærer"
    
    def leggTilElever(self, elever):
        if type(elever) == list:
            for x in elever:
                self.elever.append(x)
        else:
            self.elever.append(x)

    def visElever(self):
        elever = []
        for x in self.elever:
            elever.append(x.fornavn)
        maksLengde = len(max(elever, key=len))+2
        for i in range(len(elever)):
            print("+"+"-"*maksLengde+"+")
            print(f"| {elever[i]}" + " "*(maksLengde-1-len(elever[i])) +"|")
        print("+"+"-"*maksLengde+"+")

    def visInfo(self):
        print(f"KLASSE {self.navn}")
        self.visElever()
        print(f"Kontaktlærer: {self.kontaktlærer}")

def main():
    """Funksjon for testing av kode"""
    navn = ["Ola", "Per", "Kari", "Niklas", "Sebastian", "David", "Daniel", "John"]
    etternavn = ["Hansen", "Olsen", "Johansen", "Pedersen", "Larsen", "Andersen", "Nilsen", "Kristiansen"]

    elever = []
    for i in range(4):
        elever.append(Elev(random.choice(navn), random.choice(etternavn), random.randint(2000, 2003)))

    obj = Klasse("3A", Lærer("Ola", "Hansen", 1980, ["Matte", "Norsk", "Engelsk"]))
    obj.leggTilElever(elever)
    obj.visInfo()

    lærer = Lærer("Ola", "Hansen", 1980, ["Matte", "Norsk", "Engelsk"])
    lærer.visInfo()

if __name__ == "__main__":
    main() #kun kjør main dersom denne filen blir direkte kjørt