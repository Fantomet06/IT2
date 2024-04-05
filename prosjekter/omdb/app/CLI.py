import sys
sys.dont_write_bytecode = True #NO PYCHACHE

import backend

class App:
    def __init__(self):
        # spare på siste søk her
        pass

    def print_valg(self):
        print("""
                Her kan du søke informasjon om filmer!
                1. Søk etter en film
                2. Hent informasjon om en film
                x. Avslutt
            """)
        
    def run(self):
        while True:
            self.print_valg()
            valg = input("Velg et alternativ: ")

            match valg:
                case "1":
                    film_tittel = input('Skriv inn tittelen på filmen: ')
                    film_data = backend.hent_sok(film_tittel)  
                    for i in film_data:
                        print(i)

                case "2":
                    film_tittel = input('Skriv inn imdb id på filmen: ')
                    film_data = backend.hent_film_info(film_tittel)
                    print(film_data)
                case "x":
                    print("Avslutter...")
                    break
                case _:
                    print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    app = App()
    app.run()