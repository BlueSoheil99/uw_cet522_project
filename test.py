import pandas as pd
import numpy as np
import seaborn as sns
import os


# ## loading file names and making metadata for data files

input_folder = 'data/'
file_names = os.listdir(input_folder)
print(file_names)

#
# # In[4]:
# def define_route(route):
#     if route=='005':
#         return'I5'
#     elif route=='090':
#         return 'I90'
#     elif route == '520':
#         return '520'
#     else:
#         return None
#
# def get_milepost(string):
#     a = float(string[:-2])
#     b = float(string[-2:])/100
#     return a+b
#
# def get_metadata(file_name):
#     name = file_name.split('_')
#     route, milepost, lane, weekend, start, end = define_route(name[0][:3]), name[0][-5:], name[4], name[5], name[6], name[7]
#     if route is None:
#         print('unknown route for '+file_name)
#     return route, get_milepost(milepost), lane, weekend, start, end
#
#
#
# # In[5]:
#
#
# # get data files info
# # 520es00972_MW___3_MoTuWeThFr_2015-01-01_2015-12-31.csv :
# #        (Route 520, milepost 9.72, general purpose lane, mainline, westbound, shared thru,
# #         mainline, not speed loop/speed trap/meter rate, lane 3, Monday through Friday in 2015)
#
# # I don't understand lane details (general purpose lane, mainline, westbound, shared thru, mainline, not speed loop/speed trap/meter rate)
# info = {'id':[], 'file_name':[], 'route':[], 'milepost':[], 'lane':[], 'weekend':[], 'start_date':[], 'end_date':[] }
#
# for i, name in enumerate(file_names):
#     name = name[:-5]  # remove '.xlsx' part
#     route, milepost, lane, weekend, start, end = get_metadata(name)
#     info['id'].append(i)
#     info['file_name'].append(name)
#     info['route'].append(route)
#     info['milepost'].append(milepost)
#     info['lane'].append(lane)
#     info['start_date'].append(start)
#     info['end_date'].append(end)
#     if weekend == 'MoTuWeThFr':
#         info['weekend'].append(False)
#     else:
#         info['weekend'].append(True)
#
# metadata = pd.DataFrame(data=info)
# metadata.start_date = pd.to_datetime(metadata.start_date)
# metadata.end_date = pd.to_datetime(metadata.end_date)
# # metadata
#
#
# # ## loading dataframes
#
# # In[62]:
#
#
# speed, VpLpH, occupancy = [], [], []
# for name in file_names:
#     name = input_folder+name
#     speed.append(pd.read_excel(name, sheet_name='Speed', index_col=0))
#     VpLpH.append(pd.read_excel(name, sheet_name='Volume Per Lane', index_col=0))
#     occupancy.append(pd.read_excel(name, sheet_name='Occupancy', index_col=0))
#
#
# # In[130]:
#
#
# s = speed[0]
# vpl = VpLpH[0]
# occ = occupancy[0]
# aggregated = {'time':[], 'date':[], 'speed':[], 'occupancy':[], 'volumePL':[]}
# for time in s.index:
#     for date in s.columns[1:]:
#         aggregated['time'].append(time)
#         aggregated['date'].append(date)
#         aggregated['speed'].append(s.loc[time, date])
#         aggregated['occupancy'].append(occ.loc[time, date])
#         aggregated['volumePL'].append(vpl.loc[time, date])
# data = pd.DataFrame(data=aggregated)
# # data.set_index(['time', 'date'], inplace=True)
# data['date'] = pd.to_datetime(data.date)
# data['time'] = pd.to_datetime(data.time).dt.time
# data
#
#
# # In[142]:
# # sns.scatterplot(data=data[data.date == '2015-01-02'], x='occupancy', y='speed', alpha=0.1)
# # sns.scatterplot(data=data[data.date.apply(lambda d:d.month) == 1], x='occupancy', y='speed', alpha=0.2, hue='volumePL', marker='.')
# sns.scatterplot(data=data, x='occupancy', y='speed', alpha=0.2, hue=data.date.apply(lambda d:d.month), marker='.')
#
#
#
# # In[ ]:
#
#
# def get_FD(route, milepost):
#     # aggregate different lanes of the nearest post
#     return None
#
#
# # ## interaction with logic
#
# # In[ ]:
#
#
#
#
