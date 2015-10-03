# -*- coding: utf-8 -*-
"""
    Gregory Guterman Portfolio
"""

from flask import Flask, render_template, request
app = Flask(__name__)

from wtforms import Form, TextField, TextAreaField, SubmitField, validators

app.secret_key = '3ruqh4r0r8j230rj0w9f0kq90i23092'

class ContactForm(Form):
    name = TextField('Name', [validators.Length(min=1, max=35)])
    email = TextField('Email', [validators.Length(min=6, max=35)])
    message = TextAreaField('Message', [validators.DataRequired('Please enter a message')])
    submit = SubmitField("Submit")

@app.route('/email', methods=['GET', 'POST'])
def email():
    form = ContactForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for your email')
    form = ContactForm()
    return render_template('home.html', form=form)

@app.route('/', methods=['GET'])
def home():
    form = ContactForm()
    return render_template('home.html', form=form)

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@app.route('/websites')
def websites():
    return render_template('websites.html')

if __name__ == '__main__':
    app.run(debug='true')
