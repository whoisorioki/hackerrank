#!/bin/python3

import math
import os
import random
import re
import sys


def hour_glass():
    hour_glass_list = []
    for i in range(4):
        for j in range(4):
            r1 = arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
            r2 = arr[i + 1][j + 1]
            r3 = arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2]
            total = r1 + r2 + r3
            hour_glass_list.append(total)

    return max(hour_glass_list)


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(hour_glass())