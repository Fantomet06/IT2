import sys
sys.dont_write_bytecode = True #NO PYCHACHE

from flask import Flask, request, render_template, redirect, url_for
import backend

app = Flask(__name__,template_folder='./frontend/templates',static_folder='./frontend/static') 

@app.route('/result', methods=['GET', 'POST'])
def result():
	search = request.args.get('query')
	film_data = backend.hent_sok(search)
	movies = [vars(movie) for movie in film_data[0]]
	series = [vars(serie) for serie in film_data[1]]
	return render_template('namesearch.html', title='Filmsøk', movies=movies, series=series)

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
	app.run() 
