from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)

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
    guide.NAME = name
    guide.CALAMITY = calamity
    guide.FW = fw
    guide.MED = med
    guide.CLOTH = cloth
    guide.NOTE = note
    return render_template('guide.html')

# display function to call the display page for the responsible authorities
@app.route("/display", methods=['GET', 'POST'])
def display():

    mydb = mysql.connector.connect(host="loaclhost", user="root", passwd="1234", database='provider1')
    fqs = 0
    ms = 0
    cls = 0
    mycursor = mydb.cursor()
    mycursor.execute(" select quantity from inventory where category='Food' ")
    for i in mycursor:
        fqs += i

    mycursor.execute(" select quantity from inventory where category='Med' ")
    for i in mycursor:
        ms += i

    mycursor.execute(" select quantity from inventory where category='Cloth' ")
    for i in mycursor:
        cls += i

    return render_template('display.html', Name=guide.NAME, Calamity=guide.CALAMITY, FW=guide.FW, Med=guide.MED,
                           Cloth=guide.CLOTH, Note=guide.NOTE)

app.run(debug=True)