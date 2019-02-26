from flask import (
    Blueprint, jsonify, render_template,
    request, redirect
)
from .models import User
from .forms import UserForm
from app import db

user = Blueprint('users', __name__, template_folder="templates")

@user.route("/users")
def get_users():
    users = db.session.query(User)
    return render_template("index.html", users=users)

@user.route("/user/create", methods=['GET','POST'])
def create_user():
    form = UserForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_user = User()
            form.populate_obj(new_user)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/users')
    
    return render_template("create_user.html", form=form)