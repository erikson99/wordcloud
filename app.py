from flask import Flask, render_template, request
#import pandas as pd
#from PySripts.pandas_implementation import *
#from PySripts.df_text import *
from PySripts.wordcloud_generator import *
from pathlib import Path


app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')


@app.route('/', methods = ['POST'])
def upload_file():
	if request.method == 'POST':
		# input file
		f = request.files['file']
		f2 = request.files['file2']
		# decodes utf-8 into a python string 
		decoded = f.read().decode('utf-8')
		
		# Gets a string of all chats from the DataFrame and using that string to create a
		# wordcloud image and show it on index.hmtl
		# txt = df_to_text(Data_extracted)
		txt = decoded.replace('\n', '')
		img = np.array(Image.open(f2))
		wc_created = create_wc(txt, img)
		return render_template('index.html', plot=1, url ='/static/WordCloud.png')

@app.after_request
def add_header(response):
	"""
		Add headers to both force latest IE rendering engine or Chrome Frame,
		and also to cache the rendered page for 10 minutes.
		"""
	response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
	response.headers['Cache-Control'] = 'public, max-age=0'
	return response

