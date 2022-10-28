from xml.etree.ElementInclude import FatalIncludeError
from pygame import mixer
from flask import Flask 
import time
mixer.init()
app = Flask(__name__)
is_on = False
@app.route('/on')
def on():
    global is_on
    is_on  = True
    mixer.music.load('file.mp3')

    while is_on == True:
        mixer.music.play()
        time.sleep(50)
    mixer.music.pause()
    is_on = False
@app.route('/off')
def off():
    global is_on
    is_on = False
    mixer.music.pause()
app.run(debug=True)