import os
import pandas as pd
import numpy as np
from . import meta_creator
from datetime import date, datetime, time

START_DATE_DEFAULT = date(2016, 1, 1)
END_DATE_DEFAULT = date(2016, 12, 31)
START_TIME_DEFAULT = time(0, 0, 0)
END_TIME_DEFAULT = time(23, 55, 0)


def _filter_date_months(dataframe, column_names, dates):
    start_cname, end_cname = column_names[0], column_names[1]
    # start_date, end_date = dates[0], dates[1]  # start should be prior to end. front end handles that
    start_month, end_month = dates[0].month, dates[1].month
    x = dataframe[start_cname].apply(lambda date: date.month) == start_month
    y = dataframe[end_cname].apply(lambda date: date.month) == end_month
    first = np.argwhere(np.array(x))[0][0]
    second = np.argwhere(np.array(y))[-1][0]
    return dataframe.iloc[first:second+1, :]


def _filter_date_time(milepost_DFs, column_names, start_date, end_date, start_time, end_time, daily_average):
    start_date_cname, end_date_cname, time_cname = column_names[1], column_names[2], column_names[0]
    for i, df in enumerate(milepost_DFs):
        df = df[start_time <= df[time_cname]]
        df = df[df[time_cname] <= end_time]
        if not daily_average:
            df = df[df[start_date_cname] >= start_date]
            df = df[df[end_date_cname] <= end_date]
        milepost_DFs[i] = df
    return milepost_DFs


def _select_files(route, direction, daily_average, weekend, start_date, end_date):
    df = metadata[metadata.route == route]
    df = df[df.weekend == weekend]
    df = df[df.direction == direction]
    if daily_average:
        df = df[df.type == 'averaged daily data']
    else:
        df = df[df.type == 'daily data']
    df = _filter_date_months(df, ('start_date', 'end_date'), (start_date, end_date))
    df.reset_index(drop=True, inplace=True)
    return df


def _extract_mileposts(dataframes, column_names, mileposts, periods, daily_average):
    # in case column_names are : ['time', 'start_date', 'end_date', 'speed', 'Volume (5-mins all lanes)']
    template = {col: [] for col in column_names}
    # for average daily files the first columns are just time, for daily files, it's date and time

    if daily_average:
        times = dataframes[0][0].iloc[:, 0]
        times = times.apply(lambda t: datetime.strptime(t, '%H:%M').time())
        template[column_names[0]] = list(times)*len(dataframes)
        # if we use daily data, we need another way to insert dates
        start, end = [], []
        for i in range(len(dataframes)):
            a = [periods[i][0]] * 288  # =24*12
            b = [periods[i][1]] * 288
            start.extend(a)
            end.extend(b)
        template[column_names[1]] = start
        template[column_names[2]] = end
    else:
        for i in range(len(dataframes)):
            DTs = dataframes[i][0].iloc[:, 0]
            DTs = DTs.apply(lambda dt: datetime.strptime(dt, '%Y-%m-%d %H:%M:%S'))
            template[column_names[0]].extend(DTs.apply(lambda dt: dt.time()))
            dates = DTs.apply(lambda dt: dt.date())
            template[column_names[1]].extend(dates)
            template[column_names[2]].extend(dates)

    DFs = [template] * len(mileposts)
    for sheets in dataframes:
        for i, df in enumerate(sheets):
            attr = column_names[i+3]
            for j, milepost in enumerate(mileposts):
                a = df.loc[:, milepost]
                DFs[j][attr].extend(a)
    ans = [pd.DataFrame(data=df, columns=column_names) for df in DFs]
    return ans


def _read_whole_excel(path, sheet_names):
    sheets = []
    for name in sheet_names:
        df = pd.read_excel(path, sheet_name=name)
        cols = list(df.columns)
        cols[0] = 'time'
        df.columns = cols
        sheets.append(df)
    print(f'read complete: {path}')
    return sheets


def get_data(route, direction, mileposts=None, daily_average=True, weekend=False,
             start_date=START_DATE_DEFAULT, end_date=END_DATE_DEFAULT,
             start_time=START_TIME_DEFAULT, end_time=END_TIME_DEFAULT):
    dataframes = []
    files_dates = []
    sheet_names = ['Speed', 'Volume (5-mins all lanes)']
    column_names = ['time', 'start_date', 'end_date', 'speed', 'Volume (5-mins all lanes)']

    file_metas = _select_files(route, direction, daily_average, weekend, start_date, end_date)
    for idx, meta in file_metas.iterrows():
        # # we save the files we read in RAM and when they are needed again, we'll use
        # # previously opened files, instead of reading those files again
        address = meta.file_adr  # meta is a row of meta table
        if address in opened_DFs.keys():
            dfs, dates = opened_DFs[address][0], opened_DFs[address][1]
            print(f'retrieved file: {address}')
        else:
            dfs = _read_whole_excel(meta.file_adr, sheet_names)
            dates = (meta.start_date, meta.end_date)
            opened_DFs[address] = [dfs, dates]
        dataframes.append(dfs)
        files_dates.append(dates)
    DFs_for_mileposts = _extract_mileposts(dataframes, column_names, mileposts, files_dates, daily_average)
    DFs_for_mileposts = _filter_date_time(DFs_for_mileposts,  column_names[:3], start_date, end_date,
                                          start_time, end_time, daily_average)
    return DFs_for_mileposts


print('query.py dir: ' + os.getcwd())
metadata = meta_creator.get_meta()
opened_DFs = {}

# if __name__ == '__main__':
    # print(os.getcwd())
    # data = get_data('I5', 'Increasing', mileposts=[168.85], daily_average=True, weekend=False)
