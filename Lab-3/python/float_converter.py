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
    while (len(val) < precision):
        val = val + '0'
    return val[:precision]

''' Calculate the precision based on the start and end indices '''
def calculatePrecision(input_values, start, end):
    # Calculate the precision for w and f values
    w_precision = 1
    f_precision = 0
    for i in range(start, end):
        w = 1
        f = 0
        w += len(bin(int(input_values[i][2]))) - 2  # precision of decimal
        f += len(convertFractionToBinary(input_values[i][3]))  # precision of fraction
        if (w > w_precision):
            w_precision = w
        if (f > f_precision):
            f_precision = f
    return w_precision, f_precision

''' Calculates twos complements based on precision and indices to include '''
def calculateTwosComplements(input_values, w_precision, f_precision, start, end):
    # Store the twos complements output
    output = []
    # Convert all x values to twos complements
    for i in range(start, end):
        complement = ''
        if (input_values[i][1] == '-'):
            complement = '1'
        else:
            complement = '0'
        complement = complement + twos_comp_f(convertFractionToBinary(input_values[i][3]), f_precision)
        output.append(complement)
    return output

''' Writes the output to a file '''
def writeOutput(output_values, filename):
    output = ''
    for i in range(len(output_values)):
        output = output + output_values[i] + '\n'
    writer = open(filename, 'w')
    writer.write(output)

# Input files
X_INPUT = 'lab3-in.txt'
C_INPUT = 'lab3-coeff.txt'

# Read input files
x_string = open(X_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')
c_string = open(C_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')

# Store x and c values in a vector format
x_values = [] # [float, sign, integer, fraction]
c_values = [] # [float, sign, integer, fraction]

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

# Read c values and store in the vector format
for i in range(0, len(c_string) - 1):
    value = c_string[i]
    vector = ['1', '', '0', '0']
    vector[0] = value
    if (value[0] == '-'):
        value = value.replace('-', '')
        vector[1] = '-'
    split = value.split('.')
    vector[2] = split[0]
    if (len(split) == 2):
        vector[3] = split[1]
    c_values.append(vector)

# Calculate precision for main batch
w, f = calculatePrecision(x_values, 0, len(x_values))
print('Input W Precision: ', w)
print('Input F Precision: ', f, '\n')

# Calculate twos complements based on precision for main batch and writes to file
output = calculateTwosComplements(x_values, 1, 15, 0, len(x_values))
writeOutput(output, 'lab3-in-fixed-point.txt')

# Calculate precision for main batch
w, f = calculatePrecision(c_values, 0, len(c_values))
print('Coefficient W Precision: ', w)
print('Coefficient F Precision: ', f, '\n')

# Calculate twos complements based on precision for main batch and writes to file
output = calculateTwosComplements(c_values, 1, 15, 0, len(c_values))
writeOutput(output, 'lab3-coeff-fixed-point.txt')


