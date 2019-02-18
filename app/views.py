from flask import render_template
from app import app
from .request import get_news
#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    popular_news = get_news('popular')
    print(popular_news)
    message = 'Welcome to our website'
    title = 'Welcome to our News website'

# Getting popular news

    return render_template('index.html', title = title, popular = popular_news)

@app.route('/newz/<newz_id>')
def newz(newz_id):
    '''
    view newz page function that returns the newz details page and its data.
    '''
    return render_template('newz.html',id=newz_id)