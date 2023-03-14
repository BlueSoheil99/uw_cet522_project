import matplotlib.pyplot as plt
import seaborn as sns
from data_handler.data_query import get_data


def make_FD(route, direction, milepost, daily_average, weekend, start_date, end_date, start_time, end_time):
    data = get_data(route, direction, [milepost], daily_average=daily_average, weekend=weekend,
                    start_date=start_date, end_date=end_date, start_time=start_time, end_time=end_time)[0]
    data['volume'] = data['Volume (5-mins all lanes)']*12
    data['density'] = data.volume/data.speed


    fig, axs = plt.subplots(2, 2)
    fig.tight_layout(pad=2.5)

    ax1 = sns.scatterplot(data=data, x='density', y='volume', ax=axs[0, 0],
                         alpha=0.2, marker='.')
    ax2 = sns.scatterplot(data=data, x='density', y='speed', ax=axs[1, 0],
                         alpha=0.2, marker='.')
    ax3 = sns.scatterplot(data=data, x='volume', y='speed', ax=axs[1, 1],
                         alpha=0.2, marker='.')
    axs[0,1].remove()
    plt.suptitle(f'FD for {route} in {direction} direction, '
                    f'milepost {milepost} ')

    return axs

if __name__ == '__main__':
    make_FD('I5', 'Increasing', milepost=168.85)
