from app import app
from flask import render_template
import requests

@app.route('/home')
def home():
    exercise_info ={}
    url = "https://exercisedb.p.rapidapi.com/exercises"

    headers = {
        "X-RapidAPI-Key": "859f396bc9mshcd9a657952c157fp17d690jsndab93f8a8cbc",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    new_response = response.json()
    print(new_response)


    return render_template('index.html', exercises=new_response)


@app.route('/')
def welcome():
    return render_template('welcome.html')







