''' Converts the fractional component to a binary string '''
def convertFractionToBinary(digits):
    fraction = float('0.' + digits)
    binary = ''
    while(fraction != 0.0):
        fraction = fraction * 2
        if (fraction < 1):
            binary = binary + '0'
        else:
            binary = binary + '1'
            fraction = fraction - 1
    return binary

''' Converts the w component to its twos complement with the correct precision '''
def twos_comp_w(val, precision):
    p = '0' + str(precision) + 'b'
    converted = bin(int(val) % (1 << precision))
    binary = format(int(converted, 2), p)
    return binary

''' Converts the f component to its twos complement with the correct precision '''
def twos_comp_f(val, precision):
    while (len(val) <= precision):
        val = val + '0'
    return val

# Input files
X_INPUT = 'lab2-x.txt'
Y_INPUT = 'lab2-y.txt'

# Read input files
x_string = open(X_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')
y_string = open(Y_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')

# Store x andy values in a vector format
x_values = [] # [float, sign, integer, fraction]
y_values = [] # [float, sign, integer, fraction]

# Read x values and store in the vector format
for i in range(0, len(x_string)-1):
    value = x_string[i]
    vector = ['1', '', '0', '0']
    vector[0] = value
    if (value[0] == '-'):
        value = value.replace('-', '')
        vector[1] = '-'
    split = value.split('.')
    vector[2] = split[0]
    if (len(split) == 2):
        vector[3] = split[1]
    x_values.append(vector)

# Read y values and store in the vector format
for i in range(0, len(y_string)-1):
    value = y_string[i]
    vector = ['1', '', '0', '0']
    vector[0] = value
    if (value[0] == '-'):
        value = value.replace('-', '')
        vector[1] = '-'
    split = value.split('.')
    vector[2] = split[0]
    if (len(split) == 2):
        vector[3] = split[1]
    y_values.append(vector)

# Calculate the precision for w and f values
w_precision = 1
f_precision = 0
for i in range(len(x_values)):
    w = 1
    f = 0
    w += len(bin(int(x_values[i][2]))) - 2 # precision of decimal
    f += len(convertFractionToBinary(x_values[i][3])) # precision of fraction
    if (w > w_precision):
        w_precision = w
    if (f > f_precision):
        f_precision = f
for i in range(len(y_values)):
    w = 1
    f = 0
    w += len(bin(int(y_values[i][2]))) - 2 # precision of decimal
    f += len(convertFractionToBinary(y_values[i][3])) # precision of fraction
    if (w > w_precision):
        w_precision = w
    if (f > f_precision):
        f_precision = f
print('W Precision: ', w_precision)
print('F Precision: ', f_precision)

# Store the twos complements output
x_output = ''
y_output = ''

# Convert all x values to twos complements
for i in range(len(x_values)):
    complement = twos_comp_w(x_values[i][1] + x_values[i][2], w_precision)
    complement = complement + twos_comp_f(convertFractionToBinary(x_values[i][3]), f_precision)
    x_output = x_output + complement + '\n'

# Converts all y values to twos complements
for i in range(len(y_values)):
    complement = twos_comp_w(y_values[i][1] + y_values[i][2], w_precision)
    complement = complement + twos_comp_f(convertFractionToBinary(y_values[i][3]), f_precision)
    y_output = y_output + complement + '\n'

# Write the result to an output file
writer = open('lab2-x-fixed-point.txt', 'w')
writer.write(x_output)
writer = open('lab2-y-fixed-point.txt', 'w')
writer.write(y_output)
