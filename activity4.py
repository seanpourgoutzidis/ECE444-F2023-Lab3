from flask import Flask, render_template, session, redirect, url_for, flash
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

from datetime import datetime
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import DataRequired
from wtforms.validators import Email

app = Flask(__name__)
app.config['SECRET_KEY'] = 'wowzers'
bootstrap = Bootstrap(app)
moment = Moment(app)

class NameEmailForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = EmailField('What is your UofT Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

@app.route('/', methods = ['GET', 'POST'])
def index():
    form = NameEmailForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        if old_email is not None and old_email != form.email.data:
            flash('Looks like you have changed your email!')
        session['name'] = form.name.data
        session['email'] = form.email.data

        isUoftEmail = False

        if ('utoronto' in session['email']):
            isUoftEmail = True

        return redirect(url_for('index'))
    return render_template('form.html', form = form, name = session.get('name'), email = session.get('email'))

    

