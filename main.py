from flask import Flask,request
from helpers import alphabet_position
import string

app = Flask(__name__)
app.config['DEBUG'] = True

form  = """ 
<html lang="en">
    <head>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }

        </style>
    </head>
    <body>
        <form ("/add", methods=['POST'])>
            <label for = "rot">Rotate by:</label>
            <input type="text" name="rot" value="0"/>
        
    </form>
    </body>
</html>
"""

@app.route("/add", methods=['POST'])
def encrypt(text,rot):
    rotated = ''
    alphabet = string.ascii_lowercase
    rot = int(rot)

    for char in text:
        if char.isalpha():
            rotated_idx = (alphabet_position(char) + rot) %26
            if char.isupper(): # if it was uppercase originally, make it uppercase
                rotated += alphabet[rotated_idx].upper()
            else: # keep it lowercase
                rotated += alphabet[rotated_idx]
        elif char == " ": 
            rotated += char
        else:
            rotated += char
    return "<h1>"+rotated+"</h1>"



@app.route("/")
def index():
    return form.format(form)

app.run()