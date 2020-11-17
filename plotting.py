import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import mpld3


def plot_cases(case_data, titles):
    fig = Figure()

    plt.plot(case_data)

    plt.title(titles['figure'])
    plt.xlabel(titles['x'])
    plt.ylabel(titles['y'])

    fig.autofmt_xdate()
    html_str = mpld3.fig_to_html(fig)
    plt.close(fig)

    return html_str
