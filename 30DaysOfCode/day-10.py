#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # binary = list('{0:b}'.format(int(n)))
    binary = []
    while n > 0:
        remainder = n % 2
        n = n // 2
        binary.append(remainder)

    binary = list(reversed(binary))

    count = 0
    max_count = 0
    for i in binary:
        if i == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0

    if count > max_count:
        max_count = count

    print(max_count)


    print(binary)
    print(count)


