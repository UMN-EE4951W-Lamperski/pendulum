#handle a POST request
from flask import Flask, render_template, request, url_for, jsonify
import subprocess
import os
import RPi.GPIO as GPIO
app = Flask(__name__)

UPLOAD_DESTINATION = "Uploads/ee4951W_pendulum_web/app/app/FileProcessing/Uploads"
SYSTEM_DESTINATION = "System/"
RESULTS_DESTINATION = "Uploads/ee4951W_pendulum_web/app/app/FileProcessing/Results"

INITIALIZE_SYSTEM = "initialize_system.py"

@app.route('/')
def home():
    return "ANDI'S PIE"

@app.route('/tests/endpoint', methods=['POST'])
def my_test_endpoint():
    # Receive post
    input_json = request.get_json(force=True) 

    # Put file content into a file caled upload.py
    filename=input_json['filename'].encode("ascii")
    file_content=input_json['file_content'].encode("ascii")
    filename=input_json['filename']
    file_content=input_json['file_content']
    upload = open(UPLOAD_DESTINATION + filename, "w+")
    upload.write(file_content)
    upload.close()

    # Run python script
    process = subprocess.Popen(["python3", UPLOAD_DESTINATION + filename])
    try:
        process.wait()
        print("Program exited normally!\n")
    except:
        print("Exception occurred running program!\n")
        process.terminate()
    finally:
        GPIO.cleanup()

    # Get results file
    results_filename = filename.split(".")[0]
    results_filename = results_filename + "_results.csv"
    with open(RESULTS_DESTINATION + results_filename, 'r') as results:
        results_content = results.read()
        results.close()
    
    # Remove test file and results file now that were done with them
    os.remove(UPLOAD_DESTINATION + filename)
    os.remove(RESULTS_DESTINATION + results_filename)

    # Return results file content
    dictToReturn = {'results_filename':results_filename, 'results_content':results_content}
    return jsonify(dictToReturn)

# This will run on system bootup.
if __name__ == '__main__':
    os.chdir('/home/pi/pendulum')
    # Initialize the system before accepting any files.
    subprocess.call(["python3", SYSTEM_DESTINATION + INITIALIZE_SYSTEM])
    # Run the web client to start receiving files.
    app.run(host="192.168.1.10", port=8000)
