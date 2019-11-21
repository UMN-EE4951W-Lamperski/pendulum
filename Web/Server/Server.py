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
app.secret_key = "secret key"
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'py'])

PI_URL = 'http://localhost:8000'

RESULTS_DESTINATION = "Results/results.txt"

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
	
@app.route('/')
def upload_form():
	return render_template('upload.html')

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
			dictToSend = {'file_content':file.read()}
			file.close
			print('Running test')
			flash('Running test')
			response = requests.post(PI_URL + '/tests/endpoint', json=dictToSend)
			contents = json.loads(response.text)[u'results_content']
			flash('Response from server:' + contents)

			results = open(RESULTS_DESTINATION, "w")
			results.write(contents)
			results.close()

			return render_template('upload.html', results = 'True')
		else:
			flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')
			return redirect(request.url)

@app.route('/results', methods=['GET'])# this is a job for GET, not POST
def download():
	print("in downlaods")
	with open(RESULTS_DESTINATION, 'r') as results:
		results_content = results.read()
		results.close()
	print("results_content")
	return Response(
		results_content,
		mimetype="text/csv",
		headers={"Content-disposition":
					"attachment; filename=results.csv"})

if __name__ == "__main__":
    app.run(host="localhost", port=5000)