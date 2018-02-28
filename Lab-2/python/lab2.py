import re
import numpy as np
import struct
from struct import *
import struct

X_INPUT = 'lab2-x.txt'
Y_INPUT = 'lab2-y.txt'

x_string = open(X_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')
y_string = open(Y_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')

x_values = [] # [float, sign, integer, fraction]
y_values = [] # [float, sign, integer, fraction]

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

def twos_comp_w(val, precision):
    if(val == ''):
        val = 0
    else:
        val = int(val, 2)
    val = ~val  # flip the bits
    val += 1  # add one (two's complement method)
    p = '0' + str(precision - 1) + 'b'
    binary = str(format(val, p))
    binary = binary.replace('-', '1')
    return binary

def twos_comp_f(val, precision):
    p = '0' + str(precision - 1) + 'b'
    p = '0' + str(precision - 2) + 'b'
    if (val == ''):
        val = 0
    else:
        val = int(val, 2)
    if (val == 0):
        print(str(format(0,p)))
        return str(format(0,p))
    val = val - (1 << precision - 2)
    p = '0' + str(precision - 1) + 'b'
    binary = str(format(val, p))
    binary = binary.replace('-', '')
    print(binary)
    return binary

for i in range(0, len(x_string)-1):
    value = x_string[i]
    vector = ['1', '0', '0', '0']
    vector[0] = value
    if (value[0] == '-'):
        value = value.replace('-', '')
        vector[1] = '1'
    split = value.split('.')
    vector[2] = split[0]
    if (len(split) == 2):
        vector[3] = split[1]
    x_values.append(vector)

for i in range(0, len(y_string)-1):
    value = y_string[i]
    vector = ['1', '0', '0', '0']
    vector[0] = value
    if (value[0] == '-'):
        value = value.replace('-', '')
        vector[1] = '1'
    split = value.split('.')
    vector[2] = split[0]
    if (len(split) == 2):
        vector[3] = split[1]
    y_values.append(vector)

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

x_output = ''
y_output = ''

for i in range(len(x_values)):
    complement = x_values[i][1]
    complement += twos_comp_w((str(bin(int((x_values[i][2]))))).replace('0b',''), w_precision)
    complement += '.'
    complement += twos_comp_f(convertFractionToBinary(x_values[i][3]), f_precision+2)
    x_output += complement + ' '

for i in range(len(y_values)):
    complement = y_values[i][1]
    complement += twos_comp_w((str(bin(int((y_values[i][2]))))).replace('0b',''), w_precision)
    complement += '.'
    complement += twos_comp_f(convertFractionToBinary(y_values[i][3]), f_precision+2)
    x_output += complement + ' '

writer = open('lab1-x-fixed-point.txt', 'w')
writer.write(x_output)
writer = open('lab1-y-fixed-point.txt', 'w')
writer.write(y_output)

print(convertFractionToBinary('1'))