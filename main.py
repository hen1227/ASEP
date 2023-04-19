from flask import Flask, render_template
from urllib.request import urlopen 
import json

APIKey = "c09e16df2da01eaacc00a45d04eb066e"

API_URL = ('http://api.openweathermap.org/data/2.5/weather?id=524901&appid=' + APIKey)


app = Flask(__name__)
@app.route('/')
def index():
   return render_template('home.html')

@app.route('/weather')
def weather():
    with urlopen(API_URL) as r:
        weather_data = json.loads(r.read())
        print(weather_data)
        weather_data["main"]["temp"] = round(weather_data["main"]["temp"])
        print(weather_data)
    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
   app.run(debug=True, port=8001)

