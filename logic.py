import pandas as pd

dataframes = []
metadata = pd.DataFrame(data={'id': [], 'file_name': [], 'route': [], 'milepost': [], 'lane': [],
                              'weekend': [], 'start_date': [], 'end_date': []})


def fetch_data(route, milepost, lanes):
    # return list of indices of dataframes needed to work with
    # connect to database module which will modify 'dataframes' and 'metadata'
    return None


def get_FD(route, milepost, lanes, start_date, end_date, start_time, end_time):
    df_indices = fetch_data(route, milepost, lanes)
    return None
