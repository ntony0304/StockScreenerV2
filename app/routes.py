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
@app.route('/signin',methods=['GET','POST'])
def signin():
    return render_template("signin_ex.html")
@app.route('/login', methods=['GET', 'POST'])
def login():
    from database import Database
    from setting import Setting
    setting = Setting()
    db = Database(setting)

    login_form = LoginForm()
    if (login_form.validate_on_submit()):
        username_from_html =login_form.user.data
        password_from_html = login_form.password.data
        if (user_exist(username_from_html, password_from_html)):
            user=db.retrieve_account_by_user_name(username_from_html)
            #send the user to /dashboard
            return render_template('dashboard.html', user=user)
        else:
            all_account=db.retrieve_accounts()
            return render_template('login.html', form=login_form)
    return render_template('login.html', form=login_form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    register_form = RegisterForm()
    if (register_form.validate_on_submit()):
        username_from_html = register_form.user.data
        password_from_html = register_form.password.data
        confirm_from_html = register_form.confirm.data
        if password_from_html != confirm_from_html: #password and confirm password not match
            return render_template("register.html", form=register_form)
        email_from_html = register_form.email.data
        contact_num_from_html = register_form.contact_num.data
        if (user_exist(username_from_html, password_from_html)):
            # send the user to /dashboard
            return render_template('register.html', form=register_form)
        else:
            #from database import Database
            from database import Database
            from setting import Setting
            setting = Setting()
            db = Database(setting)
            #ionsert new user account
            db.insert_account_data(username_from_html,password_from_html, email_from_html,"user",
                                   contact_num_from_html )
            return render_template("register.html" , form = register_form)
    return render_template("register.html" , form = register_form)


@app.route('/dashboard_ex',methods=['GET','POST'])
def dashboard_ex():
    if request.method =="GET":
        return render_template("dashboard_ex.html")
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    if request.method =="GET":
        return render_template("dashboard.html")

def scrape_button():
    if request.method =="POST":
        print(request.form.get("testing_scrape_button"))
        if request.form.get("testing_scrape_button") =="scrape":
            from db_updater import wraper_for_scraping
            wraper_for_scraping()
            return render_template("dashboard.html")
        if request.form.get("testing_screener_button") == "screener":
            import stock_screener
            stock_screener.screener()
            return render_template("dashboard.html")

    elif request.method =="GET":
        return render_template("dashboard.html")



def user_exist(username, password):
    exist = False #assume user not exist in database
    from database import Database
    from setting import Setting
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