from flask import Flask, render_template, request
from keras.models import load_model
from keras.preprocessing import image
from sklearn import metrics
from werkzeug.utils import secure_filename
import numpy as np

app = Flask(__name__,template_folder='template')
dic = {0 : 'melanoma', 1 : 'basal cell carcinoma', 2 : 'squamous cell carcinoma'}

model = load_model('model.h5')
model.make_predict_function()

def modelPrediction(img_path):
	img = image.load_img(img_path, target_size=(100,100))
	img = image.img_to_array(img)/255.0
	img = img.reshape(1, 100,100,3)
	predict_x=model.predict(img)
	p=np.argmax(predict_x,axis=1)
	return dic[p[0]]

@app.route("/", methods=['GET', 'POST'])
def main():
	return render_template("index.html")

@app.route("/submit", methods = ['GET', 'POST'])
def output():
	if request.method == 'POST':
		img = request.files['my_image']

		img_path = "static/" + img.filename	
		img.save(img_path)
		p = modelPrediction(img_path)
	return render_template("index.html", prediction = p, img_path = img_path)
if __name__ =='__main__':
	app.run(debug = True)
