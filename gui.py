import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

root = tk.Tk()
root.title('Comparar arquivos')
# root.resizable(False, False)
root.geometry('450x150')

files = []


def select_files():
    filetypes = (
        ('All files', '*.*'),
        ('csv files', '*.csv'),
        ('text files', '*.txt'),
    )

    files = []

    path = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)
    if len(path) == 0:
        return

    for n in range(0, len(path)):
        files.append(path[n])
        filename = path[n].split('/').pop()
        create_label(n, filename)
        if n >= 2:
            break


def create_button(column, text, function):
    # open button
    open_button = ttk.Button(
        root,
        text=text,
        command=function
    )

    open_button.grid(padx=10, pady=5, row=4, column=column)
    open_button.place(x=column * 200 + 100, y=111)


def create_label(row, text):
    label = ttk.Label(width=55, text=text)
    label.grid(padx=10, pady=5, row=row, column=1)


def search():
    showinfo(
        title='Concluído',
        message="Arquivo criado"
    )


create_button(0, "Abrir arquivo", select_files)
create_button(1, "Fazer busca", search)

root.mainloop()
