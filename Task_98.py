regex_integer_in_range = r"^[1-9]{1}[0-9]{5}$"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d)(?=(\d)\1)"	# Do not delete 'r'.


import re
P = input()

print(bool(re.match(regex_integer_in_range, P)))
 
print(re.findall(regex_alternating_repetitive_digit_pair, P))