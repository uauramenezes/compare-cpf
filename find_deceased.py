# Programa para comparar as tabelas da Previcon com o arquivo de falecidos dos mês e retornar pessoas em comum
# Indicando falecimento de aposentados da Previcon sem notificação

from tkinter.messagebox import showinfo
from tkinter import filedialog as fd
from tkinter import ttk
import tkinter as tk
import csv
import re


def find_deceased(files):
    # TODO: Try to return single lists
    previcon = {
        'cpf': [],
        'name': [],
        'registration': []
    }

    deceased = {
        'cpf': [],
        'mothers_name': [],
        'date_of_birth': [],
        'date_of_death': [],
    }

    def handle_obi_file(path):
        with open(path) as file:
            lines = file.read().splitlines()
            for line in lines:
                deceased['cpf'].append(line[163:174])
                deceased['mothers_name'].append(line[115:147])
                deceased['date_of_birth'].append(line[147:155])
                deceased['date_of_death'].append(line[155:163])

    def handle_csv(path):
        with open(path, newline='') as csvfile:
            lines = csv.reader(csvfile, delimiter=';')
            next(lines)
            for row in lines:
                if row[0] == "*":
                    continue
                cpf = row[2].replace('.', '').replace('-', '')
                previcon['cpf'].append(cpf)
                previcon['name'].append(row[0])
                previcon['registration'].append(row[1])

    def get_previcon_deceased_list():
        previcon_deceased_list = []
        cpf_list = set(previcon['cpf']).intersection(deceased['cpf'])
        for item in cpf_list:
            index_previcon = previcon['cpf'].index(item)
            index_deceased = deceased['cpf'].index(item)
            prev_deceased = [previcon['cpf'][index_previcon],
                             previcon['registration'][index_previcon],
                             deceased['date_of_birth'][index_deceased],
                             deceased['date_of_death'][index_deceased],
                             previcon['name'][index_previcon],
                             deceased['mothers_name'][index_deceased],
                             ]
            previcon_deceased_list.append(prev_deceased)
        return previcon_deceased_list

    def create_file():
        previcon_deceased = get_previcon_deceased_list()

        path = files[0].split('/')
        path = '/'.join(path[0:-1])
        fields = ['CPF', 'Matrícula', 'Nascimento',
                  'Data Óbito', 'Mãe', 'Nome']
        with open(f'{path}/Óbitos.csv', 'w', newline='') as file:
            csv_writer = csv.writer(file, delimiter=';')
            csv_writer.writerow(fields)
            csv_writer.writerows(previcon_deceased)

        # header = 'CPF\t\t\tMatrícula\tNascimento\t\tÓbito\t\t\tMãe\t\t\t\t\tNome\n'
        # with open(f'{path}/Óbitos.txt', 'w') as file:
        #     file.write(header)
        #     for item in previcon_deceased:
        #         file.write(f"\t".join(item) + '\n')

    for file in files:
        file_format = file.split('.').pop()
        if len(files) > 3:
            files.pop()
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
