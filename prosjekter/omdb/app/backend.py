import sys
sys.dont_write_bytecode = True #NO PYCHACHE

import settings
import requests
import requests

def hent_film_info(imdbID):
    """ Hente informasjon om et film"""
    url = settings.url + "&i=" + imdbID
    response = requests.get(url)
    if response.status_code == 200:  # sjekker at HTTP request til API gikk bra.
        film_data = response.json()
        if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
            print(film_data["Error"])
            return 
        return Movie(film_data["Title"], film_data["Year"], film_data["Type"], film_data["imdbID"], film_data["Poster"])
    else:
        print('Feil ved henting av filminformasjon.')
        return None
    
def hent_sok(tittel) -> list:
    """
    Hente alle resultater fra søk
    Returnerer en linked list med filmer og serier
    [[Movie], [Series]]
    """
    url = settings.url + "&s=" + tittel
    response = requests.get(url)
    if response.status_code == 200:  # sjekker at HTTP request til API gikk bra.
        film_data = response.json()
        if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
            print(film_data["Error"])
            return 
        else:
            results = [[],[]]
            for i in film_data["Search"]:
                if i["Type"] == "movie":
                    results[0].append(Movie(i["Title"], i["Year"], i["imdbID"], i["Poster"]))
                elif i["Type"] == "series":
                    results[1].append(Series(i["Title"], i["Year"], i["imdbID"], i["Poster"]))
            return results
    else:
        print('Feil ved henting av filminformasjon.')
        return None
    
class AudiovisueltElement:
    def __init__(self, title, year, imdb_id, poster):
        self.title = title
        self.year = year
        self.imdb_id = imdb_id
        self.poster = poster
        self.id = id
        self.ratings = [] #TODO

    def __str__(self):
        return f"""
        Tittel: {self.title}
        År: {self.year}
        Type: {self.genre}
        {'imdbID: ' + self.imdb_id if self.imdb_id else ''}
        """

class Movie(AudiovisueltElement):
    """ Klasse for å representere en film. """
    def __init__(self, title, year, imdb_id, poster):
        super().__init__(title, year, imdb_id, poster)

class Series(AudiovisueltElement):
    """ Klasse for å representere en serie. """
    def __init__(self, title, year, imdb_id, poster):
        super().__init__(title, year, imdb_id, poster)