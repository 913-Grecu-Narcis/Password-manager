from flask import Flask, render_template, url_for, request

from business.connect_service import ConnectService
from domain.user import User
from infrastructure.repository import Repository

app = Flask(__name__)
repo = Repository()
connect_service = ConnectService(repo)


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        user_name = request.form['username']
        email = request.form['email']
        confirm_email = request.form['confirm_email']
        password = request.form['password']
        confirm_pass = request.form['confirm_password']

        try:
            connect_service.register_user(user_name, email, confirm_email, password, confirm_pass)
            return render_template('register.html', message='Register successfully!')
        except Exception as e:
            return render_template('register.html', message=str(e))


    return render_template('register.html', message='')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']

        login_status, login_message = connect_service.check_for_login(user_email, user_password)

        return render_template('login.html', message=login_message)

    return render_template('login.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
