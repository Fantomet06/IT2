import time
class Person:
    """
    Klasse for å lage personer

    Attributer:
        fornavn(str): personens fornavn
        etternavn(str): personens etternavn
        fodselsar(int): personens fødselsår
    """
    def __init__(self, fornavn: str, etternavn: str, fodselsar: int):
        """Konstruktør for Person"""
        self.fornavn = fornavn
        self.etternavn = etternavn
        self.fodselsar = fodselsar

    def __str__(self) -> str:
        return f"""
fornavn: {self.fornavn} 
etternavn: {self.etternavn}
fodselsar: {self.fodselsar}
alder: {self.beregnAlder()}"""
    
    def visInfo(self):
        """Metode for å vise info om personen"""
        print(self.__str__())

    def beregnAlder(self) -> int:
        """Metode for å beregne alder"""
        return time.localtime().tm_year - self.fodselsar
    

def main():
    assert type(Person("Kajus", "Andreja", 2006)) == Person, "Person class is not defined"
    testPerson = Person("Kajus", "Andreja", 2006)
    testPerson.visInfo()

if __name__ == "__main__":
    main()