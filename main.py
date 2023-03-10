import logic.fd
import logic.mfd
import os
import matplotlib.pyplot as plt


req_code = 1
route = 'I5'


def analyze_command(input_list):
    return None


if __name__ == '__main__':
    print('main dir: '+os.getcwd())
    ax = logic.mfd.make_MFD('I5', 'Increasing', milepost=[168.85, 170.25])
    plt.show()
    # app = Application()
    # app.run()\
    # while True:
    #     app_inputs = app.get_input()
    #     output = analyze_command(app_inputs)
    #     app.show_result(output)
