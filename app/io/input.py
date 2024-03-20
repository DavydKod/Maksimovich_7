import pandas


def input_text_console():
    '''
    For inputting text from console.

    Examples:
        >>> input_text_console()
        Text from console
        Text from console

    Returns:
        str: text from the console.
    '''
    text = input("Enter your text:")
    return text

def read_file(filename):
    '''
    Reads file and returns it's content.

    Args:
        filename (str): name of the file that will be read.

    Examples:
         >>> read_file("Book.txt")

    Returns:
        str: text from the file.
    '''
    try:
        with open(filename, 'r') as file:
            data = file.read()
        return data
    except FileNotFoundError:
        return "FileNotFound"

def read_file_pandas(filename):
    '''
    Reads file and returns it's content using pandas.

    Args:
        filename (str): name of the file that will be read.

    Examples:
         >>> read_file_pandas("Book.txt")

    Returns:
        str: text from the file.
    '''
    try:
        data = pandas.read_csv(filename)
        return data
    except FileNotFoundError:
        return "FileNotFound"