from flask import Flask, request, render_template, redirect, url_for
import os

from threading import Lock

lock = Lock()

import get_data
import plotting

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/somerset')
def somerset():
    somerset_data = get_data.get_penn_data(county='Somerset')
    cases = somerset_data[0]
    titles = {'figure': 'Somerset Cases',
              'x': 'Date',
              'y': 'Daily Cases'}
    with lock:
        figure_html = plotting.plot_cases(cases.cases,
                                          cases.cases_avg_new,
                                          titles)

    return render_template('location_page.jinja2',
                           county_name='Somerset',
                           figure_html=figure_html)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)
