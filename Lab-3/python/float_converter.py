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

# Calculate twos complements and writes to file
output = calculateTwosComplements(x_values, 1, 15, 0, len(x_values))
writeOutput(output, 'lab3-in-fixed-point.txt')

# Calculate twos complements and writes to file
output = calculateTwosComplements(c_values, 1, 15, 0, len(c_values))
writeOutput(output, 'lab3-coeff-fixed-point.txt')


