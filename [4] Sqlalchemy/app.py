from flask import Flask,render_template,request
from sqlalchemy import sql
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/flask_app'
db = SQLAlchemy(app)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    passs = db.Column(db.String(120),  nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    #Date = db.Column(db.String(120), nullable=True)
    #status = db.Column(db.Integer, nullable=True)

@app.route('/',methods=['GET','POST'])
def home():
    if request.method == 'POST':
        name = request.form.get('fname')
        passs = request.form.get('passs')
        email = request.form.get('email')
        data_entry = Users(name=name,passs=passs,email=email)
        db.session.add(data_entry)
        db.session.commit()

    return render_template('index.html')

@app.route('/Users')
def users():
    res = Users.query.all()
    return render_template('view.html',res =res)

app.run(debug=True)