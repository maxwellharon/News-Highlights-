from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    message = 'News'
    title = 'Welcome to the world\'s number one news site'
    return render_template('index.html',title = title,message = message)


# @app.route('/news/<news_id>')
# def news(news_id):
#
#     '''
#     View movie page function that returns the movie details page and its data
#     '''
#     return render_template('news.html',id = news_id)
