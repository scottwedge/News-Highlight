from flask import render_template,request,redirect,url_for
from  . import main
from .request import get_source,get_article
from app import app

#views
@app.route('/')
def index():
    '''
    View function that returns the index page and its data
    '''

    # Getting sources according to category
    business_source = get_source('business')
    general_source = get_source('general')
    sport_source = get_source('sport')
    entertainment_source = get_source('entertainment')
    tech_source = get_source('tech')

    title = 'Home - Welcome to the number one News Website Online'

    return render_template('index.html',title = title,business = business_source,general = general_source,sport = sport_source,entertainment = entertainment_source,tech = tech_source)

@app.route('/source/<id>')
def source(source_id):
    '''
    View function that returns the source page and its data
    '''
    # Getting articles according to source chosen
	  article = get_article(id):
	  source_id = id.upper()
	  title = f'{source_id} - Top Article'
    return render_template('source.html',title = title,id = source_id, article = article)    