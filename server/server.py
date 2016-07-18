import os
from flask import *
from flask.ext.cors import CORS, cross_origin
from werkzeug.utils import secure_filename
import network
import account_setting
import time


app = Flask(__name__)
app.secret_key = "super secret key"
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
UPLOAD_FOLDER = '/var/www/csvuploadfolder'
ALLOWED_EXTENSIONS = set(['csv'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
		return '.' in filename and \
				filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/snbcalc/login', methods=['POST'])
@cross_origin()
def login():
		username = request.form["username"]
		password = request.form["password"]
		account_setting.username = username
		account_setting.password = password
		if network.login():
			return json.dumps({"success": 'true'})
		else:
			return json.dumps({"success": 'false'})


@app.route('/snbcalc/uploadcsv', methods=['POST'])
@cross_origin()
def upload_csvfile():
		if request.method == 'POST':
				# check if the post request has the file part
				if 'file' not in request.files:
						flash('No file part')
						return json.dumps({"success": 'false', "message": "No file part"})
				file = request.files['file']
				# if user does not select file, browser also
				# submit a empty part without filename
				if file.filename == '':
						flash('No selected file')
						return json.dumps({"success": False, "message": "No selected file"})
				if file and allowed_file(file.filename):
						timestamp = int(time.mktime(time.localtime()))
						filename = "csv_" + str(timestamp) + ".csv"
						file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
						return json.dumps({"success": True, "filename": filename})
		return json.dumps({"success": False})


if __name__ == '__main__':
		app.run(host='123.56.176.38', port=8085)
