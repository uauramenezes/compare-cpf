import csv
import sys

# Besides Pandas (pip3 install pandas) it's also needs xlrd (pip3 install xlrd)
# import pandas as pd
# data = pd.read_excel(r"teste.xls")
# cpf_excel = data['CPF'].to_list()

# lines = []
# with open("cpf.txt") as f:
#     lines = f.read().splitlines()  # Removes only \n

if len(sys.argv) < 3:
    raise ValueError(
        'Por favor, informe o nome dos arquivos a serem comparados.')


cpf_obito = []
with open(sys.argv[1]) as file:
    lines = file.read().splitlines()
    for line in lines:
        cpf_obito.append(line[163:174])


cpf_prev = []
prev = []
with open(sys.argv[2], newline='') as csvfile:
    column = csv.reader(csvfile, delimiter=',')
    next(column)
    for row in column:
        cpf_prev.append(row[0])
        prev.append(row)


cpf = set(cpf_prev).intersection(cpf_obito)

result = []
for item in cpf:
    index = cpf_prev.index(item)
    result.append(prev[index])

with open('obitos.txt', 'w') as file:
    for item in result:
        file.write(" ".join(item) + '\n')
