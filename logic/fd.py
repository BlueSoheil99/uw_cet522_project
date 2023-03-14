import matplotlib.pyplot as plt
import seaborn as sns
from data_handler.data_query import get_data


def make_FD(route, direction, milepost, start_date='2016-01-01', end_date='2016-12-31', start_time='00:00', end_time='23:55'):
    data = get_data(route, direction, [milepost])[0]
    data['volume'] = data['Volume (5-mins all lanes)']*12
    data['density'] = data.volume/data.speed


    fig, axs = plt.subplots(2, 2)
    fig.tight_layout(pad=2.5)

    ax1 = sns.scatterplot(data=data, x='density', y='volume', ax=axs[0,0],
                         alpha=0.2, marker='.')
    ax2 = sns.scatterplot(data=data, x='density', y='speed', ax=axs[1,0],
                         alpha=0.2, marker='.')
    ax3 = sns.scatterplot(data=data, x='volume', y='speed', ax=axs[1,1],
                         alpha=0.2, marker='.')
    axs[0,1].remove()
    plt.suptitle(f'FD for {route} in {direction} direction, '
                    f'milepost {milepost} ')

    return axs

if __name__ == '__main__':
    make_FD('I5', 'Increasing', milepost=168.85)
