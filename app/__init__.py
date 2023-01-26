from flask import Flask
from config import Config
from flask_migrate import Migrate
from .models import db, User, Food
from .auth.routes import auth
from .exercise.routes import exercise
from flask_login import LoginManager
from flask_socketio import SocketIO, send, join_room

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@socketio.on("message")
def sendMessage(message):
    send(message, broadcast=True)


# new add
socketio.on("send_message")
def handle_send_message(data):
    app.logger.info("{} has sent a message to room {}:{}".format(data['username'], data['room'], data['message']))
    socketio.emit('receive_message', data, room=data['room'] )


socketio.on('join_room')
def handle_join(data):
    app.logger.info("{} has joined {}".format(data['username'], data['room']))
    join_room(data['room'])
    socketio.emit('join_room_warning', data)



app.config.from_object(Config)

login_manager = LoginManager()
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)



app.register_blueprint(auth)
app.register_blueprint(exercise)

#initialize database to elephantsql
db.init_app(app)
migrate = Migrate(app, db) 
login_manager.init_app(app)

from . import routes
from . import models


