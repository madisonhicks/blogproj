from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname' : 'jane'}
    return '''
    <html>
        <head>
            <title>Project: Blog</title>
        </head>
        <body>
            <h1>Hello ''' + user['nickname'] + '''</h1>
        </body>
    </html>
    '''