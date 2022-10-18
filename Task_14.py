def decimal2Binary(num : int, resList : list) -> None:
    if num >= 1:
        decimal2Binary(num = num // 2, resList = resList)
        resList.append(num % 2)

def decimal2Hex(num: int) -> str:
    return hex(num).replace('0x', '').upper()

def decimal2Octal(num: int) -> int:
    res = 0
    count = 1
    while(num != 0):
        remain = num % 8
        res += remain * count
        count *= 10
        num //= 8
    return res

def calculateMaxPad(num : int) -> int:
    decimal2BinaryList = []
    decimal2Binary(num = num, resList = decimal2BinaryList)
    pad = len(decimal2BinaryList) + 1
    return pad

def print_formatted(number):
    # your code goes here
    maxPad = calculateMaxPad(num = number)
    hex_pad = 1
    for i in range(1, number+1, 1):        
        # Decimal
        decimal_pad = len(str(i))
        print(" " * (maxPad - decimal_pad - 1)  + f"{i}", end="")
        # Octal
        octal_value = decimal2Octal(num = i)
        octal_pad = len(str(octal_value))
        print(" " * (maxPad - octal_pad) + f"{octal_value}", end="")        
        # Hex
        hex_value = decimal2Hex(num = i)
        if i > 15:
            hex_pad = 2
        print(" " * (maxPad - hex_pad) + f"{hex_value}", end="")
        # Binary        
        decimal2BinaryList = []
        decimal2Binary(num = i, resList = decimal2BinaryList)
        binary_pad = len(decimal2BinaryList)
        print(" " * (maxPad - binary_pad) + ''.join(str(a) for a in decimal2BinaryList), end="")
        print("\n", end="")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)