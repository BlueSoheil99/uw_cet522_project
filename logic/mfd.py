import pandas as pd
import seaborn as sns
from data_handler.data_query import get_data

global datamfd
datamfd=pd.DataFrame()
def make_MFD(route, direction, milepost):
    global datamfd
    for i in range(len(milepost)):
        global data
        data = get_data(route, direction, [milepost[i]])[0]
        data['volume'] = data['Volume (5-mins all lanes)'] * 12
        data['density'] = data.volume / data.speed
        data=data[['volume', 'density']]
        if datamfd.empty:
            datamfd=data
        else:
            datamfd+=data



    datamfd=datamfd/(i+1)
    ax = sns.scatterplot(data=datamfd, x='density', y='volume',
                         alpha=0.2, marker='.').set(
        title=f'MFD for {route} in {direction} direction, milepost {milepost}')
    return ax


if __name__ == '__main__':
    make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])

