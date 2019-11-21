#handle a POST request
from flask import Flask, render_template, request, url_for, jsonify
import subprocess
import os
app = Flask(__name__)

UPLOAD_DESTINATION = "Uploads/upload.py"

RESULTS_DESTINATION = "Results/results.txt"

@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    # Receive post
    input_json = request.get_json(force=True) 

    # Put file content into a file caled upload.py
    file_content=input_json['file_content']
    upload = open(UPLOAD_DESTINATION, "w")
    upload.write(file_content)
    upload.close()

    # Run python script
    subprocess.call(["python", UPLOAD_DESTINATION], shell=True)

    # Get results file
    with open(RESULTS_DESTINATION, 'r') as results:
        results_content = results.read()
        results.close()

    # subprocess.check_output(["echo", "Hello World!"])
    # os.remove(UPLOAD_DESTINATION)
    # os.remove(RESULTS_DESTINATION)

    # Return results file content
    dictToReturn = {'results_content':results_content}
    return jsonify(dictToReturn)

if __name__ == '__main__':
    app.run(host="localhost", port=8000)