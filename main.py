from flask import Flask, render_template, url_for,redirect
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('index.html')

@socketio.on('connect')
def connect():
    print("Connected")

@socketio.on('disconnect')
def disconnect():
    print("Disconnect")

@socketio.on('my_event')
def handle_message(data):
    print(f'received message: {data}')
    emit(f'the date is {data}')

if __name__ == '__main__':
    socketio.run(app, debug=True, port=80)