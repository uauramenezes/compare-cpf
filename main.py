# Besides Pandas (pip3 install pandas) it's also needs xlrd (pip3 install xlrd)
import pandas as pd
data = pd.read_excel(r"teste.xls")
cpf_excel = data['CPF'].to_list()

lines = []
with open("cpf.txt") as f:
    lines = f.read().splitlines()  # Removes only \n
    # lines = [line.rstrip() for line in f] # Removes all trailing whitespace

cpf = []

for n in range(0, len(cpf_excel)):
    for line in lines:
        if float(line) == cpf_excel[n]:
            cpf.append(line)

print(cpf)
