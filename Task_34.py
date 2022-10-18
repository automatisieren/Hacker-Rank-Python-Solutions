from sys import exit
from math import acos, degrees, hypot
if __name__ == "__main__":
    ab = int(input().strip())
    bc = int(input().strip())
    if (ab < 0 or ab > 100) or (bc < 0 or bc > 100):
        exit()
    hypotenuse = hypot(ab, bc)
    cos_bc = float(bc / hypotenuse)
    print(f"{round(degrees(acos(cos_bc)))}{chr(176)}")