import json

class AudiovisueltElement:
    def __init__(self, data: dict[str, str]):
        # match variable name with json key
        self.Title = data.get("Title")
        self.Year = data.get("Year")
        self.imdbID = data.get("imdbID")
        self.Poster = data.get("Poster")
        self.Type = data.get("Type")
        #self.id = id
        self.Ratings = [] #TODO

    def __str__(self) -> str:
        return f"Tittel: {self.Title}, År: {self.Year}"

class Movie(AudiovisueltElement):
    """ Klasse for å representere en film. """
    def __init__(self, data: dict[str, str]):
        super().__init__(data)
        self.DVD = data.get("DVD")
        self.Production = data.get("Production")
        self.Website = data.get("Website")

class Series(AudiovisueltElement):
    """ Klasse for å representere en serie. """
    def __init__(self, data: dict[str, str]):
        super().__init__(data)
        self.totalSeasons = data.get("totalSeasons")

class Favorites:
    """ Klasse for å representere favoritter."""
    def __init__(self):
        self.favorites = [[],[]] # [[Movie], [Series]]

    def load_favorites(self, exit):
        """ Henter favoritter fra fil eller lagrer til fil"""
        try:
            if exit:
                with open("favorites.json", "w") as f:
                    string_dicts = {"movies": [], "series": []}
                    string_dicts["movies"] = [vars(movie) for movie in self.favorites[0]]
                    string_dicts["series"] = [vars(serie) for serie in self.favorites[1]]
                    
                    json.dump(string_dicts, f)

            else:
                with open("favorites.json", "r") as f:
                    data = json.load(f)
                    for movie in data["movies"]:
                        self.favorites[0].append(Movie(movie))
                    for serie in data["series"]:
                        self.favorites[1].append(Series(serie))
       
        except Exception as e:
            print(e)

    def add_favorite(self, favorite):
        if favorite.Type == "movie":
            self.favorites[0].append(favorite)
        else:
            self.favorites[1].append(favorite)
        
    def remove_favorite(self, imdb_id) -> str:
        """Fjern favoritt basert på imdb_id"""
        for fav in self.favorites[0]:
            if fav.imdbID == imdb_id:
                self.favorites[0].remove(fav)
                return "Favoritt fjernet."
        
        for fav in self.favorites[1]:
            if fav.imdbID == imdb_id:
                self.favorites[1].remove(fav)
                return "Favoritt fjernet."
            
        return "Ikke en favoritt."
    def get_favorites(self) -> list:
        movies = [vars(movie) for movie in self.favorites[0]]
        series = [vars(serie) for serie in self.favorites[1]]
        return movies, series
    
    def in_favorites(self, favorite) -> bool:
        movies, series = self.get_favorites()
        return vars(favorite) in movies or vars(favorite) in series 

    def __str__(self) -> str:
        return str([vars(favorite) for favorite in self.favorites])