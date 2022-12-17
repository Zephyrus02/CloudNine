from flask import Flask, render_template,request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy()

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

from script import db

class Support(db.Model):
    name = db.Column(db.String, primary_key=True, nullable=False)
    calamity = db.Column(db.String)
    fw = db.Column(db.Integer)
    med = db.Column(db.Integer)
    cloth = db.Column(db.Integer)
    note = db.Column(db.String)

with app.app_context():
    db.create_all()

# home function to call homepage for user
@app.route("/")
def home():
    return render_template('index.html')

# guide function to call guidelines page for user
@app.route("/guide", methods=['GET', 'POST'])
def guide():
    name = request.form['name']
    calamity = request.form['disaster']
    fw = request.form['FW']
    med = request.form['Med']
    cloth = request.form['Cloth']
    note = request.form['note']

    sup = Support(
        name=name,
        calamity=calamity,
        fw=fw,
        med=med,
        cloth=cloth,
        note=note
    )
    db.session.add(sup)
    db.session.commit()

    guide.NAME = name
    guide.CALAMITY = calamity
    guide.FW = fw
    guide.MED = med
    guide.CLOTH = cloth
    guide.NOTE = note
    return render_template('guide.html', Name=name, Calamity=calamity, FW=fw, Med=med, Cloth=cloth, Note=note)

# display function to call the display page for the responsible authorities
@app.route("/display", methods=['GET', 'POST'])
def display():
    return render_template('display.html', Name=guide.NAME, Calamity=guide.CALAMITY, FW=guide.FW, Med=guide.MED,
                           Cloth=guide.CLOTH, Note=guide.NOTE)

app.run(debug=True)