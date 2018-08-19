import os
from flask import Flask,render_template,request
import re

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__)) 

@app.route("/")
def index():
    language = ['English', 'Japanese', 'French', 'Chinese']
    return render_template("index.html",languages=language)


@app.route("/",methods = ['GET','POST'])
def upload():
    language = ['English', 'Japanese', 'French', 'Chinese']
    selected_language = request.form.get('language')
    print(selected_language)
    target = os.path.join(APP_ROOT,selected_language)
    print (target)
    
    if not os.path.isdir(target):
        os.mkdir(target)
    print (request.files.getlist('file'))
    for file in request.files.getlist('file'):
        print (file)
        file_name = file.filename
        music_destination = "/".join([target,file_name])
        print (music_destination)
        file.save(music_destination)
    return render_template("index.html",target=file_name,languages=language,directory=selected_language)


    


    
    
    
