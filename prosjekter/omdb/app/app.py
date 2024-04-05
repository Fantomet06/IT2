import sys
sys.dont_write_bytecode = True #NO PYCHACHE

from flask import Flask, request, render_template 
import backend

app = Flask(__name__) 


@app.route('/', methods=['GET', 'POST']) 
def index(): 
	if request.method == 'POST': 
		# Retrieve the text from the textarea 
		namesearch = request.form.get('namesearch')
		idsearch = request.form.get('idsearch')

		if namesearch:
			# Print the text in terminal for verification 
			film_data = backend.hent_sok(namesearch)
			text = ""
			for film in film_data:
				text += film.__str__() + 2*"<br>"
			return text
		
		if idsearch:
			# Print the text in terminal for verification 
			film_data = backend.hent_film_info(idsearch)
			return film_data.__str__() + 2*"<br>" + f'<img src="{film_data.poster}" alt="Poster">'

	return render_template('index.html') 


if __name__ == '__main__': 
	app.run() 
