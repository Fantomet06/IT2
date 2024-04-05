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
        return Result(film_data["Title"], film_data["Year"], film_data["Type"], film_data["imdbID"], film_data["Poster"])
    else:
        print('Feil ved henting av filminformasjon.')
        return None
    
def hent_sok(tittel):
    """ Hente alle resultater fra søk"""
    url = settings.url + "&s=" + tittel
    response = requests.get(url)
    if response.status_code == 200:  # sjekker at HTTP request til API gikk bra.
        film_data = response.json()
        if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
            print(film_data["Error"])
            return 
        else:
            results = []
            for i in film_data["Search"]:
                results.append(Result(i["Title"], i["Year"], i["Type"], i["imdbID"]))
            return results
    else:
        print('Feil ved henting av filminformasjon.')
        return None
    
class Result:
    def __init__(self, title, year, type, imdb_id=None, poster=None):
        self.title = title
        self.year = year
        self.genre = type
        self.imdb_id = imdb_id
        self.poster = poster
    
    def __str__(self):
        return f"""
        Tittel: {self.title}
        År: {self.year}
        Type: {self.genre}
        {'imdbID: ' + self.imdb_id if self.imdb_id else ''}
        """
    
class AudiovisueltElement:
    def __init__(self, title, year, imdb_id, poster, id):
        self.title = title
        self.year = year
        self.imdb_id = imdb_id
        self.poster = poster
        self.id = id
        self.ratings = [] #TODO

class Movie(AudiovisueltElement):
    """ Klasse for å representere en film. """
    def __init__(self, title, year, imdb_id, poster, id):
        super().__init__(title, year, imdb_id, poster, id)

class Series(AudiovisueltElement):
    """ Klasse for å representere en serie. """
    def __init__(self, title, year, imdb_id, poster, id):
        super().__init__(title, year, imdb_id, poster, id)