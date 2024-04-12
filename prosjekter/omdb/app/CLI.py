import sys
sys.dont_write_bytecode = True #NO PYCHACHE

import backend
from klasser import Favorites


class App:
    def __init__(self):
        self.last_search = []

    def print_valg(self):
        print("""
                Her kan du søke informasjon om filmer!
                1. Søk etter en film
                2. Hent informasjon om en film
                3. Legg til i favoritter
                4. Fjern fra favoritter
                5. Vis favoritter
                x. Avslutt
            """)
        
    def print_filmer(self, film_data=None):
        if not film_data:
            print("Favoritter:")
            movies, series = Favorites.get_favorites()
        else:
            movies = film_data[0]
            series = film_data[1]
        
        count = 0
        viste = []
        print("Filmer:")
        for movie in movies:
            print(f"{count}, {movie}")
            viste.append(movie)
            count += 1
        print("Serier:")
        for serie in series:
            print(f"{count}, {serie}")
            viste.append(serie)
            count += 1
        return viste

    def run(self):
        while True:
            self.print_valg()
            valg = input("Velg et alternativ:\n> ")

            match valg:
                # Søke etter filmer
                case "1":
                    #hente film
                    film_tittel = input('Skriv inn tittelen på filmen:\n> ')
                    film_data = backend.hent_sok(film_tittel)

                    #vise resultater
                    print(f"Resultater for '{film_tittel}'") 
                    self.last_search = self.print_filmer(film_data)

                # Hente informasjon om en film
                case "2":
                    if not self.last_search:
                        print("Søk etter en film først")
                    else:
                        valg = input("Skriv inn nr på film/serie:\n> ")
                        film = self.last_search[int(valg)]
                        print(vars(film)) # TODO: add better print
                
                # Legge til favoritter
                case "3":
                    if not self.last_search:
                        print("Søk etter en film først")
                    else:
                        valg = input("Skriv inn nr på film/serie:\n> ")
                        Favorites.add_favorite(self.last_search[int(valg)])
                        print("Film/serie lagt til i favoritter!")

                # Fjerne favoritter
                case "4":
                    viste = self.print_filmer()

                    valg = int(input("Skriv inn nr på film/serie:\n> "))
                    Favorites.remove_favorite(viste[int(valg)]["imdbID"])
                    print("Film/serie fjernet fra favoritter!")

                # Vise favoritter
                case "5":
                    self.print_filmer()

                # Avslutte
                case "x":
                    print("Avslutter...")
                    Favorites.load_favorites(True)
                    break
                case _:
                    print("Ugyldig valg. Prøv igjen.")

if __name__ == "__main__":
    Favorites = Favorites()
    Favorites.load_favorites(False) # Load favorites from file
    app = App()
    app.run()