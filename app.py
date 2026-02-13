from flask import Flask, render_template, request, redirect, url_for
import requests

app = Flask(__name__)

API_KEY = "62f64dabd5b8e44af4fb1c1e72665ab5"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    forecast_data = None
    error = None

    if request.method == "POST":
        if "clear" in request.form:
            return redirect(url_for("index"))

        city = request.form.get("city")

        # Current Weather
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric"
        }

        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code == 200:
            weather_data = {
                 "city": data["name"],
                 "temperature": data["main"]["temp"],
                 "description": data["weather"][0]["description"],
                 "humidity": data["main"]["humidity"],
                 "wind": data["wind"]["speed"],
                 "icon": data["weather"][0]["icon"],
                 "main": data["weather"][0]["main"]
            }

            # 5 Day Forecast
            forecast_response = requests.get(FORECAST_URL, params=params)
            forecast_json = forecast_response.json()

            forecast_data = []

            for item in forecast_json["list"]:
                if "12:00:00" in item["dt_txt"]:
                    forecast_data.append({
                        "date": item["dt_txt"].split(" ")[0],
                        "temp": item["main"]["temp"],
                        "description": item["weather"][0]["description"],
                        "icon": item["weather"][0]["icon"]
                    })

        else:
            error = "City not found. Please try again."

    return render_template("index.html", weather=weather_data, forecast=forecast_data, error=error)


if __name__ == "__main__":
    app.run(debug=True)
