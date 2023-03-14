from data_handler import meta_creator
import data_handler.meta_creator
import logic.fd
import logic.mfd
import os
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore")
import matplotlib.pyplot as plt
import streamlit as st
from datetime import date, time
import warnings
from logic import fd, mfd
import os
import matplotlib.pyplot as plt
from logic import mfd
from logic import fd
from copy import deepcopy
from PIL import Image

# from user_interface import Application



def analyze_command(command, route, direction, milepost, start_d, end_d):
    if command == 'MFD':
        # return logic.mfd.make_MFD(route, direction, milepost=milepost, start_d, end_d)
        return mfd.make_MFD(route, direction, milepost=milepost)
    elif command == 'FD':
        # return logic.fd.make_FD(route, direction, milepost, start_d, end_d)
        return fd.make_FD(route, direction, milepost)


def get_mileposts(route, direction):
    return meta_creator.extract_list_of_mileposts(route, direction)


if __name__ == '__main__':
    # mileposts_list = meta_creator.extract_list_of_mileposts('I5', 'Increasing')
    #print('main dir: '+os.getcwd())
    #ax = mfd.make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])
    #plt.show()
    # ax = logic.fd.make_FD('I5', 'Increasing', milepost=168.85)
    # plt.show()]
    # app = Application()
    # while app.isRunning():
    #     input = app.run()

    warnings.simplefilter("ignore")
    st.write('<span style="font-size: 36px;">Fundamental/ Macroscopic Fundamental Diagram of Seattle Highways</span>', unsafe_allow_html=True)

    st.write(
        '<div style="background-color: blue; color: white; padding: 10px; border: 1px solid white;">By: Soheil Keshavarz, Shakiba Naderian, and Mohammad Mehdi Oshanreh</div>',
        unsafe_allow_html=True)

    route = st.selectbox("Select route", ["I5"])
    direction = st.selectbox("Select increasing or decreasing", ["Increasing", "Decreasing"])
    fd_mfd = st.selectbox("Select FD or MFD", ["FD", "MFD"])
    st.markdown("""
    <div style="background-color: #aaa;
                height: 4px;
                background-image: linear-gradient(to right, #00b4db, #0083b0, #6a82fb, #e60073);
                margin-top: 25px;
                margin-bottom: 25px;">
    </div>
    """, unsafe_allow_html=True)

    st.write('<span style="font-size: 24px;">Select Starting Time</span>', unsafe_allow_html=True)

    shour = st.slider('Hour', 0, 23, step=1)
    sminute = st.slider('Minute', 0, 55, step=5)

    start_time = time(shour, sminute,0)
    print('*********')
    print(start_time)
    print('******')

    st.markdown("""
    <div style="background-color: #aaa;
                height: 4px;
                background-image: linear-gradient(to right, #00b4db, #0083b0, #6a82fb, #e60073);
                margin-top: 25px;
                margin-bottom: 25px;">
    </div>
    """, unsafe_allow_html=True)

    st.write('<span style="font-size: 24px;">Select Ending Time</span>', unsafe_allow_html=True)
    ehour = st.slider('Hour ', 0, 23, step=1,value=23)
    eminute = st.slider('Minute ', 0, 55, step=5,value=55)

    end_time = time(ehour, eminute,0)

    st.markdown("""
    <div style="background-color: #aaa;
                height: 4px;
                background-image: linear-gradient(to right, #00b4db, #0083b0, #6a82fb, #e60073);
                margin-top: 25px;
                margin-bottom: 25px;">
    </div>
    """, unsafe_allow_html=True)

    mpi = data_handler.meta_creator.extract_list_of_mileposts(route, 'Increasing')
    mpd = data_handler.meta_creator.extract_list_of_mileposts(route, 'Decreasing')

    mpi.sort()
    #Exclude non-Seattle sensors
    mpi = [i for i in mpi if i > 160 and i != 165.51]
    mpd.sort()
    mpd = [i for i in mpd if i > 160 and i != 165.51]
    mp = deepcopy(mpi)
    if direction == 'Decreasing':
        mp = deepcopy(mpd)

    if fd_mfd == "FD":
        milepost_fd = st.select_slider(
            'Enter the milepost',
            options = mp)
        #milepost_fd = st.selectbox("Select a milepost:", mp)

    else:

        #mfd_start = st.selectbox("Select the starting milepost:", mp)
        #mfd_end = st.selectbox("Select the ending milepost:", mp[mp.index(mfd_start)+1:])
        mfd_start, mfd_end = st.select_slider(
            'Select a range of milepost',
            options = mp,
            value=(mp[0], mp[-1]))
        milepost_mfd_list = mp[mp.index(mfd_start): mp.index(mfd_end)+1]
        #st.write(milepost_mfd_list,type(milepost_mfd_list))

    start_date = st.date_input("Select a start date", value = date(2016, 1, 1),
                               min_value = date(2016, 1, 1),
                               max_value = date(2016, 12, 31))

    end_date = st.date_input("Select an end date", value=date(2016, 12, 31),
                             min_value=start_date,
                             max_value=date(2016, 12, 31))
    avg_daily = st.selectbox    ('Select aggregation type',['Average Daily','Daily'])
    daily_average = False
    if avg_daily == 'Average Daily':
        daily_average = True
    day_type = st.selectbox('Select Day type',['WorkDay','Weekend'])
    isWeekend = False
    if day_type == 'Weekend':
        isWeekend = True

    def plot_fd(routee, directionn, fd_mpp,daily_avgg,isweekendd,start_date,end_date,start_time,end_time):
        print(routee, directionn, fd_mpp,daily_avgg,isweekendd,start_date,end_date,start_time,end_time)
        #if fd_mpp <120:
            #fd_mpp = mp[mp.index(fd_mpp) +1]
        ax = fd.make_FD(routee, directionn,fd_mpp,daily_avgg,isweekendd,start_date,end_date,start_time,end_time)
        plt.savefig('fd.png')
        return ()


    def plot_mfd(routee, directionn, mfd_mp_first_lastt):
        ax = mfd.make_MFD(routee, directionn, milepost=mfd_mp_first_lastt)
        plt.savefig('mfd.png')
        return ()


    if fd_mfd and fd_mfd == 'FD':
        plot_fd(route, direction, milepost_fd,daily_average,isWeekend,start_date,end_date,start_time,end_time)
        image = Image.open('fd.png')
        fig = plt.figure(figsize=(10, 4))
        st.image('fd.png')

    if fd_mfd and fd_mfd == 'MFD':

        plot_mfd(route, direction, milepost_mfd_list)
        #image = Image.open('C:\\Users\\12066\\Desktop\\Pycharm\\uw_cet522_project\\mfd.png')
        image = Image.open('mfd.png')
        fig = plt.figure(figsize=(10, 4))
        st.image('mfd.png')
