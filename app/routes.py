from flask import render_template, request
from app import app
from app.forms import LoginForm
from app.forms import RegisterForm


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
            #send the user to /dashboard
            return render_template('dashboard.html')
        else:
            print("no user with such name")
            return render_template('login.html', form=login_form)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if (register_form.validate_on_submit()):
        print(register_form.user.data)
        username_from_html = register_form.user.data
        print(register_form.password.data)
        password_from_html = register_form.password.data
        confirm_from_html = register_form.confirm.data
        email_from_html = register_form.email.data
        contact_num_from_html = register_form.contact_num.data
        if (user_exist(username_from_html, password_from_html)):
            print("user exist in database")
            # send the user to /dashboard
            return render_template('register.html', form=register_form)
        else:
            print("create user in the database")
            from database import Database
            from config import Setting
            setting = Setting()
            db = Database(setting)
            #ionsert new user account
            db.insert_account_data(username_from_html,password_from_html, email_from_html,"user", contact_num_from_html )
            return render_template("register.html" , form = register_form)
    return render_template("register.html" , form = register_form)

@app.route("/dashboard", methods=["GET","POST"])
def scrape_button():
    if request.method =="POST":
        print(request.form.get("testing_scrape_button"))
        if request.form.get("testing_scrape_button") =="scrape":
            from db_updater import wraper_for_scraping
            wraper_for_scraping()

            return render_template("dashboard.html")
    elif request.method =="GET":
        return render_template("dashboard.html")


def user_exist(username, password):
    exist = False #assume user not exist in database
    from database import Database
    from config import Setting
    setting = Setting()
    db = Database(setting)
    #codes to extract the user information from database
    #compare the input user with database
    all_account = db.retrieve_accounts()
    for item in all_account:
        if (item[0] == username):
            exist = True

    # print(all_account)
    # print(type(all_account))
    return exist