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
    app.run()
