from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy
#from datetime import datetime

app = Flask(__name__)
#app.config['SQLACHEMY_DATABASE_URI'] = 'sqlite:///test.db'
#db = SQLAlchemy(app)

#class ToDo(db.Model):
#    id = db.Column(db.Integer, primary_key = True)
#    content = db.Column(db.String(200), nullable = False)
#    completed = db.Column(db.Integer, default = 0)
#    date_created = db.Column(db.DateTime, default = datetime)

def __repr__(self):
    return '<Task %r>' % self.id

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signUp')
def signup():
    return render_template('signup.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/myEvents')
def myevents():
    return render_template('myEvents.html')

@app.route('/bookAnEvent')
def bookanevent():
    return render_template('bookanevent.html')

if __name__ == "__main__":
    app.run(debug = True)