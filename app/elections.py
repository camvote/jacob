from __main__ import app

from flask import render_template, request

# Election home-page
@app.route('/elections/<election_id>/')
def view_election(election_id):
    return render_template('election.html')

# Voting page for a specific election
@app.route('/elections/<election_id>/vote')
def vote(election_id):
    return render_template('vote.html')

# Results page for a specific election
@app.route('/elections/<election_id>/results')
def results(election_id):
    return render_template('results.html')

# Audit page for a specific election
@app.route('/elections/<election_id>/audit')
def audit(election_id):
    return render_template('audit.html')