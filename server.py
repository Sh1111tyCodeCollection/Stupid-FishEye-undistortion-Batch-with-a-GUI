from flask import Flask,request,send_from_directory
import urllib
import os
import json
static_url_path=''


app = Flask(__name__)

@app.route('/html/example', defaults=dict(filename=None))
@app.route('/<path:filename>', methods=['GET', 'POST'])
def index(filename):
    filename = filename or 'index.html'
    if request.method == 'GET':
        return send_from_directory('./html/example/', filename)
    return jsonify(request.data)

@app.route('/transferimage',methods=['POST'])
def transferimage():
	imageData = request.form.get('image')
	filename = request.form.get('file_name')
	response = urllib.request.urlopen(imageData)
	with open('export/calibrated_'+filename, 'wb') as f:
    		f.write(response.file.read())
	return 'image saved'

@app.route('/list',methods=['GET'])
def listAllImages():
	arr = os.listdir('html/example/data')
	jsonStr = json.dumps(arr)
	return jsonStr


app.run(host = 'localhost', debug = True,port=5000)