import mysql.connector
import requests
import mysql.connector
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

    ip_req = requests.get('https://get.geojs.io/v1/ip.json')
    ip_add = ip_req.json()['ip']
    print(ip_add)

    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_req = requests.get(url)
    geodata = geo_req.json()
    print(geodata)
    print(geodata['latitude'])
    print(geodata['longitude'])
    print(geodata['timezone'])
    print(geodata['country'])

    guide.lat = geodata['latitude']
    guide.lon = geodata['longitude']

    return render_template('guide.html', Name=name, Calamity=calamity, FW=fw, Med=med, Cloth=cloth, Note=note)


# display function to call the display page for the responsible authorities
@app.route("/display", methods=['GET', 'POST'])
def display():
    db = mysql.connector.connect(host="localhost", user="root", password="root", database="provider1")
    my_cursor = db.cursor()
    my_cursor.execute("SELECT quantity FROM INVENTORY where item='Food & Water'")
    qty = 0
    for i in my_cursor:
        qty = i[0]
        print(qty)
    return render_template('display.html', Name=guide.NAME, Lat=guide.lat, Lon=guide.lon, Calamity=guide.CALAMITY,
                           FW=guide.FW, Med=guide.MED, Cloth=guide.CLOTH, Note=guide.NOTE, IO=qty)


app.run(debug=True)
