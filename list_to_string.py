# Programa simples para pegar uma lista de matrículas e retorná-las numa única string para serem adicionadas no sistema
from utils.GUI import GUI


def handle_file(filepath):
    matricula = ''
    path = filepath[0].split('/')
    path = '/'.join(path[0:-1])
    with open(filepath[0]) as file:
        lines = file.readlines()
        for line in lines:
            matricula += line.replace('\n', ',')

    with open(f'{path}/test.txt', 'w') as file:
        file.write(matricula)


gui = GUI(1, 'Juntar Matrículas', 135, handle_file)
gui.create_button(0, 'Abrir Arquivo', 'open')
gui.create_button(1, 'Juntar Matrículas', 'handle_file')
gui.mainloop()
