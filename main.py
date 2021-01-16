#!/usr/bin/env python
import json
import os
import logging
from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
from weather import query_api
from city import get_cities

app = Flask(__name__)

@app.route('/')
def index():
    data = get_cities()
    return render_template(
        'weather.html',
        data=data,
        phase='ask',
        jsinfo=data)


@app.route("/result", methods=["GET", "POST"])
def result():
    data = []
    error = None
    select = request.form.get('comp_select')
    resp = query_api(select)
    pp(resp)
    if resp:
       data.append(resp)
    if len(data) != 2:
        error = 'Bad Response from Weather API'
    return render_template(
        'result.html',
        data=data,
        error=error,
        phase='answer')


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500

if __name__=='__main__':
    app.run(debug=True)
