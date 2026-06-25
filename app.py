import requests
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html')

@app.route("/contact")
def MaPremiereAPI():
    return "<h2>Ma page de contact</h2>"

@app.get("/paris")
def api_paris():
    url = "https://api.open-meteo.com/v1/forecast?latitude=48.8566&longitude=2.3522&hourly=temperature_2m&forecast_days=7&timezone=Europe%2FParis"
    data = requests.get(url).json()
    times = data.get("hourly", {}).get("time", [])
    temps = data.get("hourly", {}).get("temperature_2m", [])
    result = [
        {"datetime": time, "temperature_c": temp}
        for time, temp in zip(times, temps)
    ]
    return jsonify(result)

@app.route("/rapport")
def mongraphique():
    return render_template("graphique.html")

@app.get("/atelier-data")
def api_atelier():
    url = "https://api.open-meteo.com/v1/forecast?latitude=43.2965&longitude=5.3698&hourly=wind_speed_10m&forecast_days=1&timezone=Europe%2FParis"
    data = requests.get(url).json()
    times = data.get("hourly", {}).get("time", [])
    speeds = data.get("hourly", {}).get("wind_speed_10m", [])
    result = [
        {"datetime": time, "wind_speed_kmh": speed}
        for time, speed in zip(times, speeds)
    ]
    return jsonify(result)

@app.route("/atelier")
def atelier():
    return render_template("atelier.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
