def print_menu(title, list_options):
    """Prints options in standard menu format

    Args:
        title (str): the title of the menu (first row)
        list_options (list): list of the menu options (listed starting from 1, 0th element goes to the end)
    """
    print(title)
    for index, item in enumerate(list_options):
        try:
            print(f"({index + 1}) {list_options[index + 1]}")
        except IndexError:
            print("(0)",list_options[0])


def print_message(message):
    """Prints a single message to the terminal.

    Args:
        message: str - the message
    """
    print(message)


def print_general_results(result, label):
    """Prints out any type of non-tabular data.
    It should print numbers (like "@label: @value", floats with 2 digits after the decimal),
    lists/tuples (like "@label: \n  @item1; @item2"), and dictionaries
    (like "@label \n  @key1: @value1; @key2: @value2")
    """
    if type(result) == int:
        print(label + ": " + str(float(result)))
    elif type(result) == list or type(result) == tuple:
        print(label)
        for index, item in enumerate(result):
            if index <= len(result) - 2:
                print(item, end="; ")
            else:
                print(item)
    elif type(result) == dict:
        print(label)
        for index, item in enumerate(result):
            if index <= len(result) - 2:
                print(item + ": " + str(result[item]), end="; ")
            else:
                print(item + ": " + str(result[item]))


def print_table(headers, table):

    """Prints tabular data in a table.

    Args:
        table: list of lists - the table to print out
    """
    for index, item in enumerate(headers):
        if index < len(headers) - 1:
            print(item.center(20), end="|")
        else:
            print(item.center(20), end="|\n")

    for row in table:
        for index, item in enumerate(row):
            if index < len(row) - 1:
                print(item.center(20), end="|")
            else:
                print(item.center(20), end="|\n")

            
def get_input(label):
    """Gets single string input from the user.

    Args:
        label: str - the label before the user prompt
    """
    choice = input(label)
    return choice
    

def get_inputs(labels):
    """Gets a list of string inputs from the user.

    Args:
        labels: list - the list of the labels to be displayed before each prompt
    """
    result = []
    for item in labels:
        result.append(input(item + ": "))

    return result


def print_error_message(message):
    """Prints an error message to the terminal.

    Args:
        message: str - the error message
    """
    print(message)


#print_menu("data to be modified", ["Id", "Name", "Date of birth", "Department", "Clearance"])