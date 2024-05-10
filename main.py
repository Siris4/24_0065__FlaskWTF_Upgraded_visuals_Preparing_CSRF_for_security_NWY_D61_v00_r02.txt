# main.py
from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired
import os

# sets up environment variables before app initialization:
SECRET_KEY_ENV = os.environ.get('MYSECRETKEY', 'default-secret-key') #within backup catch for default value of key
app = Flask(__name__)
app.config['SECRET_KEY'] = SECRET_KEY_ENV

class MyLoginForm(FlaskForm):
    email = StringField('Email', render_kw={"size": "30"})  # adds size attribute
    password = StringField('Password', render_kw={"size": "30"})

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyLoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', form=form)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = MyLoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('submit.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
