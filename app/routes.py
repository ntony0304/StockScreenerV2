from flask import render_template
from app import app
from app.forms import LoginForm


@app.route('/')
@app.route('/index')
def index():
    user_account = {'username' : "tony", "name" :""}
    return render_template("index.html", user=user_account)
# @app.route('/bootstrap')
# def bootstrap_ex():
#     return render_template("bootstrapex.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    if (login_form.validate_on_submit()):

        print(login_form.user.data)
        username_from_html =login_form.user.data
        print(login_form.password.data)
        password_from_html = login_form.password.data
        if (user_exist(username_from_html, password_from_html)):
            print("user found")

    return render_template('login.html', form=login_form)


def user_exist(username, password):
    exist = False #assume user not exist in database
    from database import Database
    #codes to extract the user information from database
    #compare the input user with database
    # if user exist then exist = true
    return exist