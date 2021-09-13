from flask import render_template
from app import app
from .request import get_articles, get_sources
# Views


@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    all_sources = get_sources()
    title = 'Trending Now in the World| Ready News'
    return render_template('index.html', title=title, sources=all_sources)


@app.route('/source/<string:id>')
def source(id):
    '''
    View aticles from one source function
    '''
    source = get_articles(id)
    title = 'Trending Now in the World | Get More'
    return render_template('source.html',  title=title, source=source)