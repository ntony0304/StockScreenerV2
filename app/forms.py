from flask_wtf import FlaskForm  # from library/file/package/directory flask_wtf
from wtforms import StringField, PasswordField, SubmitField  # from library/package/file import class/object StringField


class LoginForm(FlaskForm):
    # user field
    user = StringField("Username")  # create a box that accept string
    # password field
    password = PasswordField("Password")  # keep raw input. 123 = 123 mypawsowrd123 @#$@#
    login_btn = SubmitField("Log in")

class RegisterForm(FlaskForm):
    user = StringField("Username")  # create a box that accept string
    # password field
    password = PasswordField("Password")  # keep raw input. 123 = 123 mypawsowrd123 @#$@#
    confirm = PasswordField("Confirm Password")
    email = StringField("Email")
    contact_num = StringField("Contact Number")
    register_btn = SubmitField("Sign up")
