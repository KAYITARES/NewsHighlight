from flask import render_template
from app import app
from .request import get_news
#Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    general_category= get_source('general')
    sport_category= get_source('sport')
    business_category = get_source('business')
    entertainement_category = get_source('entertainement')
    technology_category = get_source('technology')
    message = 'Welcome to our website'
    title = 'NEWS'
# Getting popular news
    return render_template('index.html', title = title, general = general_category, sport = sport_category, business =  business_category, entertainement = entertainement_category,technology =  technology_category  )
@app.route('/source/<source_name>')
def source(source_name):
    '''
    view source page function that returns the nsource details page and its data.
    '''
    return render_template('source.html',id=source_name)