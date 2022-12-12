from Flask import Flask, jsonify
import pandas as pd
from sqlHelper import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"""Welcome to the Hawaii Weather API!<br>
        <a href='/api/v1.0/precipitation>//api/v1.0/precipitation</a>"""
    )

@app.route("/api/v1.0/precipitation")
def get_precipitation():
    df = sqlHelper.getprecipitation()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_stations():
    df = sqlHelper.getstations()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def get_temp_data_for_date(start):
    df = sqlHelper.getTempDataForDate(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def get_temp_data_for_date_range(start, end):
    df = sqlHelper.getTempDateForDateRange(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))

if __name__ == "__main__":
    app.run(debug=True)
