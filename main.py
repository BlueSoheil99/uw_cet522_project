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
from datetime import datetime
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
    print('main dir: '+os.getcwd())
    ax = mfd.make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])
    plt.show()
    # ax = logic.fd.make_FD('I5', 'Increasing', milepost=168.85)
    # plt.show()]
    # app = Application()
    # while app.isRunning():
    #     input = app.run()

    warnings.simplefilter("ignore")
    route = st.selectbox("Select route", ["I5"])
    direction = st.selectbox("Select increasing or decreasing", ["Increasing", "Decreasing"])
    fd_mfd = st.selectbox("Select FD or MFD", ["FD", "MFD"])
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

    start_date = st.date_input("Select a start date", value = datetime(2016, 1, 1),
                               min_value = datetime(2016, 1, 1),
                               max_value = datetime(2016, 12, 31))

    end_date = st.date_input("Select an end date", value=start_date,
                             min_value=start_date,
                             max_value=datetime(2016, 12, 31))

    def plot_fd(routee, directionn, fd_mpp):
        #if fd_mpp <120:
            #fd_mpp = mp[mp.index(fd_mpp) +1]
        ax = fd.make_FD(routee, directionn, milepost=fd_mpp)
        plt.savefig('fd.png')
        return ()


    def plot_mfd(routee, directionn, mfd_mp_first_lastt):
        ax = mfd.make_MFD(routee, directionn, milepost=mfd_mp_first_lastt)
        plt.savefig('mfd.png')
        return ()


    if fd_mfd and fd_mfd == 'FD':
        plot_fd(route, direction, milepost_fd)
        image = Image.open('fd.png')
        fig = plt.figure(figsize=(10, 4))
        st.image('fd.png')

    if fd_mfd and fd_mfd == 'MFD':

        plot_mfd(route, direction, milepost_mfd_list)
        #image = Image.open('C:\\Users\\12066\\Desktop\\Pycharm\\uw_cet522_project\\mfd.png')
        image = Image.open('mfd.png')
        fig = plt.figure(figsize=(10, 4))
        st.image('mfd.png')
