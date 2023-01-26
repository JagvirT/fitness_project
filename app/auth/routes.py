from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, current_user, login_required
from app.auth.forms import UserCreationForm, LoginForm, ExerciseForm, SingleExerciseForm, FoodForm
from app.models import User, Post
from werkzeug.security import check_password_hash
import requests 
from flask_socketio import SocketIO, send
import os


auth = Blueprint('auth', __name__, template_folder= 'auth_templates')

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    form = UserCreationForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            print(username, email, password)

            user = User(username, email, password)

            #add user to database
            user.save_to_db()
            return redirect(url_for('auth.login'))

    return render_template('signup.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            password = form.password.data

            print(username, password)

            user = User.query.filter_by(username= username).first()
            if user:
                if check_password_hash(user.password, password):
                    print('Login successful')
                    login_user(user)
                else:
                    print('Invalid password')
            else:
                print('Invalid username')
    return render_template("login.html", form=form)


@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/search', methods=['GET', 'POST'])
@login_required
def home():
    form = ExerciseForm()
    if request.method == 'POST':
        if form.validate():
            exercise = form.exercise.data.lower()
            exercise_info ={}
            url = f'https://exercisedb.p.rapidapi.com/exercises/name/{exercise}'

            headers = {
                "X-RapidAPI-Key": "859f396bc9mshcd9a657952c157fp17d690jsndab93f8a8cbc",
                "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers)
            new_response = response.json()
            # print(new_response)


            return render_template('search_exercise.html', exercises=new_response, form=form)
    return render_template('search_exercise.html', form=form)

@auth.route('/test_add/<exercise_name>')
@login_required
def test_add(exercise_name):
    url = f'https://exercisedb.p.rapidapi.com/exercises/name/{exercise_name}'

    headers = {
        "X-RapidAPI-Key": "859f396bc9mshcd9a657952c157fp17d690jsndab93f8a8cbc",
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    new_response = response.json()
    name = new_response[0]['name']
    bodyPart = new_response[0]['bodyPart']
    target = new_response[0]['target']
    equipment = new_response[0]['equipment']
    gifUrl = new_response[0]['gifUrl']
    post = Post(name, bodyPart, target, equipment, gifUrl, current_user.id)
    post.save_to_db()
    flash("Successfully added to your exercises")
    return redirect(url_for('auth.my_exercises'))       

    


@auth.route('/posts')
@login_required
def my_exercises():
    posts= Post.query.filter_by(user_id=current_user.id).all()
    # videos = {}
    # if posts.target == 'back':
    #     videos['back'] = 'https://www.youtube.com/watch?v=B1T6ZYrPAy4&list=PLLALQuK1NDrgbrHnrWt_TaQK1sSraAQ1U'
    # elif posts.target == 'chest':
    #     videos['chest'] = 'https://www.youtube.com/watch?v=g7U3Q8_6css&list=PLoA8R7df04hR8myTXR30kZGy6dRhS7kni'
    # elif posts.target == 'abs':
    #     videos['abs'] = 'https://www.youtube.com/watch?v=2pLT-olgUJs&list=PLAFs3kxY4h1_XkN6EsVci1E3Y_lHj5xzK'
    # elif posts.taret == 'biceps':
    #     videos['biceps'] = 'https://www.youtube.com/watch?v=lBy-7EFK30o&list=PLX8QIwhN83ZWVSua-HFLG7oDDT87fdu9k'
    # elif posts.target == 'triceps':
    #     videos['triceps'] = 'https://www.youtube.com/watch?v=lBy-7EFK30o&list=PLX8QIwhN83ZWVSua-HFLG7oDDT87fdu9k'
    # elif posts.target == 'shoulders':
    #     posts['shoulders'] = 'https://www.youtube.com/watch?v=oq77AW1XNbc'


    return render_template('my_exercises.html', posts=posts)


@auth.route('/posts/delete/<int:post_id>')
@login_required
def delete_exercise(post_id):
    post = Post.query.get(post_id)
    if current_user.id == post.user_id:
        if post:
            post.delete_from_db()
        return redirect(url_for('auth.my_exercises'))
    else:
        print('you are not allowed to be here')
        return redirect(url_for('auth.search_exercises'))


@auth.route('/chat')
def message():
    return render_template('chat.html')


@auth.route('/search_food', methods=['GET', 'POST'])
@login_required
def search_food():
    form = FoodForm()
    if request.method == 'POST':
        if form.validate():
            print("hello")
            food = form.food.data.lower()
            url = "https://nutrition-by-api-ninjas.p.rapidapi.com/v1/nutrition"

            querystring = {"query":f'{food}'}

            headers = {
                "X-RapidAPI-Key": "859f396bc9mshcd9a657952c157fp17d690jsndab93f8a8cbc",
                "X-RapidAPI-Host": "nutrition-by-api-ninjas.p.rapidapi.com"
            }

            response = requests.request("GET", url, headers=headers, params=querystring)
            food_response = response.json()

            print(food_response)
            # name= food_response[0]['name']
            # sugar=food_response[0]['sugar']
            # serving_size = food_response[0]['serving_size_g']
            # sodium = food_response[0]['sodium_mg']
            # potassium_mg = food_response[0]['potassium_mg']
            # saturated_fat = food_response[0]['fat_saturated_g']
            # total_fat = food_response[0]['total_fat_g']
            # calories = food_response[0]['calories']
            # cholesterol = food_response[0]['cholesterol_mg']
            # protein = food_response[0]['protein_g']
            # carbs = food_response[0]['carbohydrates']
            # food_info = Food(name, sugar, serving_size, sodium, potassium_mg, saturated_fat, total_fat, calories, cholesterol, protein, carbs)
            # food_info.save_to_db()
            return render_template('search_nutrition.html', form=form, food_response=food_response)
    return render_template('search_nutrition.html', form=form)








    
