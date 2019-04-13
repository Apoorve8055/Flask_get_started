from flask import Flask
app = Flask(__name__)
@app.route('/')

def Hellow():
    return "<h1>Hellow World Page</h1>"

app.run(debug = True)
