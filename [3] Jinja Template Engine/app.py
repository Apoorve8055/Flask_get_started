from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')
def Home():
    Homeactive = 'active'
    return  render_template('pages/index.html',Homeactive =Homeactive)

@app.route('/about')
def About():
    Aboutactive = 'active'
    return render_template('pages/about.html',Aboutactive = Aboutactive)

@app.route('/login')
def Login():
    Loginactive = 'active'
    return render_template('pages/login.html',Loginactive = Loginactive)

@app.route('/signup')
def Signup():
    Signupactive = 'active'
    return render_template('pages/signup.html',Signupactive = Signupactive)

app.run(debug=True)