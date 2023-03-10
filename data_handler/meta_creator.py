import glob
import pandas as pd
import os


def _define_route(route):
    if route == '005':
        return'I5'
    elif route == '090':
        return 'I90'
    elif route == '520':
        return '520'
    else:
        return None


def _get_milepost(string):
    a = float(string[:-2])
    b = float(string[-2:])/100
    return a+b


def _get_metadata(file_name):
    name = file_name.split('_')
    route, direction, mile_start, mile_end, weekend, start, end =\
        _define_route(name[0]), name[1], name[2], name[3], name[4], name[5], name[6]
    if route is None:
        print('unknown route for '+file_name)

    return route, direction, mile_start, mile_end, weekend, start, end


def _create_meta(glob_address='./data/DriveNet/*/*.xlsx'):
    print('metacreator dir: '+os.getcwd())
    file_names = sorted(glob.glob(glob_address))

    info = {'file_adr': [], 'type': [], 'route': [], 'mile_start': [], 'mile_end': [],
            'weekend': [], 'direction': [], 'start_date': [], 'end_date': []}
    # for i, name in enumerate(file_names):
    for name in file_names:
        org_name = name
        name = name.split('/')
        pre_name = name[:-1]
        name = name[-1][:-5]  # remove '.xlsx' part
        route, direction, mile_start, mile_end, weekend, start, end = _get_metadata(name)

        # info['id'].append(i)
        info['file_adr'].append(org_name)
        info['type'].append(pre_name[-1])
        info['route'].append(route)
        info['mile_start'].append(mile_start)
        info['mile_end'].append(mile_end)
        info['direction'].append(direction)
        info['start_date'].append(start)
        info['end_date'].append(end)
        if weekend == 'MoTuWeThFr':
            info['weekend'].append(False)
        else:
            info['weekend'].append(True)

    metadata = pd.DataFrame(data=info)
    return metadata


def _extract_list_of_mileposts():
    n = len(metadata)
    file_number = random.randint(0, n-1)
    x = metadata.file_adr[file_number]
    df = pd.read_excel(x)
    mileposts = list(df.columns[1:])
    print(f'*** Mileposts are extracted from mileposts of file: {x}\n')
    return mileposts


def get_meta():
    return metadata


def get_mileposts():
    return mileposts


metadata = _create_meta()
mileposts = _extract_list_of_mileposts()



if __name__ == '__main__':
    file_names = sorted(glob.glob('./data/DriveNet/*/*.xlsx'))

    info = {'file_adr': [], 'type': [], 'route': [], 'mile_start': [], 'mile_end': [],
            'weekend': [], 'direction': [], 'start_date': [], 'end_date': []}

    # for i, name in enumerate(file_names):
    for name in file_names:
        org_name = name
        name = name.split('/')
        pre_name = name[:-1]
        name = name[-1][:-5]  # remove '.xlsx' part
        route, direction, mile_start, mile_end, weekend, start, end = _get_metadata(name)

        # info['id'].append(i)
        info['file_adr'].append(org_name)
        info['type'].append(pre_name[-1])
        info['route'].append(route)
        info['mile_start'].append(mile_start)
        info['mile_end'].append(mile_end)
        info['direction'].append(direction)
        info['start_date'].append(start)
        info['end_date'].append(end)
        if weekend == 'MoTuWeThFr':
            info['weekend'].append(False)
        else:
            info['weekend'].append(True)

    metadata = pd.DataFrame(data=info)
    # metadata.start_date = pd.to_datetime(metadata.start_date)
    # metadata.end_date = pd.to_datetime(metadata.end_date)
    metadata.to_excel('./data/metadata.xlsx')
