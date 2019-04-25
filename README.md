# miyazaki
Classifier that determines from which of Hayao Miyazaki's films is the picture fed to it, and a basic Flask web app.
The classifier uses a ResNet-34 pretrained on ImageNet which then was finetuned on an evenly distributed dataset of 10000 frames from different Hayao Miyazaki's films. This was a part of my work on the fast.ai's course "Practical Deep Learning for Coders".

REQUIREMENTS: flask, fastai

BIG SPOILER:
Unfortunately, the file that cotains the model is too big for Github and can be found here: https://drive.google.com/file/d/12jcwnSzAUPgvnkcLK0lk7ug38lBd4eKT/view?usp=sharing
It should be put into flaskapp/model folder
