from tkinter import ttk
import tkinter
import string
from handlers import *

cyr_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
caps = False

def make_button(frame: ttk.Frame, label: ttk.Label, text: str) -> ttk.Button:
    # Buttons for chars
    button = ttk.Button(frame, text=text, command=button_handler(text, label))
    return button


def button_layout(frame: ttk.Frame, label: ttk.Label, caps: bool):
    # Lays out the char buttons, returns the last used row
    latin_alphabet = string.ascii_uppercase if caps else string.ascii_lowercase
    cur_cyr_alphabet = cyr_alphabet.upper() if caps else cyr_alphabet

    for i in range(len(latin_alphabet)):
        make_button(frame, label, latin_alphabet[i]).grid(row=2 + i//10, column=i%10)
        last_row_ascii = 2 + i//10

    for i in range(len(cur_cyr_alphabet)):
        make_button(frame, label, cur_cyr_alphabet[i]).grid(row=last_row_ascii + 1 + i//10, column=i%10)
        last_row_cyr = last_row_ascii + 1 + i//10

    for i in range(len(string.punctuation)):
        make_button(frame, label, string.punctuation[i]).grid(row=last_row_cyr + 1 + i//10, column=i%10)
        last_row_punct = last_row_cyr + 1 + i//10

    for i in range(10):
        make_button(frame, label, str(i)).grid(row=last_row_punct + 1 + i//10, column=i%10)
    
    return last_row_punct + 1 + i//10


def make_entry(frame: ttk.Frame, label: ttk.Label, row: int):
    entry = ttk.Entry(frame)
    button = ttk.Button(frame, text="Search!", command=entry_handler(entry, label))
    entry.grid(row=row, column=10)
    button.grid(row=row, column=11)


def make_capslock(frame: ttk.Frame, label: ttk.Label, last_row: int):
    ttk.Button(frame, text="CAPS", command=caps_handler(frame, label)).grid(row=last_row + 1, column=0)


def make_app():
    app = tkinter.Tk()
    frame = ttk.Frame(app)
    frame.grid(column=0, row=0, sticky=("N","E","W","S"))

    label = ttk.Label(frame, text="smth")
    label.grid(row=1,column=1)

    last_row = button_layout(frame, label, caps)

    make_capslock(frame, label, last_row)
    make_entry(frame, label, last_row + 1)
    
    return app


# THIS DOESN'T BELONG HERE
# TODO: find a way to escape having global variable
def caps_handler(frame: ttk.Frame, label: ttk.Label):
    def switch_caps():
        global caps
        if caps:
            caps = False
        else:
            caps = True

        button_layout(frame, label, caps)
    return switch_caps
