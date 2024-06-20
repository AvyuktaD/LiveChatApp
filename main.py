from flask import Flask, render_template, url_for,redirect,request
from flask_socketio import SocketIO, emit
from backend import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/login',methods=['POST'])
def login():
    if request.method == 'POST':
        return render_template('login.html')

@app.route('/info',methods=['POST'])
def info():
    if request.method == 'POST':
        user = request.form['user']
        email = request.form['email']
        user_Info = db.signUp(user,email)
        if user_Info:
            return redirect(url_for('home'))
        else:
            return redirect(url_for('home'))


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