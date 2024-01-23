#!/usr/bin/python3
'''This module is to define a script that reads stdin line by line and computes metrics'''


import sys

cache = {'200': 0, '301': 0, '400': 0, '401': 0,
         '403': 0, '404': 0, '405': 0, '500': 0}
total_s = 0
coun = 0

try:
    for l in sys.stdin:
        line_list = l.split(" ")
        if len(line_list) > 4:
            code = line_list[-2]
            size = int(line_list[-1])
            if code in cache.keys():
                cache[code] += 1
            total_s += size
            coun += 1

        if coun == 10:
            coun= 0
            print('File size: {}'.format(total_size))
            for key, value in sorted(cache.items()):
                if value != 0:
                    print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_s))
    for key, value in sorted(cache.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
