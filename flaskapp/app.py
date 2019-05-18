from flask import Flask, render_template, request, make_response
from fastai import *
from fastai.vision import *
import os
IMG_FOLDER = '/static'
app = Flask(__name__)
app.config['IMG_FOLDER'] = IMG_FOLDER
learn = load_learner('model/')

@app.route('/upload')
def upload():
   return render_template('upload.html')
	
@app.route('/result', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save('static/img.jpg')
      f.close()
      img = open_image('static/img.jpg')
      prediction = learn.predict(img)[0]
      template = open('templates/result.html', 'w')
      content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Result</title>
    <style>

        .wrapper {
            height: 600px;
            position: relative;
        }

        .container {
            margin: 0;
            position: absolute;
            top: 50%;
            left: 50%;
            -ms-transform: translate(-50%, -50%);
            transform: translate(-50%, -50%);
        }

        .title {
            text-align: center;
            font-size: 30px;
            padding: 10px;
        }
    </style>
</head>
<body>
<div class="wrapper">
    <div class="container">
        <div class="title">
            <img style="max-width: 600px; height: auto;" src="static/img.jpg" />         
            <br>
            prediction = """ + str(prediction) + """
            
        </div>
    </div>

    

</div>
</body>
</html>"""
      template.write(content)
      template.close()

      resp = make_response(render_template("result.html"))
      resp.headers['Cache-Control'] =  'no-cache, no-store'
      resp.headers['Pragma'] = 'no-cache'
      return resp

if __name__ == '__main__':
   app.run(debug = True)