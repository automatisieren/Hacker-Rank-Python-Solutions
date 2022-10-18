import math
import os
import random
import re
import sys
from datetime import datetime

# The only question that I had to check on Internet
# Thanks: https://github.com/abrahamalbert18/HackerRank-Solutions-in-Python/blob/master/Time%20Delta

# Complete the time_delta function below.
def time_delta(t1, t2):
    t1_datetime = datetime.strptime(t1, "%a %d %b %Y %H:%M:%S %z")
    t2_datetime = datetime.strptime(t2, "%a %d %b %Y %H:%M:%S %z")
    result = t1_datetime - t2_datetime
    return int(abs(result.total_seconds()))
        
if __name__ == '__main__':
    t = int(input())
    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        print(delta)