import pandas


def output_console(text):
    '''
    Prints the text in the console.

    Examples:
        >>> output_console("Text to print")
        Text to print

    Args:
        text (str): text that will be printed in console.
    '''
    print(text)

def output_file(text, filename):
    '''
    Writes the text to the file.

    Examples:
        >>> output_console("Text to write", "Book.txt")

    Args:
        text (str): text that will be written to the file.
        filename (str): name of the file where the text will be written.

    Returns:
        bool: True if everything is okay and False if otherwise
    '''
    try:
        with open(filename, 'w') as file:
            file.write(text)
    except Exception as e:
        print(f"Error: {e}")

def output_file_pandas(text, filename):
    '''
    Writes the text to the file using pandas.

    Examples:
        >>> output_console("Text to write", "Book.txt")

    Args:
        text (str): text that will be written to the file.
        filename (str): name of the file where the text will be written.

    Returns:
        bool: True if everything is okay and False if otherwise
    '''
    try:
        df = pandas.DataFrame({'Text': [text]})
        df.to_csv(filename, index=False)
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False