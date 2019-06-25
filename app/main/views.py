from flask import render_template,request,redirect,url_for
from  . import main
from ..request import get_sources,get_article
from ..models import Source

#views
@main.route('/')
def index():
    '''
    View function that returns the index page and its data
    '''

    # Getting sources according to category
    business_sources = get_sources('business')
    general_sources = get_sources('general')
    sport_sources = get_sources('sport')
    entertainment_sources = get_sources('entertainment')
    tech_sources = get_sources('tech')

    title = 'Home - Welcome to the number one News Website Online'

    return render_template('index.html',title = title,business = business_sources,general = general_sources,sport = sport_sources,entertainment = entertainment_sources,tech = tech_sources)

@main.route('/source/<id>')
def source(source_id):
    '''
    View function that returns the source page and its data
    '''
    # Getting articles according to source chosen
    article = get_article(id)
    source_id = id.upper()
    title = f'{source_id} - Top Article'
    return render_template('source.html',title = title,id = source_id, article = article)    