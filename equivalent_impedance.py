#this program tries to find the equivalent impedance of a network

import cmath
import math


def equivalent_impedance(z):
    node_E = []
    node_S = []
    impedance = []
    for i in range(len(z)):
        node_E.append(z[i][2])
        node_S.append(z[i][1])
        impedance.append(z[i][0])
    node_E = node_E[::-1]
    node_S = node_S[::-1]
    impedance = impedance[::-1]
    print(node_E, '\n', node_S)
    sum = impedance.pop(0)
    y = 1
    count = 0
    end = node_E.pop(0)
    start = node_S.pop(0)
    while y:
        if len(node_E) == 0:
            y = 0
        elif end == node_E[count] and start == node_S[count]:
            sum = 1 / ((1 / sum) + (1 / impedance[count]))
            node_S.pop(count)
            node_E.pop(count)
            impedance.pop(count)
            count = 0
            continue
        elif end > node_S[count] and start == node_E[count]:
            sum = sum + impedance[count]
            start = node_S[count]
            node_S.pop(count)
            node_E.pop(count)
            impedance.pop(count)
            count = 0
            continue
        count += 1
    return sum


print('***please prioritize starting node while inputting data i.e. if node a is connected to components ending at b,'
      'c,d,e then input a b, a c, a d, a e***')
z = []
f = 1
print('input values of resistance(1), capacitance(2) and inductance(3):[4 when done input is done] ')
print('type value node_S node_E')
while f:
    x = input()
    x = (x.split(' '))
    count = 0
    for i in x:
        x[count] = float(i)
        count += 1
    if x[0] == 1:
        z.append(x[1:len(x)])
    elif x[0] == 2:
        x[1] = 1 / (2 * math.pi * 1j * 60 * x[1])
        z.append(x[1:len(x)])
    elif x[0] == 3:
        x[1] = (2 * math.pi * 1j * 60 * x[1])
        z.append(x[1:len(x)])
    elif x[0] == 4:
        f = 0
    else:
        print('wrong choice')
print(z)
Zeq = equivalent_impedance(z)

print('Equivalent Impedance of the Network: ', Zeq)
