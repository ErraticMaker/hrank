#!/bin/python3


def offset(time):
    if (time[-2:] == 'PM' and time[:2] != '12' or
            time[-2:] == 'AM' and time[:2] == '12'):
        return 12
    else:
        return 0

time = input().strip()
print('{:0>2}{}'.format((int(time[:2]) + offset(time)) % 24, time[2:-2]))
