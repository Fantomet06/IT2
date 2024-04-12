import sys
sys.dont_write_bytecode = True #NO PYCHACHE

import configs.settings as settings
import requests
import requests
from klasser import AudiovisueltElement, Movie, Series

def hent_film_info(imdbID) -> object | int:
    """ Hente informasjon om et film"""
    url = settings.url+"&i="+imdbID
    response = requests.get(url)
    # sjekker at HTTP request til API gikk bra.
    if not response.ok:
        print('Feil ved henting av filminformasjon. - API nede?')
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
    Henter alle resultater fra søk
    Returnerer en linked list med filmer og serier
    [[Movie], [Series]]
    """
    url = settings.url + "&s=" + tittel
    response = requests.get(url)
    if response.status_code != 200:  # sjekker at HTTP request til API gikk bra.
        return 'Feil ved henting av filminformasjon.'

    film_data = response.json()
    if film_data["Response"] == "False":   #sjekker om OMDb API tjeneste kall gikk bra.
        return 404
    
    #hvis alt gikk bra, så sorterer vi filmer og serier
    results = [[],[]]
    for film in film_data["Search"]:
        if film["Type"] == "movie":
            results[0].append(AudiovisueltElement(film))
        elif film["Type"] == "series":
            results[1].append(AudiovisueltElement(film))
    return results

