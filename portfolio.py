# -*- coding: utf-8 -*-
"""
    Gregory Guterman Portfolio
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', projects= [
        ('TekBubble', '/games', 'static/images/tbvonwoz.png'),
        ('Synteny Explorer', '/visualizations', 'static/images/genome.png'),
        ('ChessGo', '/games', 'static/images/chessgoSS.png'),
        ('All of the Video Games', '/visualizations', 'static/images/allgames.png'),
        ('Davis Dinner Club', '/websites', 'static/images/ddc.png')
    ])

@app.route('/games')
def games():
    return render_template('games.html')

@app.route('/visualizations')
def visualizations():
    return render_template('visualizations.html')

@app.route('/websites')
def websites():
    return render_template('websites.html')

@app.route('/ddc')
def ddc():
    return render_template('ddc.html')

if __name__ == '__main__':
    app.run(debug='true')
