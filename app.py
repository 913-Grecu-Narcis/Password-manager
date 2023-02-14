from flask import Flask, render_template, url_for, request

from domain.user import User
from infrastructure.repository import Repository

app = Flask(__name__)
repo = Repository()


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user_email = request.form['email']
        user_password = request.form['password']
        user = User(user_email, user_password)

        login_result = check_for_login(user)

        if login_result is True:
            return render_template('login.html', message='Login success!')

        else:
            return render_template('login.html', message=login_result)

    return render_template('login.html')


def check_for_login(user):
    result = repo.find_by_email(user.email)
    if len(result) == 0:
        return 'Email not found!'

    if result[0][2] != user.password:
        return 'Password is incorrect!'

    return True


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True, threaded=True)
