import sys
sys.dont_write_bytecode = True #NO PYCHACHE

from flask import Flask, request, render_template, redirect, url_for
import backend
from backend import Favorites

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static') 

@app.route('/favorites/add', methods=['GET', 'POST'])
def add_favorite():
	imdb_id = request.args.get('imdb_id', None)
	display = request.args.get('test')
	if display == 1: # sjekk om det er en redirect fra details
		return "HEI"
	film_data = backend.hent_film_info(imdb_id)
	if film_data == 503:
		return "Feil ved henting av filminformasjon."
	
	# Save to favorites
	favorites.add_favorite(film_data)
	return redirect(url_for('favorites'))

@app.route('/favorites', methods=['GET'])
def favorites():
	return favorites.__str__()

@app.route('/result', methods=['GET'])
def result():
	search = request.args.get('query')
	film_data = backend.hent_sok(search)
	movies = [vars(movie) for movie in film_data[0]]
	series = [vars(serie) for serie in film_data[1]]
	return render_template('namesearch.html', title=search, movies=movies, series=series)

@app.route('/details', methods=['GET', 'POST'])
def details():
    # Perform any necessary actions here
    # You can use the button_id to determine which image to display
	imdb_id = request.args.get('imdb_id')
	film_data = backend.hent_film_info(imdb_id)
	if film_data == 503:
		return "Feil ved henting av filminformasjon."
	
	global last_search # Save object in case of add_favorite
	last_search = film_data # prevent unnecesary API calls

	if film_data.genre == "movie":
		return render_template('movie.html', data=vars(film_data))
	else:
		return render_template('serie.html', data=vars(film_data))

@app.route('/', methods=['GET', 'POST']) 
def index(): 
	if request.method == 'POST': 
		# retrieve text from the form
		namesearch = request.form.get('namesearch')
		idsearch = request.form.get('idsearch')

		if namesearch:
			return redirect(url_for('result', query=namesearch))
		
		if idsearch:
			# Print the text in terminal for verification 
			film_data = backend.hent_film_info(idsearch)
			return film_data.__str__() + 2*"<br>" + f'<img src="{film_data.poster}" alt="Poster">'

	return render_template('index.html', title='Filmsøk') 


if __name__ == '__main__': 
	favorites = Favorites()
	app.run()