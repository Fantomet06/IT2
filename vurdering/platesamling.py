# -*- coding: utf-8 -*-
# -- CLASSES -- #
class Eier:
    def __init__(self, navn):
        self.navn = navn
        self.platesamlinger = []

    def opprett_platesamling(self, navn:str, beskrivelse:str, opprettet:str):
        self.platesamlinger.append(Platesamling(navn, beskrivelse, opprettet))

class Platesamling:
    def __init__(self, navn:str, beskrivelse:str, opprettet:int):
        self.navn = navn
        self.beskrivelse = beskrivelse
        self.opprettet = opprettet
        self.albumer = []
        self.artister = {}
    
    def legg_til_album(self, navn:str, artist:str, utgitt:int, plateselskap:str, CD:bool, farge:str=None, hastighet:int=None):
        if "artist" not in self.artister:
            self.legg_til_artist(artist)
        _artist = self.artister[artist]
        if CD:
            obj = CD(navn, artist, utgitt, plateselskap)
        else:
            obj = Vinyl(navn, artist, utgitt, plateselskap, farge, hastighet)
        self.albumer.append(obj)
        _artist.albumer.append(obj)

    def legg_til_artist(self, navn:str):
        self.artister[navn] = Artist(navn)

    def vis_alle_album(self, artist=None):
        if artist:
            for x in self.artister[artist].albumer:
                print(x)
        else:
            for x in self.albumer:
                print(x)

    def vis_alle_artister(self):
        for x in self.artister:
            print(x)

class Artist:
    def __init__(self, navn:str):
        self.navn = navn
        self.albumer = []

    def vis_albumer(self):
        for x in self.albumer:
            print(x)

    def __str__(self) -> str:
        return f"Navn: {self.navn}\nAntall albumer: {len(self.albumer)}"

class Album:
    def __init__(self, navn:str, artist:str, utgitt:int, plateselskap:str):
        self.navn = navn
        self.artist = artist
        self.utgitt = utgitt
        self.plateselskap = plateselskap

    def vis_info(self):
        return f"Navn: {self.navn}\nArtist: {self.artist}\nUtgitt: {self.utgitt}\nPlateselskap: {self.plateselskap}"

class Vinyl(Album):
    def __init__(self, navn:str, artist:str, utgitt:int, plateselskap:str, farge: str, hastighet: int):
        super().__init__(navn, artist, utgitt, plateselskap)
        self.farge = farge
        assert hastighet in [33, 45], "Ugyldig hastighet. Hastighet må være 33 eller 45"
        self.hastighet = hastighet

    def __str__(self) -> str:
        return self.vis_info() + f"\nFarge: {self.farge}\nHastighet: {self.hastighet}"
    
class CD(Album):
    def __init__(self, navn: str, artist: str, utgitt: int, plateselskap: str):
        super().__init__(navn, artist, utgitt, plateselskap)
    
    def __str__(self) -> str:
        return self.vis_info()
