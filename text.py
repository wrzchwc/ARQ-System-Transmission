filepath = 'txt/sampleACAD.txt'
output = 'txt/data.txt'

data = []

with open(filepath) as file:
    for line in file:
        for name in line.split():
            data.append(name)

with open(output, 'w') as file:
    for name in data:
        file.write(name + '\n')
