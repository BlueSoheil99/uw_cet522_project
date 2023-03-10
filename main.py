import data_handler.meta_creator
import logic.fd
import logic.mfd
import os
import matplotlib.pyplot as plt


def analyze_command(input_list):

    return None


if __name__ == '__main__':
    mileposts_list = data_handler.meta_creator.extract_list_of_mileposts('I5', 'Increasing')
    # test.run()
    print('main dir: '+os.getcwd())
    ax = logic.mfd.make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])
    plt.show()
    ax = logic.fd.make_FD('I5', 'Increasing', milepost=168.85)
    plt.show()
    # # app = Application()
    # app.run()\
    # while True:
    #     app_inputs = app.get_input()
    #     output = analyze_command(app_inputs)
    #     app.show_result(output)
