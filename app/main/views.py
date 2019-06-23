from flask import render_template
from app import app

#views
@app.route('/')
def index():
    '''
    View function that returns the index page and its data
    '''
    message = 'News-Highlights'
    return render_template('index.html',message = message)

@app.route('/source/<int:source_id>')
def source(source_id):
    '''
    View function that returns the source page and its data
    '''
    return render_template('source.html',id = source_id)    