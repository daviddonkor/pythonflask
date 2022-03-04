from flask  import Flask,render_template
from flask_cors import CORS
from flask import request,url_for,redirect
import sqlite3
from pandas_datareader import wb


app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources = {r'/*':{'origns':'*'}})


@app.route("/")
def index():
    return render_template('/pages/index.html',name='siaw')

@app.route("/country",methods=['POST','GET'])
def country():
    errors=None
    conn = sqlite3.connect("db/world_bank.db",detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES)
    cur = conn.cursor()
    cur1= conn.cursor()
    cur.execute("select * from countries")

    countries  = cur.fetchall()
  

    if request.method == 'POST':

        cname = request.form['country']
        ciso = request.form['isoname']
        
        try:
            conn.execute("insert into countries (country_name,iso_name) values('"+cname+"','"+ciso+"')")
            conn.commit()
        except:
            errors="Failed to insert data"
        return redirect(url_for('country'))
    else:
        return render_template('/pages/addcountry.html',data=countries)

@app.route("/indicators",methods=['POST','GET'])
def indicator():
    errors=None
    conn = sqlite3.connect("db/world_bank.db")
    cur = conn.cursor()
    
    cur.execute("select * from indicators")

    indicators  = cur.fetchall()
  

    if request.method == 'POST':

        cname = request.form['nicename']
        ciso = request.form['code']
        
        try:
            conn.execute("insert into indicators (indicatorname,code) values('"+cname+"','"+ciso+"')")
            conn.commit()
        except:
            errors="Failed to insert data"
        return redirect(url_for('indicator'))
    else:
        return render_template('/pages/addvariable.html',data=indicators)


@app.route("/propose",methods=['GET'])
def propose():
    errors=None
    conn = sqlite3.connect("db/world_bank.db")
    cur = conn.cursor()
    
    cur.execute("select * from indicators")
    indicators  = cur.fetchall()
  
    cur.execute("select * from countries")
    countries= cur.fetchall()

    return render_template('/pages/propose_request.html',countries=countries,indicators=indicators)


@app.route("/generateresults",methods=['POST'])
def generateresults():
    errors=None
    indicators=[]
    countries = []
    print (request.form)
    for ind in request.form['indicator']:
        indicators.append(ind)

    for cnt in request.form['country']:
        countries.append(cnt)
    #data = wb.download(indicator=indicators,country=countries,start=1990,end=2020)


    return render_template('/pages/results.html',countries=countries,indicators=indicators)