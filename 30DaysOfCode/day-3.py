#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    if N % 2 != 0:
        print('Weird')
    elif N % 2 == 0:
        if N < 6 and N > 1:
            print('Not Weird')
        elif N < 21 and N > 5:
            print('Weird')
        elif N > 20:
            print('Not Weird')
