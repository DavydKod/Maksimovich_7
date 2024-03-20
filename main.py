from app.io.input import *
from app.io.output import *


def main():
    console_text = input_text_console()
    read_text = read_file("data/First.txt")
    pandas_text = read_file_pandas("data/Second.txt")

    output_console(console_text)
    output_console(read_text)
    output_console(pandas_text)

    output_file(console_text ,"data/Third.txt")
    output_file(read_text, "data/Fourth.txt")

if __name__ == "__main__":
    main()