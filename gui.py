from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
import csv
import re


class GUI(tk.Tk):
    def __init__(self, title, size, resize) -> None:
        tk.Tk.__init__(self)
        self.title(title)
        self.geometry(size)
        self.resizable(resize, resize)

    def __select_files(self):
        filetypes = (
            ('All files', '*.*'),
            ('csv files', '*.csv'),
            ('text files', '*.txt'),
        )

        path = fd.askopenfilenames(
            title='Open files',
            initialdir='/',
            filetypes=filetypes)

        if len(path) == 0:
            return
        for n in range(0, len(path)):
            self.files.insert(n, path[n])
            filename = path[n].split('/').pop()
            self.__create_label(n, filename)
            if n >= 2:
                break

    def __search(self):
        if len(self.files) == 0:
            return

        # search_cpf(files)

    def create_button(self, row, text, command):

        function = self.__select_files if command == 'open' else self.__search

        button = ttk.Button(
            self,
            text=text,
            command=function
        )

        button.grid(padx=10, pady=5, row=row, column=0)
        button.place(x=10, y=row * 40 + 15)

    def __create_label(self, row, text):
        label = ttk.Label(width=55, text=text)
        label.grid(padx=10, pady=5, row=row, column=1)


gui = GUI('Comparar arquivos', '450x250', False)
gui.create_button(0, 'Abrir arquivo', 'open')
gui.create_button(1, 'Abrir arquivo', 'open')
gui.create_button(2, 'Abrir arquivo', 'open')
gui.mainloop()
