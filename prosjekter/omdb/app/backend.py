import sys
sys.dont_write_bytecode = True #NO PYCHACHE

import settings
import requests
import requests

def hent_film_info(imdbID) -> object | int:
    """ Hente informasjon om et film"""
    url = settings.url + "&i=" + imdbID
    response = requests.get(url)
    # sjekker at HTTP request til API gikk bra.
    if not response.ok:
        print('Feil ved henting av filminformasjon.')
        return 503

    #sjekk at API kall gikk bra
    film_data = response.json()
    if film_data["Response"] == "False":
        print(film_data["Error"])
        return 503
    
    #hvis alt gikk bra
    if film_data["Type"] == "movie":
        return Movie(film_data)
    elif film_data["Type"] == "series":
        return Series(film_data)
    
def hent_sok(tittel) -> list | str:
    """
    Hente alle resultater fra søk
    Returnerer en linked list med filmer og serier
    [[Movie], [Series]]
    """
    url = settings.url + "&s=" + tittel
    response = requests.get(url)
    if response.status_code != 200:  # sjekker at HTTP request til API gikk bra.
        return 'Feil ved henting av filminformasjon.'

    film_data = response.json()
    if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
        return film_data["Error"]
    
    #hvis alt gikk bra, så sorterer vi filmer og serier
    results = [[],[]]
    for film in film_data["Search"]:
        if film["Type"] == "movie":
            results[0].append(AudiovisueltElement(film))
        elif film["Type"] == "series":
            results[1].append(AudiovisueltElement(film))
    return results
    
class AudiovisueltElement:
    def __init__(self, data: dict[str, str]):
        self.title = data.get("Title")
        self.year = data.get("Year")
        self.imdb_id = data.get("imdbID")
        self.poster = data.get("Poster")
        self.genre = data.get("Type")
        #self.id = id
        self.ratings = [] #TODO

    def __str__(self) -> str:
        return f"""
        Tittel: {self.title}
        År: {self.year}
        Type: {self.genre}
        {'imdbID: ' + self.imdb_id if self.imdb_id else ''}
        """

class Movie(AudiovisueltElement):
    """ Klasse for å representere en film. """
    def __init__(self, data: dict[str, str]):
        super().__init__(data)
        self.DVD = data.get("DVD")
        self.production = data.get("Production")
        self.website = data.get("Website")

class Series(AudiovisueltElement):
    """ Klasse for å representere en serie. """
    def __init__(self, data: dict[str, str]):
        super().__init__(data)
        self.total_seasons = data.get("totalSeasons")

class Favorites:
    def __init__(self):
        self.favorites = [[],[]] # [[Movie], [Series]]

    def add_favorite(self, favorite):
        if favorite.genre == "movie":
            self.favorites[0].append(favorite)
        else:
            self.favorites[1].append(favorite)

    def remove_favorite(self, favorite):
        self.favorites.remove(favorite)

    def get_favorites(self):
        return self.favorites

    def __str__(self):
        return str([vars(favorite) for favorite in self.favorites])