from flask import Flask, request, redirect
from helpers import rotate_string
import string

app = Flask(__name__)
app.config['DEBUG'] = True

page_header  = """ <!DOCTYPE html>

<html>
    <head>
    <a>Welcome to WebCaesar</a> 
    <style>
    form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
    textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
"""

form = """
<body>
    <form action="/" method="POST">
      <label for="text">Enter text:</label>
      <input type="text" name="text" id="text"/>
      <label>Rotate by:</label>
      <input type="textarea" name="rot" id="rot" value="0"/>
      <button type="submit">Submit Query</button>
      <textarea name="rotated" id="rotated">{0}</textarea>
      </form>
    </body>
</html>
"""


@app.route("/", methods=['POST'])
def encrypt():
    rot=int(request.form['rot'])
    text=str(request.form['text'])

    rotated = rotate_string(text,rot)

    return form.format(rotated)

    
@app.route("/")
def index():
    return form.format("")

app.run()