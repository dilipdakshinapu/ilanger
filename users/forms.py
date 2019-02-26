from flask_wtf import FlaskForm
import wtforms as f
from wtforms.validators import DataRequired

class UserForm(FlaskForm):
    email = f.StringField("email", validators=[DataRequired()])
    firstname = f.StringField("Firstname", validators=[DataRequired()])
    lastname = f.StringField("Lastname")
    password = f.PasswordField("password")
    
    display = ["email", "firstname", "lastname", "password"]