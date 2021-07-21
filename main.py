from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
import csv
import re


def search_cpf(files):
    cpf_obito = []
    cpf_prev = []
    prev = []

    def open_obi_file(path):
        with open(path) as file:
            lines = file.read().splitlines()
            for line in lines:
                cpf_obito.append(line[163:174])

    def open_csv(path):
        with open(path, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            index = next(lines).index("CPF")
            for row in lines:
                if row[0] == "*":
                    continue
                cpf = row[index].replace('.', '').replace('-', '')
                cpf_prev.append(cpf)
                prev.append(row[0:3])

    def create_file():
        cpf = []
        cpf_list = set(cpf_prev).intersection(cpf_obito)
        for item in cpf_list:
            index = cpf_prev.index(item)
            cpf.append(prev[index])

        path = files[0].split('/')
        path = '/'.join(path[0:-1])
        with open(f'{path}/obi/obitos.txt', 'w') as file:
            for item in cpf:
                file.write(f"\t\t".join(item[::-1]) + '\n')

    for file in files:
        file_format = file.split('.').pop()
        if bool(re.search("OBI", file_format)):
            open_obi_file(file)
        elif file_format == "csv":
            open_csv(file)
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


root = tk.Tk()
root.title('Comparar arquivos')
root.resizable(False, False)
root.geometry('450x150')

files = []


def select_files():
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
        files.insert(n, path[n])
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
    if len(files) == 0:
        return

    search_cpf(files)


create_button(0, "Abrir arquivo", select_files)
create_button(1, "Fazer busca", search)

root.mainloop()
