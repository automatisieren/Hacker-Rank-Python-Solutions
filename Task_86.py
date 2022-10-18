#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter
from operator import itemgetter

if __name__ == '__main__':
    s = input()
    counter = Counter(sorted(s)).most_common(3)
    for k,v in counter:
        print(f"{k} {v}")
        
    