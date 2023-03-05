import os
import pandas as pd
from . import meta_creator


def _read_meta(adr='../data/metadata.xlsx'):
    metadata = pd.read_excel(adr)
    metadata.set_index(metadata.columns[0], inplace=True)
    return metadata


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


def _extract_mileposts(dataframes, column_names, mileposts, periods):
    template = {col: [] for col in column_names}
    template[column_names[0]] = list(dataframes[0][0].iloc[:, 0])*len(dataframes)
    start, end = [], []
    for i in range(len(dataframes)):
        a = [periods[i][0]] * 288
        b = [periods[i][1]] * 288
        start.extend(a)
        end.extend(b)
    template[column_names[1]] = start
    template[column_names[2]] = end
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
        # todo if the file was read bfore, then do not read it fully again
        dataframes.append(_read_whole_excel(meta.file_adr, sheet_names))
        files_dates.append((meta.start_date, meta.end_date))
    DFs_for_mileposts = _extract_mileposts(dataframes, column_names, mileposts, files_dates)
    return DFs_for_mileposts


print('query.py dir: ' +os.getcwd())
metadata = meta_creator.create_meta()

if __name__ == '__main__':
    # print(os.getcwd())
    data = get_data('I5', 'Increasing', mileposts=[168.85], daily_average=True, weekend=False)
