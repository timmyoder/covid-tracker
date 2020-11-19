import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
# plt.ioff()
import mpld3

title_font = {'fontsize': 18,
              }
axis_font = {'fontsize': 14}


def plot_cases(case_data, avg_case_data, titles):

    fig = plt.figure()

    plt.bar(case_data.index,
            case_data,
            alpha=.6,
            color='tab:gray',
            label='Single Day')
    plt.plot(avg_case_data,
             color='tab:red',
             lw=3,
             label='7 Day Average')
    plt.title(titles['figure'],
              fontdict=title_font)
    plt.ylabel(titles['y'],
               fontdict=axis_font)
    fig.autofmt_xdate(rotation=45)
    plt.legend()
    html_str = mpld3.fig_to_html(fig)

    return html_str


def plot_deaths(death_data, titles):
    fig = plt.figure()

    plt.bar(death_data.index,
            death_data,
            lw=3,
            color='tab:red')

    plt.title(titles['figure'],
              fontdict=title_font)
    plt.ylabel(titles['y'],
               fontdict=axis_font)
    fig.autofmt_xdate(rotation=45)
    html_str = mpld3.fig_to_html(fig)

    return html_str
