from flask import Flask, render_template, request
from fastai import *
from fastai.vision import *
app = Flask(__name__)

learn = load_learner('model/')

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(f.filename)
      img = open_image(f.filename)
      prediction = learn.predict(img)[0]
      return 'Prediction for ' + f.filename + ' = ' + str(prediction)
		
if __name__ == '__main__':
   app.run(debug = True)