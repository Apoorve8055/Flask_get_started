from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def Home():
    PageData = "This is Test webapp "
    return render_template('pages/index.html',Data = PageData)
@app.route('/about')
def About():
    PageData = "Hi my name is Apoorv Verma"
    return render_template('pages/about.html',Data = PageData)

app.run(debug=True)