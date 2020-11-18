import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
# plt.ioff()
import mpld3


def plot_cases(case_data, avg_case_data, titles):
    title_font = {'fontsize': 18,
                 }
    axis_font = {'fontsize': 14}

    fig = plt.figure()

    plt.bar(case_data.index,
            case_data,
            alpha=.6,
            color='tab:gray',
            label='Single Day Cases')
    plt.plot(avg_case_data,
             color='tab:red',
             lw=3,
             label='7 Day Average')
    plt.title(titles['figure'],
              fontdict=title_font)
    plt.xlabel(titles['x'],
               fontdict=axis_font)
    fig.autofmt_xdate(rotation=45)
    plt.legend()
    html_str = mpld3.fig_to_html(fig)

    return html_str