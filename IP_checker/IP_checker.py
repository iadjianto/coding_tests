# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:39:32 2022

@author: isaiah

Check a .txt file of possible IP addresses and asses which are valid
"""

#import sys

evaluated = []

#for line in sys.stdin:
with open('IP_checker_input.txt') as file:
    lines = file.readlines()
    for line in lines:
        if len(line.split(':')) == 8:
            i=0
            for hexacandidate in line.split(':'):
                try: 
                    int(hexacandidate, 16)
                    i+=1
                except ValueError:
                    break
            if i == 8:
                evaluated.append((line,'IPv6'))
            else:
                evaluated.append((line,'Neither'))
            #print(line,end='')
        elif len(line.split('.')) == 4:
            try:
                if int(max(line.split('.'))) <=255:
                    evaluated.append((line,'IPv4'))
                else:
                    evaluated.append((line,'Neither'))
            except ValueError:
                evaluated.append((line,'Neither'))
            #print(line,end='')
        elif len(line) < 4:
            continue
            #print(line,end='')
        elif len(line) > 500:
            evaluated.append((line,'Neither'))
            #print(line,end='')
        else:
            evaluated.append((line,'Neither'))
            #print(line,end='')

expected = []
with open('IP_checker_output_expected.txt') as file:
    lines = file.readlines()
    for line in lines:
        expected.append(line)


status = True
for i in range(len(expected)):
    if str(evaluated[i][1]) != str(expected[i].strip()):
        status = False
        print('Problem at: ',evaluated[i],end="\texpected\t")
        print(expected[i])
        break

if status:
    print('All results OK')