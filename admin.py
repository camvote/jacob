from __main__ import app

from flask import render_template, request

# Create society
@app.route('/societies/create')
def create_society():
    return render_template('create_society.html')

# TODO: View society /societies/<society_id>/

@app.route('/elections/create/')
def create_election():
    return render_template('create_election.html')