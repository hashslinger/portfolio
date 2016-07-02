# -*- coding: utf-8 -*-
"""
    Gregory Guterman Portfolio
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', projects= [
        ('Plankton Populations', '/visualizations', '''http://www.exploratorium.edu/sites/default/files/East_LivingLiquids.jpg''', False),
        ('TekBubble', '/games', 'static/images/tbvonwoz.png', False),
        ('Synteny Explorer', '/visualizations', 'static/images/genome.png', False),
        ('JS Static Analyzer', '/websites', 'static/images/js-static-analyzer.png', False),
        ('Tower Defense', '/games', 'static/videos/tower-defense.mp4', True),
        ('ChessGo', '/games', 'static/images/chessgoSS.png', False),
        ('All of the Video Games', '/visualizations', 'static/images/allgames.png', False),
        ('MoooooonRocks', '/games', 'static/videos/mooon-rocks.mp4', True),
        ('Davis Dinner Club', '/websites', 'static/images/ddc.png', False)
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

@app.route('/all-of-the-games')
def all_of_the_games():
    return render_template('all-of-the-games.html')

@app.route('/presidential-debate-simulator')
def presidential_debate_simulator():
    return render_template('debatevis.html')

if __name__ == '__main__':
    app.run(debug='true')
