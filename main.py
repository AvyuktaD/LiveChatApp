from flask import Flask, render_template, url_for,redirect,request,session
from flask_socketio import SocketIO, emit,send
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
        session['user'] = request.form['user']
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
def handle_message(json):
    print(f'received message: {json}')
    emit(f'the date is',json)

    if "user" in session:
        user_message = db.addMessage({"username" : session['user']}, {"message" : json})
        if user_message:
            return True
        else:
            return False
    else:
        return False

if __name__ == '__main__':
    socketio.run(app, debug=True, port=80)