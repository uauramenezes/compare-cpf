# Programa simples para pegar uma lista de matrículas e retorná-las numa única string para serem adicionadas no sistema

matricula = ''
with open('matriculas.txt') as file:
    lines = file.readlines()
    for line in lines:
        matricula += line.replace('\n', ',')

with open('test.txt', 'w') as file:
    file.write(matricula)
