from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import Food, User
import requests

exercise= Blueprint('exercise', __name__, template_folder='exercise_info_templates')

@exercise.route('/more_info')
def more_info():
    return render_template('body_info.html')


