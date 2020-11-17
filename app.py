from flask import Flask, request, render_template, redirect, url_for

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
plt.ioff()

from threading import Lock
lock = Lock()
import mpld3
from mpld3 import plugins

import get_data

app = Flask(__name__)


def plot_data(data, titles):
    title_font = {'fontsize': 18,
                 }
    axis_font = {'fontsize': 14}
    with lock:
        fig = plt.figure()
        plt.plot(data)
        plt.title(titles['figure'],
                  fontdict=title_font)
        plt.xlabel(titles['x'],
                   fontdict=axis_font)
        plt.ylabel(titles['y'],
                   fontdict=axis_font)
        fig.autofmt_xdate(rotation=45)
        html_str = mpld3.fig_to_html(fig)
    return html_str


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/somerset')
def somerset():
    somerset_data = get_data.get_penn_data(county='Somerset')
    titles = {'figure': 'Somerset Cases',
              'x': 'Date',
              'y': 'New Cases Rate per 100k Residents'}
    figure_html = plot_data(somerset_data.cases_avg_new_rate, titles)

    return render_template('plot.jinja2',
                           county_name='Somerset',
                           figure_html=figure_html)


if __name__ == '__main__':
    app.run()
