from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'jane'}
    return render_template('index.html',
                           title='home',
                           user=user)