from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk


class GUI(tk.Tk):
    def __init__(self, number_of_files, title, window_height, handle_file) -> None:
        tk.Tk.__init__(self)
        self.size = number_of_files
        self.files = []
        self.title(title)
        self.height = window_height
        self.geometry(f'500x{window_height}')
        self.resizable(False, False)
        self.handle_file = handle_file

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
            if n == self.size:
                break

    def __handle_file(self):
        if len(self.files) == 0:
            return
        self.handle_file(self.files)
        showinfo(
            title='Concluído',
            message="Arquivo criado"
        )

    def __create_button(self, column, text, command):

        function = self.__select_files if command == 'open' else self.__handle_file

        button = ttk.Button(
            self,
            text=text,
            command=function
        )

        button.grid(padx=10, pady=10, row=4, column=column)
        button.place(x=column * 180 + 100, y=self.height - 35)

    def __create_label(self, row, text):
        label = ttk.Label(width=55, text=text)
        label.grid(padx=10, pady=5, row=row, column=1)

    def create_gui(self, button_text):
        self.__create_button(0, 'Abrir Arquivo', 'open')
        self.__create_button(1, button_text, 'handle_file')
