from flask import Flask, render_template, request, make_response, redirect, url_for, session;
from analysis.PollutionAnalytics import GetDailyPollutionGraph;




app = Flask(__name__);



# Routes
@app.route("/", methods = ['GET'])
def root():


    data = GetDailyPollutionGraph(5, "el Poblenou")


    print("\n\n")
    print(data)

    print("\n\n")

    return render_template('index.html');










app.run(host='localhost', port=5000, debug=True);
