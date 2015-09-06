# -*- coding: utf-8 -*-
"""
    Gregory Guterman Portfolio
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

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
