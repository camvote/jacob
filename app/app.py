from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

import elections
import admin

if __name__ == '__main__':
    import os

    if os.environ.get('PRODUCTION'):
        raise Exception("Can't run interactively in PRODUCTION")

    app.run(host=os.environ.get('FLASK_HOST', '127.0.0.1'), 
            port=os.environ.get('FLASK_PORT', 5000), 
            debug=os.environ.get('FLASK_DEBUG', True))
