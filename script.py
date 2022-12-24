import mysql.connector
import requests
from flask import Flask, render_template, request
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

    r = requests.get('https://www.geojs.io')
    print(r)

    ipreq = requests.get('https://get.geojs.io/v1/ip.json')
    ipadd = ipreq.json()['ip']
    print(ipadd)

    url = 'https://get.geojs.io/v1/ip/geo/' + ipadd + '.json'
    geo_req = requests.get(url)
    geodata = geo_req.json()
    print(geodata)
    print(geodata['latitude'])
    print(geodata['longitude'])
    print(geodata['timezone'])
    print(geodata['country'])

    return render_template('guide.html', Name=name, Calamity=calamity, FW=fw, Med=med, Cloth=cloth, Note=note)


# display function to call the display page for the responsible authorities
@app.route("/display", methods=['GET', 'POST'])
def display():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="provider")
    mycursor = db.cursor()
    mycursor.execute("SELECT quantity FROM INVENTORY where item='food'")
    for i in mycursor:
        print(i[0])
    return render_template('display.html', Name=guide.NAME, Calamity=guide.CALAMITY, FW=guide.FW, Med=guide.MED,
                           Cloth=guide.CLOTH, Note=guide.NOTE, IO=i[0])


app.run(debug=True)
