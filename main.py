# run application


# get input from user
    # a list of inputs.
    # The list starts with a code by which we know what functinos to run and how to interpret the input


# get data from database


# run the request
req_code = 1
route = 'I5'

# respond to the application

def analyze_command(input_list):

    return None

if __name__ == '__main__':
    app = Application()
    app.run()
    while True:
        app_inputs = app.get_input()
        output = analyze_command(app_inputs)
        app.show_result(output)