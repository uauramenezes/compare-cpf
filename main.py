from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
import csv
import re


def find_deceased(files):
    cpf_obito = []
    cpf_prev = []
    prev = []

    def handle_obi_file(path):
        with open(path) as file:
            lines = file.read().splitlines()
            for line in lines:
                # TODO: Return date of death
                cpf_obito.append(line[163:174])

    def handle_csv(path):
        with open(path, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            index = next(lines).index("CPF")
            for row in lines:
                if row[0] == "*":
                    continue
                # TODO: Try to return a single lists
                cpf = row[index].replace('.', '').replace('-', '')
                cpf_prev.append(cpf)
                prev.append(row[0:3])

    def get_cpf_list():
        cpf = []
        cpf_list = set(cpf_prev).intersection(cpf_obito)
        for item in cpf_list:
            index = cpf_prev.index(item)
            cpf.append(prev[index])
        return cpf

    def create_file():
        cpf = get_cpf_list()

        path = files[0].split('/')
        path = '/'.join(path[0:-1])
        # TODO: Write the columns names
        with open(f'{path}/obitos.txt', 'w') as file:
            for item in cpf:
                file.write(f"\t\t".join(item[::-1]) + '\n')

    for file in files:
        file_format = file.split('.').pop()
        if bool(re.search("OBI", file_format)):
            handle_obi_file(file)
        elif file_format == "csv":
            handle_csv(file)
        else:
            showinfo(
                title='Formato de Arquivo não Suportado',
                message=f"Arquivos do tipo {file_format} não são suportados"
            )
            return

    create_file()
    showinfo(
        title='Concluído',
        message="Arquivo criado"
    )


class GUI(tk.Tk):
    def __init__(self, title, size, resize) -> None:
        tk.Tk.__init__(self)
        self.files = []
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
            self.create_label(n, filename)
            if n >= 2:
                break

    def __search(self):
        if len(self.files) == 0:
            return
        find_deceased(self.files)

    def create_button(self, column, text, command):

        function = self.__select_files if command == 'open' else self.__search

        button = ttk.Button(
            self,
            text=text,
            command=function
        )

        button.grid(padx=10, pady=5, row=4, column=column)
        button.place(x=column * 180 + 100, y=111)

    def create_label(self, row, text):
        label = ttk.Label(width=55, text=text)
        label.grid(padx=10, pady=5, row=row, column=1)


gui = GUI('Comparar arquivos', '450x150', False)
gui.create_button(0, 'Abrir arquivo', 'open')
gui.create_button(1, 'Fazer busca', 'search')
gui.mainloop()
