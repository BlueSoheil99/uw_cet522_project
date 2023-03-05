import data_handler.data_query as data_query


def make_MFD(route, mile_start, mile_end, Week_of_the_year):
    data = data_query.get_data()
    # process data
    plot = 'a plot you just made!'
    return plot


if __name__ == '__main__':
    make_MFD('I5', 0, 190)

