from flask import Flask, render_template

app = Flask(__name__)

#Here's where we get data.
#Home data retrieval
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

#You need to pip install mysqlclient so sqlalchemy can work with MySQL databases
engine = create_engine("mysql://lfmavjnpmit77pyc:piypmhp3rei57h25@zj2x67aktl2o6q2n.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/zfrd6ni2bkg243pf", echo=True)

Base = automap_base()
Base.prepare(engine, reflect=True)
session = Session(engine)
States = Base.classes.States
Num = Base.classes.Num_Restaurants
Heart = Base.classes.cleaned_heart_no_nulls
Fifteen = Base.classes.wikidata_2015
Eighteen = Base.classes.wikidata_2018

ins = [States.states,Num.restaurants_per_10k_residents,
      Fifteen.Vehicles_per_1000_People,
      Eighteen.Vehicles_per_1000_People,
      Heart.Year,Heart.Category,Heart.Data_Value_Type,
      Heart.Data_Value_Unit,Heart.Data_Value,
      Heart.Data_Value_Alt,Heart.Confidence_Limit_Low,
      Heart.Confidence_Limit_High,Heart.Break_Out_Category,
      Heart.Break_out]
merged = session.query(*ins).filter(States.state_id == Num.state_id).\
    filter(States.state_id == Fifteen.state_id).\
    filter(States.state_id == Eighteen.state_id).\
    filter(States.state_id == Heart.LocationID).all()

@app.route("/")
def home():
    return render_template("index.html",alldata=merged)

if __name__ == "__main__":
    app.run(debug=True)