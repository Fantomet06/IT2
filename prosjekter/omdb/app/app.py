import sys
sys.dont_write_bytecode = True #NO PYCHACHE

from flask import Flask, request, render_template, redirect, url_for
import backend
from backend import Favorites

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static') 

@app.route('/favorites/add', methods=['GET', 'POST'])
def add_favorite():
	imdb_id = request.args.get('imdb_id')
	redir = request.args.get('redirect')
	if redir == "1": # sjekk om det er en redirect fra details
		film_data = last_search
	else:
		film_data = backend.hent_film_info(imdb_id)

	if film_data == 503:
		return "Feil ved henting av filminformasjon."

	if Favorites.in_favorites(film_data):
		return redirect(url_for('favorites'))
	
	# Save to favorites
	Favorites.add_favorite(film_data)
	return redirect(url_for('favorites'))

@app.route('/favorites/remove', methods=['GET', 'POST'])
def remove_favorite():
	imdb_id = request.args.get('imdb_id')
	Favorites.remove_favorite(imdb_id)
	return redirect(url_for('favorites'))

@app.route('/favorites', methods=['GET'])
def favorites():
	movies, series = Favorites.get_favorites()
	return render_template('favorites.html', movies=movies, series=series)

@app.route('/result', methods=['GET'])
def result():
	try:
		search = request.args.get('query')
		film_data = backend.hent_sok(search)
		
		movies = [vars(movie) for movie in film_data[0]]
		series = [vars(serie) for serie in film_data[1]]
		return render_template('namesearch.html', title=search, movies=movies, series=series)
	except:
		return "Ingen film(er) funnet."

@app.route('/details', methods=['GET', 'POST'])
def details():
	try:
		imdb_id = request.args.get('imdb_id')
		film_data = backend.hent_film_info(imdb_id)
		
		global last_search # Save object in case of add_favorite
		last_search = film_data # prevent unnecesary API calls

		if film_data.genre == "movie":
			return render_template('movie.html', data=vars(film_data))
		else:
			return render_template('serie.html', data=vars(film_data))
		
	except:
		return "Feil ved henting av filminformasjon."

@app.route('/', methods=['GET', 'POST']) 
def index(): 
	if request.method == 'GET':
		return render_template('index.html', title='Filmsøk')
	
	# retrieve text from the form
	namesearch = request.form.get('namesearch')
	idsearch = request.form.get('idsearch')

	if namesearch:
		return redirect(url_for('result', query=namesearch))
	
	if idsearch:
		return redirect(url_for('details', imdb_id=idsearch))

	 


if __name__ == '__main__': 
	Favorites = Favorites()
	app.run()