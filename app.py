from flask import Flask, request, render_template, redirect, url_for
import os
from threading import Lock

import get_data
from location_page import LocationPage

app = Flask(__name__)
lock = Lock()


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/somerset')
def somerset():
    cases, deaths, hospital = get_data.get_penn_data(county='Somerset')

    somerset_page = LocationPage('Somerset',
                                 cases=cases,
                                 deaths=deaths,
                                 r_value=0,
                                 hospital=hospital)

    with lock:
        somerset_page.create_case_plots()
        somerset_page.create_death_plots()

    return render_template('location_page.jinja2',
                           location_data=somerset_page)


@app.route('/philadelphia')
def philly():
    cases, deaths, hospital = get_data.get_penn_data(county='Philadelphia')

    philly_page = LocationPage('Philadelphia',
                               cases=cases,
                               deaths=deaths,
                               r_value=0,
                               hospital=hospital)

    with lock:
        philly_page.create_case_plots()
        philly_page.create_death_plots()

    return render_template('location_page.jinja2',
                           location_data=philly_page)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
