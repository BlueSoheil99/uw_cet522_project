from data_handler import meta_creator
from logic import fd, mfd
import os
import matplotlib.pyplot as plt
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
    # ax = logic.mfd.make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])
    # plt.show()
    # ax = logic.fd.make_FD('I5', 'Increasing', milepost=168.85)
    # plt.show()]
    # app = Application()
    # while app.isRunning():
    #     input = app.run()
