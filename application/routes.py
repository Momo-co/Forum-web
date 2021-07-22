from application import app
from flask import redirect, request, render_template, url_for

@app.route('/')
@app.route('/home')
def home():
    return render_template('layout.html')
