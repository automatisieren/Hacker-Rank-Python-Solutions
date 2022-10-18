#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    words = re.compile(r'(\s+)').split(s)
    return ''.join(element.capitalize() for element in words)

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)
    #fptr.write(result + '\n')

    #fptr.close()
