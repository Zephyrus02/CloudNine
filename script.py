from flask import Flask, render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/guide", methods=["POST"])
def guide():
    name = request.form['name']
    fw = request.form['FW']
    med = request.form['Med']
    cloth = request.form['Cloth']
    note = request.form['note']
    return render_template('guide.html', Name=name, FW=fw, Med=med, Cloth=cloth, Note=note)

app.run(debug=True)