from flask import render_template
from app import app
#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    message = 'Welcome to our website'
    title = 'Welcome to our News website'
    return render_template('index.html', title = title)

@app.route('/newz/<newz_id>')
def newz(newz_id):
    '''
    view newz page function that returns the newz details page and its data.
    '''
    return render_template('newz.html',id=newz_id)