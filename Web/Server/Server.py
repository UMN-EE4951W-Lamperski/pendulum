import os
try: #python3
    from urllib.request import urlopen
except: #python2
    from urllib2 import urlopen
from flask import Flask, flash, request, redirect, render_template, Response
from werkzeug.utils import secure_filename
import requests
import json

app = Flask(__name__)
app.secret_key = "ski u mah"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['py'])

PI_URL = 'http://localhost:8000'

RESULTS_DESTINATION = "Results/results.txt"

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def home():
	return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
        # Check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)

		# Grab the file
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)

		# Send the file content as a post to the PI
		if file and allowed_file(file.filename):

			dictToSend = {'filename':file.filename, 'file_content':file.read()}
			file.close
			print('Running test')
			flash('Running test')
			response = requests.post(PI_URL + '/tests/endpoint', json=dictToSend)
			
			results_filename = json.loads(response.text)[u'results_filename'].encode("ascii")
			results_content = json.loads(response.text)[u'results_content'].encode("ascii")
			flash('Results file:' + results_filename)
			flash('Response from server:' + results_content)
			
			results = open(RESULTS_DESTINATION, "w")
			results.write(results_content)
			results.close()

			return render_template('index.html', results = 'True')
		else:
			flash('Allowed file types are .py')
			return redirect(request.url)

@app.route('/results', methods=['GET'])
def download():
	# Grab content from results file
	with open(RESULTS_DESTINATION, 'r') as results:
		results_content = results.read()
		results.close()

	# Put content as a download file 
	return Response(
		results_content,
		mimetype="text/csv",
		headers={"Content-disposition":
					"attachment; filename=results.csv"})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)