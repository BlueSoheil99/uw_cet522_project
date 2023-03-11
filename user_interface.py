import streamlit as st
import os
import matplotlib.pyplot as plt
from PIL import Image
from datetime import datetime
import warnings

warnings.simplefilter("ignore")


class Application:
    def __init__(self):
        self.milepost = None  # when calling fd, it's a float -- when calling mfd, it's a list
        self.is_running = False
        self.command = None
        self.milepost_list = []
        self.route = ""
        self.direction = ""
        self.start_date = datetime(2016, 1, 1)
        self.end_date = datetime(2016, 12, 31)


    def isRunning(self):
        return self.is_running

    def run(self):
        self.is_running = True
        from main import get_mileposts, analyze_command

        self.route = st.selectbox("Select route", ["I5"])
        self.direction = st.selectbox("Select increasing or decreasing", ["Increasing", "Decreasing"])
        self.command = st.selectbox("Select FD or MFD", ["FD", "MFD"])
        self.milepost_list = get_mileposts(self.route, self.direction)
        mp = self.milepost_list

        # if self.command == 'mfd':
        if self.command == 'MFD':
            mfd_start = st.selectbox("Select the starting milepost:", mp)
            mfd_end = st.selectbox("Select the ending milepost:", mp[mp.index(mfd_start) + 1:])
            self.milepost = mp[mp.index(mfd_start): mp.index(mfd_end) + 1]

        # elif self.command == 'fd':
        elif self.command == 'FD':
            self.milepost = st.selectbox("Select a milepost:", mp)

        self.start_date = st.date_input("Select a start date", value=datetime(2016, 1, 1),
                                        min_value=datetime(2016, 1, 1), max_value=datetime(2016, 12, 31))

        self.end_date = st.date_input("Select an end date", value=self.start_date,
                                      min_value=self.start_date,max_value=datetime(2016, 12, 31))


        ax = analyze_command(self.command, self.route, self.direction, self.milepost_list, self.start_date, self.end_date)
        #
        # if self.command == 'FD':
        #     plot_fd(route, direction, milepost_fd)
        #     image = Image.open('C:\\Users\\12066\\Desktop\\Pycharm\\uw_cet522_project\\fd.png')
        #     fig = plt.figure(figsize=(10, 4))
        #     st.image(image)
        #
        # if self.command == 'MFD':
        #     plot_mfd(route, direction, milepost_mfd_list)
        #     image = Image.open('C:\\Users\\12066\\Desktop\\Pycharm\\uw_cet522_project\\mfd.png')
        #     fig = plt.figure(figsize=(10, 4))
        #     st.image(image)
        plt.show()


# def plot_fd(routee, directionn, fd_mpp):
#         from logic import fd
#         ax = fd.make_FD(routee, directionn, milepost=fd_mpp)
#         plt.savefig('fd.png')
#         return ()
#
#
# def plot_mfd(routee, directionn, mfd_mp_first_lastt):
#         from logic import mfd
#         ax = mfd.make_MFD(routee, directionn, milepost=mfd_mp_first_lastt)
#         plt.savefig('mfd.png')
#         return ()

def find_closest_value_index(target_value, list_of_values):
        closest_value = min(list_of_values, key=lambda x: abs(x - target_value))
        closest_index = list_of_values.index(closest_value)
        return (closest_index)

app = Application()
app.run()

