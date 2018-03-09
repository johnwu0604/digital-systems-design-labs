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
    return val

''' Calculate the precision based on the start and end indices '''
def calculatePrecision(x_values, y_values, start, end):
    # Calculate the precision for w and f values
    w_precision = 1
    f_precision = 0
    for i in range(start, end):
        w = 1
        f = 0
        w += len(bin(int(x_values[i][2]))) - 2  # precision of decimal
        f += len(convertFractionToBinary(x_values[i][3]))  # precision of fraction
        if (w > w_precision):
            w_precision = w
        if (f > f_precision):
            f_precision = f
    for i in range(start, end):
        w = 1
        f = 0
        w += len(bin(int(y_values[i][2]))) - 2  # precision of decimal
        f += len(convertFractionToBinary(y_values[i][3]))  # precision of fraction
        if (w > w_precision):
            w_precision = w
        if (f > f_precision):
            f_precision = f
    return w_precision, f_precision

''' Calculates twos complements based on precision and indices to include '''
def calculateTwosComplements(x_values, y_values, w_precision, f_precision, start, end):
    # Store the twos complements output
    x_output = []
    y_output = []
    # Convert all x values to twos complements
    for i in range(start, end):
        complement = twos_comp_w(x_values[i][1] + x_values[i][2], w_precision)
        complement = complement + twos_comp_f(convertFractionToBinary(x_values[i][3]), f_precision)
        x_output.append(complement)
    # Converts all y values to twos complements
    for i in range(start, end):
        complement = twos_comp_w(y_values[i][1] + y_values[i][2], w_precision)
        complement = complement + twos_comp_f(convertFractionToBinary(y_values[i][3]), f_precision)
        y_output.append(complement)
    return x_output, y_output

''' Writes the output to a file '''
def writeOutput(output_values, filename):
    output = ''
    for i in range(len(output_values)):
        output = output + x_output[i] + '\n'
    writer = open(filename, 'w')
    writer.write(output)

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

# Calculate precision for main batch
w, f = calculatePrecision(x_values, y_values, 0, 1000)
print('Overall W Precision: ', w)
print('Overall F Precision: ', f, '\n')

# Calculate twos complements based on precision for main batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 0, 1000)
writeOutput(x_output, 'lab2-x-fixed-point.txt')
writeOutput(y_output, 'lab2-y-fixed-point.txt')

# Calculate precision for 1st batch
w, f = calculatePrecision(x_values, y_values, 0, 200)
print('Batch 1 W Precision: ', w)
print('Batch 1 F Precision: ', f, '\n')

# Calculate twos complements based on precision for 1st batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 0, 200)
writeOutput(x_output, 'lab2-x-fixed-point-batch1.txt')
writeOutput(y_output, 'lab2-y-fixed-point-batch1.txt')

# Calculate precision for 2nd batch
w, f = calculatePrecision(x_values, y_values, 200, 400)
print('Batch 2 W Precision: ', w)
print('Batch 2 F Precision: ', f, '\n')

# Calculate twos complements based on precision for 2nd batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 200, 400)
writeOutput(x_output, 'lab2-x-fixed-point-batch2.txt')
writeOutput(y_output, 'lab2-y-fixed-point-batch2.txt')

# Calculate precision for 3rd batch
w, f = calculatePrecision(x_values, y_values, 400, 600)
print('Batch 3 W Precision: ', w)
print('Batch 3 F Precision: ', f, '\n')

# Calculate twos complements based on precision for 3rd batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 400, 600)
writeOutput(x_output, 'lab2-x-fixed-point-batch3.txt')
writeOutput(y_output, 'lab2-y-fixed-point-batch3.txt')

# Calculate precision for 4th batch
w, f = calculatePrecision(x_values, y_values, 600, 800)
print('Batch 4 W Precision: ', w)
print('Batch 4 F Precision: ', f, '\n')

# Calculate twos complements based on precision for 4th batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 600, 800)
writeOutput(x_output, 'lab2-x-fixed-point-batch4.txt')
writeOutput(y_output, 'lab2-y-fixed-point-batch4.txt')

# Calculate precision for 5th batch
w, f = calculatePrecision(x_values, y_values, 800, 1000)
print('Batch 5 W Precision: ', w)
print('Batch 5 F Precision: ', f, '\n')

# Calculate twos complements based on precision for 5th batch and writes to file
x_output, y_output = calculateTwosComplements(x_values, y_values, w, f, 800, 1000)
writeOutput(x_output, 'lab2-x-fixed-point-batch5.txt')
writeOutput(y_output, 'lab2-y-fixed-point-batch5.txt')
