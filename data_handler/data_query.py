import os
import pandas as pd
from . import meta_creator


def _select_files(route, direction, daily_average=True, weekend=False, start_date='2016-01-01', end_date='2016-12-31'):
    df = metadata[metadata.route == route]
    df = df[df.weekend == weekend]
    df = df[df.direction == direction]
    if daily_average:
        df = df[df.type == 'averaged daily data']
    else:
        df = df[df.type == 'daily data']
    # todo handling dates, which should be implemented in the end of this function, and prevent duplicates
    df.reset_index(drop=True, inplace=True)
    return df


def _extract_mileposts(dataframes, column_names, mileposts, periods, daily_average=True):
    # in case column_names are : ['time', 'start_date', 'end_date', 'speed', 'Volume (5-mins all lanes)']
    template = {col: [] for col in column_names}
    original_first_column = dataframes[0][0].iloc[:, 0]  # todo convert it to datetime dtype
    # for average daily files it's just time, for daily files, it's date and time
    if daily_average:
        template[column_names[0]] = list(original_first_column)*len(dataframes)
        # if we use daily data, we need another way to insert dates
        start, end = [], []
        for i in range(len(dataframes)):
            a = [periods[i][0]] * 288  # =24*12
            b = [periods[i][1]] * 288
            start.extend(a)
            end.extend(b)
        template[column_names[1]] = start
        template[column_names[2]] = end
    # else: # todo what if we want to use daily data instead of average data?
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


def get_data(route, direction, mileposts=None, daily_average=True, weekend=False, start_date='2016-01-01', end_date='2016-12-31'):
    dataframes = []
    files_dates = []
    sheet_names = ['Speed', 'Volume (5-mins all lanes)']
    column_names = ['time', 'start_date', 'end_date', 'speed', 'Volume (5-mins all lanes)']

    file_metas = _select_files(route, direction, daily_average, weekend)
    for idx, meta in file_metas.iterrows():
        # dataframes.append(_read_whole_excel(meta.file_adr, sheet_names))
        # files_dates.append((meta.start_date, meta.end_date))
        # # instead of two lines above, we save the files we read in RAM and when they are needed again, we'll use
        # # previously opened files, instead of reading those files again
        address = meta.file_adr  #meta is a row of meta table
        if address in opened_DFs.keys():
            dfs, dates = opened_DFs[address][0], opened_DFs[address][1]
            dataframes.append(dfs)
            files_dates.append(dates)
            print(f'retrieved file: {address}')
        else:
            dfs = _read_whole_excel(meta.file_adr, sheet_names)
            dates = (meta.start_date, meta.end_date)
            dataframes.append(dfs)
            files_dates.append(dates)
            opened_DFs[address] = [dfs, dates]
    DFs_for_mileposts = _extract_mileposts(dataframes, column_names, mileposts, files_dates)
    return DFs_for_mileposts


print('query.py dir: ' + os.getcwd())
metadata = meta_creator.get_meta()
opened_DFs = {}

if __name__ == '__main__':
    # print(os.getcwd())
    data = get_data('I5', 'Increasing', mileposts=[168.85], daily_average=True, weekend=False)
