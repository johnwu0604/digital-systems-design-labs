import re
import numpy as np
import struct

def float_to_binary(float_):
    # Turns the provided floating-point number into a fixed-point
    # binary representation with 2 bits for the integer component and
    # 6 bits for the fractional component.

    temp = float_ *2**6  # Scale the number up.
    temp = int(temp)     # Turn it into an integer.
    # If you want -1 to display as 0b11000000, include this part:
    # if temp < 0:
    #     temp += 2**8

    # The 0 means "pad the number with zeros".
    # The 8 means to pad to a width of 8 characters.
    # The b means to use binary.
    return '{:08b}'.format(temp)


X_INPUT = 'lab2-x.txt'
Y_INPUT = 'lab2-y.txt'

x_string = open(X_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')
y_string = open(Y_INPUT, 'r', encoding="utf-8").readlines()[0].split(' ')

x_float = []
y_float = []

for i in range(0, len(x_string)-1):
    x_float.append(float(x_string[i]))

for i in range(0, len(y_string)-1):
    y_float.append(float(y_string[i]))

n = float_to_binary(6.125435345345345)
print(n)









