import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from data_handler.data_query import get_data


def make_MFD (route, direction, milepost):
    datamfd = pd.DataFrame()
    for i in range(len(milepost)):
        data = get_data(route, direction, [milepost[i]])[0]
        data['volume'] = data['Volume (5-mins all lanes)'] * 12
        data['density'] = data.volume / data.speed
        data['speed'] = data.speed
        data=data[['volume', 'density', 'speed']]
        if datamfd.empty:
            datamfd=data
        else:
            datamfd+=data

    datamfd=datamfd/(len(milepost))

    fig, axs = plt.subplots(2, 2)
    fig.tight_layout(pad=1.0)

    ax1 = sns.scatterplot(data=datamfd, x='density', y='volume', ax=axs[0,0],
                         alpha=0.2, marker='.')
    ax2 = sns.scatterplot(data=datamfd, x='density', y='speed', ax=axs[1,0],
                         alpha=0.2, marker='.')
    ax3 = sns.scatterplot(data=datamfd, x='volume', y='speed', ax=axs[1,1],
                         alpha=0.2, marker='.')
    axs[0,1].remove()
    plt.suptitle(f'MFD for {route} in {direction} direction, '
                    f'milepost {milepost[0]} to {milepost[-1]}')


    # fig.suptitle('MfD plots')
    # axs[0, 0].plot(ax)  # fk
    # axs[1, 0].plot(ax)  # vk
    # axs[1, 1].plot(ax)  # vf

    return axs

if __name__ == '__main__':
    make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])

