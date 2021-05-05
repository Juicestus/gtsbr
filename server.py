#!/usr/bin/env python3

from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/synthdiv')
def synthdiv():
    return render_template('synthdiv.html')

if __name__ == '__main__':
    app.run(debug=True)
    #app.run(host="0.0.0.0", port=80)