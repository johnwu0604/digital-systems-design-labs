INPUT = 'lab3-coeff-fixed-point.txt'
OUTPUT = 'lab3-coeff-fixed-point-reversed.txt'
values = open(INPUT, 'r', encoding="utf-8").readlines()

inverse = []
for line in values[::-1]:
    n = line.split('\n')
    inverse.append(n[0])

output = ''
for i in inverse:
    output = output + i + '\n'
writer = open(OUTPUT, 'w')
writer.write(output)