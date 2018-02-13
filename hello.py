from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello World'

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/users/<path:path>')
def show_users_path(path):
    return 'Path %s' % path

@app.route('/about')
def about():
    return 'about'

@app.route('/contact/')
def contact():
    print url_for('index')
    print url_for('show_user_profile', username='sueprshy')
    print url_for('index', age='30')
    return 'contact'

@app.route('/hello/tmpl')
def tmpl():
    return '<link rel="stylesheet" href=%s><div>123</div>' % url_for('static', filename='style.css')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
