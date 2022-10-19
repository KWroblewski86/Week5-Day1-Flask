from app import app

from flask import render_template


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/movies')
def moviesPage():
    return render_template('movies.html')