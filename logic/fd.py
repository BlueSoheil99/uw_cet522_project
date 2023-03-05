import seaborn as sns
from data_handler.data_query import get_data


def make_FD(route, direction, milepost,
            start_date='2016-01-01', end_date='2016-12-31', start_time='00:00', end_time='23:55'):
    data = get_data(route, direction, [milepost])[0]
    data['volume'] = data['Volume (5-mins all lanes)']*12
    data['density'] = data.volume/data.speed

    ax = sns.scatterplot(data=data, x='density', y='volume',
                         alpha=0.2, marker='.').set(title=f'FD for {route} in {direction} direction, milepost {milepost}')
    return ax


if __name__ == '__main__':
    make_FD('I5', 'Increasing', milepost=168.85)
